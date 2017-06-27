import unittest

# from validate import Validate
from validate.validate import Validator
from validate.error import *

class TestValidate(unittest.TestCase):

    def setUp(self):
        self.v = Validator()


    def test_schema_dict(self):
        self.v.set_rules(dict(name='llnhhy'), schema=dict(name='str'))
        self.v.set_rules(dict(name='llnhhy', age=17), schema=dict(name='str', age='int'))
        self.v.set_rules(dict(name='luo', girlfriend=dict(name='wu', age=20)), schema=dict(name='str', girlfriend=dict(name='str', age='int')))
        self.v.set_rules(dict(name='luo', girlfriend=dict(name='wu', age=20)), schema=dict(name='str', girlfriend='dict'))
        self.v.set_rules(dict(name='luo', girlfriend=['wu', 'sun', 'li']), schema=dict(name='str', girlfriend=['str', 'str', 'max_length:2']))
        self.v.set_rules({'name':'luo', 'age':20}, schema={'name':'str', 'age':'int'})
        self.v.set_rules({'name':'luo', 'age':20}, schema={'name':'str'})
        self.v.set_rules({'name':'luo', 'age':20}, schema={'name':'str', 'age':'int|min_length:2'})
        self.v.set_rules({'name':'luo', 'age':20}, schema='dict|max_length:2')

    def test_schema_list(self):
        self.v.set_rules([10, 20, 'string'], schema=['int', 'int', 'str'])
        # self.v.set_rules([10, 'string', [20, 'hello']], schema=['int', 'str', ['int', 'str']])

    def test_exact_length(self):
        rule = 'exact_length:{}'

        self.v.set_rules('hello', 'exact_length:5')
        self.v.set_rules(123, 'exact_length:3')
        self.v.set_rules(dict(name='luo'), 'exact_length:1')
        self.v.set_rules({'name':'luo', 'age':18}, 'exact_length:2')
        self.v.set_rules({'name':'luo', 'girlfriend':[]}, 'exact_length:2')
        self.v.set_rules(['1', '2'], 'exact_length:2')
        self.v.set_rules([1, 2], 'exact_length:2')
        self.v.set_rules([1, [2, 3], 4], 'exact_length:3')
        self.v.set_rules((1, 2, 3), 'exact_length:3')
        self.v.set_rules(123.123, 'exact_length:7')
        self.v.set_rules(None, 'exact_length:2')
        

    def test_max_length(self):
        '''
        test max_length
        '''
        string = 'hello world'
        self.assertRaises(Max_lengthError, self.v.set_rules, string, 'max_length:2')
        self.v.set_rules(string, 'max_length:20')
        self.v.set_rules(string, 'max_length:a')

    def test_min_length(self):
        string = 'hello world'
        self.v.set_rules(string, 'min_length:1')
        self.v.set_rules(string, 'min_length:a')
        self.assertRaises(Min_lengthError, self.v.set_rules, 'helo world', 'min_length:100')
        self.assertRaises(Min_lengthError, self.v.set_rules, '', 'min_length:1')

    def test_required(self):
        '''
        test required
        not None and not ''
        '''
        self.v.set_rules('hello world', 'required')
        self.v.set_rules(dict(name='python'), 'required')
        self.v.set_rules(True, 'required')
        self.v.set_rules(False, 'required')
        self.v.set_rules(0, 'required')
        self.v.set_rules(-1, 'required')
        self.v.set_rules(100.000, 'required')
        self.v.set_rules((1, 2, 3), 'required')
        self.v.set_rules(object, 'required')

        self.assertRaises(RequiredError, self.v.set_rules, tuple(), 'required')
        self.assertRaises(RequiredError, self.v.set_rules, dict(), 'required')
        self.assertRaises(RequiredError, self.v.set_rules, list(), 'required')
        self.assertRaises(RequiredError, self.v.set_rules, str(), 'required')
        self.assertRaises(RequiredError, self.v.set_rules, '', 'required')
        self.assertRaises(RequiredError, self.v.set_rules, 'hello'[:0], 'required')
        self.assertRaises(RequiredError, self.v.set_rules, None, 'required')

    def test_in_list(self):
        '''
        in list test
        '''
        self.v.set_rules('hello', 'in_list[hello, hellos]')
        self.v.set_rules('hello', 'in_listp[hello ]')
        self.v.set_rules('hello', 'in_list[hello,]')
        self.v.set_rules('hello world', 'in_list[hello world, hello]')
        self.v.set_rules('hello "world"', 'in_list[hello "world"]')
        self.assertRaises(In_listError, self.v.set_rules, 'hello', 'in_list:h')
        self.assertRaises(ValidateError, self.v.set_rules, 'hello', 'in_list:hell0')

    def test_str(self):
        '''
        test variable type
        '''
        self.v.set_rules('hello', 'str')
        self.v.set_rules('h', 'str')
        self.v.set_rules(str(float()), 'str')
        self.v.set_rules(str(bool()), 'str')

        self.assertRaises(GenreError, self.v.set_rules, 10, 'str')
        self.assertRaises(GenreError, self.v.set_rules, float(), 'str')
        self.assertRaises(GenreError, self.v.set_rules, bool(), 'str')
        self.assertRaises(GenreError, self.v.set_rules, dict(name='hello'), 'str')
        self.assertRaises(GenreError, self.v.set_rules, list('hello'), 'str')
        self.assertRaises(GenreError, self.v.set_rules, None, 'str')

    def test_dict(self):
        '''
        test attribute type of dict
        '''
        rule = 'dict'
        self.v.set_rules(dict(), rule)
        self.v.set_rules(dict(hello='hello'), rule)
        self.v.set_rules({'hello':'world'}, rule)

        self.assertRaises(GenreError, self.v.set_rules, 'dict', rule)
        self.assertRaises(GenreError, self.v.set_rules, list(), rule)
        self.assertRaises(GenreError, self.v.set_rules, tuple(dict()), rule)


    def test_ipv4(self):
        self.v.set_rules('192.168.1.1', 'ipv4')
        self.v.set_rules('0.0.0.0', 'ipv4')

        self.assertRaises(Ipv4Error, self.v.set_rules, '888.888.888.888', 'ipv4')
        self.assertRaises(Ipv4Error, self.v.set_rules, 'hello', 'ipv4')
        self.assertRaises(Ipv4Error, self.v.set_rules, 192, 'ipv4')
        self.assertRaises(Ipv4Error, self.v.set_rules, dict(), 'ipv4')
        self.assertRaises(Ipv4Error, self.v.set_rules, list("192.168.1.1"), 'ipv4')
        self.assertRaises(Ipv4Error, self.v.set_rules, bool(), 'ipv4')
        self.assertRaises(Ipv4Error, self.v.set_rules, tuple("192,168,1,1"), 'ipv4')
        self.assertRaises(Ipv4Error, self.v.set_rules, str('1920.168.1.1'), 'ipv4')
        self.assertRaises(Ipv4Error, self.v.set_rules, [192, 168, 1, 1], 'ipv4')

    def test_ipv6(self):
        rule = 'ipv6'

        self.v.set_rules('5e:0:0:0:0:0:5668:eeee', rule)
        self.v.set_rules('5e:0:0:023:0:0:5668:eeee', rule)
        self.v.set_rules('5e::5668:eeee', rule)
        self.v.set_rules('::1:8:8888:0:0:8', rule)
        self.v.set_rules('1::', rule)
        self.v.set_rules('::1:2:2:2', rule)
        self.v.set_rules('::', rule)

        # self.assertRaises(Ipv6Error, self.v.set_rules, '5e::5668::eeee', rule)
        self.assertRaises(Ipv6Error, self.v.set_rules, '55555:5e:0:0:0:0:0:5668:eeee', rule)

    def test_email(self):
        rule = 'email'

        self.v.set_rules('baidu@baidu.com', rule)
        self.v.set_rules('cadwqd233@cascsan.com', rule)
        self.assertRaises(EmailError, self.v.set_rules, '1234@@gs.com', rule)
        self.assertRaises(EmailError, self.v.set_rules, '123@gmail', rule)
        self.assertRaises(EmailError, self.v.set_rules, '123@gmail\.com', rule)
        self.assertRaises(EmailError, self.v.set_rules, list('123@gmail'), rule)

    def test_url(self):
        rule = 'url'

        self.v.url('ftp://www.baidu.com')
        self.v.set_rules('http://baidu.com', rule)
        self.v.set_rules('https://baidu.com', rule)
        self.v.set_rules('ftp://www.baidu.com', rule)

        # self.assertRaises(UrlError, self.v.set_rules, 'hsda//baidu.com', rule)
        # self.assertRaises(UrlError, self.v.set_rules, 'baidu.com', rule)

if __name__ == '__main__':
    unittest.main(verbosity=2)
