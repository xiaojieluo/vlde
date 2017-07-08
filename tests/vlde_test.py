import pytest

from vlde.error import *
from vlde.validate import Validator

v = Validator(warning_rule=True)

def test_required():
    '''
    rule 测试： required
    '''
    v.set_rules('string', 'required')
    v.set_rules(1024, 'required')
    v.set_rules(12.04, 'required')
    v.set_rules(bool(), 'required')
    v.set_rules(['luo', 'ff'], 'required')
    v.set_rules({'name': 'vlde'}, 'required')
    v.set_rules(('name', 'age'), 'required')

    with pytest.raises(ValidateError):
        v.set_rules('', 'required')
        v.set_rules([], 'required')
        v.set_rules({}, 'required')
        v.set_rules((), 'required')
        v.set_rules(int(), 'required')
        v.set_rules(float(), 'required')
        v.set_rules(bytes(), 'required')
        v.set_rules(None, 'required')
    with pytest.raises(RulesError):
        v.set_rules('string', 'requireds')


def test_min_length():
    '''
    rule test: min_length
    '''
    v.set_rules('string', 'min_length:6')
    v.set_rules('', 'min_length:0')
    v.set_rules(bool(), 'min_length:0')
    v.set_rules(None, 'min_length:0')
    with pytest.raises(ValidateError):
        v.set_rules(100, 'min_length:4')
        v.set_rules('', 'min_length:1')
        v.set_rules(bool(), 'min_length:1')
        v.set_rules([], 'min_length:1')
        v.set_rules({}, 'min_length:1')
        v.set_rules((), 'min_length:1')
        v.set_rules(None, 'min_length:10')
    with pytest.raises(RulesError):
        v.set_rules('string', 'min_length:-1')
        v.set_rules('string', 'min_length:abc')
        v.set_rules('string', 'min_length:')
        v.set_rules('string', 'min_length:3/4')


def test_max_length():
    '''
    rule test: max_lenght
    '''
    v.set_rules('string', 'max_length:6')
    v.set_rules('', 'max_length:0')
    v.set_rules(None, 'max_length:0')
    v.set_rules({'hello': 'world'}, 'max_length:1')

    with pytest.raises(ValidateError):
        v.set_rules('string', 'max_length:1')
        v.set_rules({'dict': 'world'}, 'max_length:0')
        v.set_rules(('tuple'), 'max_length:0')
        v.set_rules(['list'], 'max_length:0')
        v.set_rules(None, 'max_length:1')

    with pytest.raises(RulesError):
        v.set_rules('string', 'max_length:-1')
        v.set_rules('string', 'max_length:abc')
        v.set_rules('string', 'max_length:')
        v.set_rules('string', 'max_length:1 3/4')


def test_length():
    '''rule test length'''
    v.set_rules('string', 'length:6')
    v.set_rules('', 'length:0')
    v.set_rules(['list1'], 'length:1')
    v.set_rules({'dict': 'dict'}, 'length:1')
    v.set_rules(('hello', 'world'), 'length:2')
    v.set_rules(None, 'length:0')

    with pytest.raises(ValidateError):
        v.set_rules('string', 'length:0')
        v.set_rules(None, 'length:1')
    with pytest.raises(RulesError):
        v.set_rules('string', 'length:-1')
        v.set_rules('string', 'length:')
        v.set_rules('string', 'length:3/4')


def test_in_list():
    '''rule test length'''
    '''只支持字符串，整型，浮点型变量'''
    v.set_rules('hello', 'in_list:hello, world')
    v.set_rules(123, 'in_list:123, 321')
    v.set_rules(123.4, 'in_list:123.4')

    with pytest.raises(ValidateError):
        v.set_rules('str', 'in_list:string')
        v.set_rules('ss', 'in_list:hello, world')

    with pytest.raises(RulesError):
        v.set_rules({}, 'in_list:dict')
        v.set_rules([], 'in_list:list')
        v.set_rules((), 'in_list:tuple')
        v.set_rules(None, 'in_list:None')


def test_str():
    '''test str type'''
    v.set_rules('hello', 'str|string')
    v.set_rules('', 'str|string')
    v.set_rules(str(123), 'str|string')

    with pytest.raises(ValidateError):
        v.set_rules(123, 'str')
        v.set_rules([], 'str')
        v.set_rules({}, 'str')
        v.set_rules((), 'str')
        v.set_rules(None, 'str')
        v.set_rules(bool(), 'str')
        v.set_rules(float(), 'str')
        v.set_rules(bytes(), 'str')


def test_dict():
    '''test dict type'''
    v.set_rules({}, 'dict')
    v.set_rules(dict(), 'dict')
    with pytest.raises(ValidateError):
        v.set_rules('', 'dict')
        v.set_rules([], 'dict')
        v.set_rules((), 'dict')
        v.set_rules(int(), 'dict')
        v.set_rules(float(), 'dict')
        v.set_rules(bytes(), 'dict')
        v.set_rules(bool(), 'dict')
        v.set_rules(None, 'dict')


def test_list():
    '''test list type'''
    v.set_rules(list(), 'list')
    v.set_rules([], 'list')

    with pytest.raises(ValidateError):
        v.set_rules('', 'list')
        v.set_rules({}, 'list')
        v.set_rules((), 'list')
        v.set_rules(int(), 'list')
        v.set_rules(float(), 'list')
        v.set_rules(bytes(), 'list')
        v.set_rules(bool(), 'list')
        v.set_rules(None, 'list')


def test_bool():
    '''test bool type '''
    v.set_rules(bool(), 'bool')
    v.set_rules(True, 'bool')
    v.set_rules(False, 'bool')

    with pytest.raises(ValidateError):
        v.set_rules('', 'bool')
        v.set_rules({}, 'bool')
        v.set_rules((), 'bool')
        v.set_rules([], 'bool')
        v.set_rules(int(), 'bool')
        v.set_rules(float(), 'bool')
        v.set_rules(bytes(), 'bool')
        v.set_rules(None, 'bool')

def test_float():
    '''test float type '''
    v.set_rules(float(), 'float')
    v.set_rules(123.456, 'float')
    v.set_rules(123.00, 'float')
    with pytest.raises(ValidateError):
        v.set_rules('', 'float')
        v.set_rules({}, 'float')
        v.set_rules((), 'float')
        v.set_rules([], 'float')
        v.set_rules(int(), 'float')
        v.set_rules(bool(), 'float')
        v.set_rules(bytes(), 'float')
        v.set_rules(None, 'float')

def test_tuple():
    '''test tuple type '''
    v.set_rules((), 'tuple')
    v.set_rules((123,), 'tuple')
    with pytest.raises(ValidateError):
        v.set_rules('', 'tuple')
        v.set_rules({}, 'tuple')
        v.set_rules(float(), 'tuple')
        v.set_rules([], 'tuple')
        v.set_rules(int(), 'tuple')
        v.set_rules(bool(), 'tuple')
        v.set_rules(bytes(), 'tuple')
        v.set_rules(None, 'tuple')

def test_int():
    '''test int type'''
    v.set_rules(int(), 'int')
    v.set_rules(123, 'int')
    v.set_rules(0, 'int')
    with pytest.raises(ValidateError):
        v.set_rules('', 'int')
        v.set_rules({}, 'int')
        v.set_rules(float(), 'int')
        v.set_rules([], 'int')
        v.set_rules((), 'int')
        v.set_rules(bool(), 'int')
        v.set_rules(bytes(), 'int')
        v.set_rules(None, 'int')

def test_ipv4():
    '''test ipv4 rule'''
    v.set_rules('192.168.1.1', 'ipv4')
    v.set_rules('255.255.255.255', 'ipv4')
    v.set_rules('0.0.0.0', 'ipv4')
    with pytest.raises(ValidateError):
        v.set_rules('192.168.1111', 'ipv4')
        v.set_rules('-1-1-1-1', 'ipv4')
        v.set_rules(None, 'ipv4')

def test_ipv6():
    '''test ipv6 rule'''
    v.set_rules('0000:0000:0000:0000:0000:0000:0000:0000', 'ipv6')
    v.set_rules('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'ipv6')
    v.set_rules('0:0:0:0:0:0:0:0', 'ipv6')
    v.set_rules('f:f:f:f:f:f:f:f', 'ipv6')
    v.set_rules('::', 'ipv6')
    v.set_rules('a::a', 'ipv6')
    with pytest.raises(ValidateError):
        v.set_rules('ff', 'ipv6')
        v.set_rules('192.168.1.1', 'ipv6')

def test_url():
    '''test url rule'''
    v.set_rules('http://google.com', 'url')
    v.set_rules('https://www.google.com', 'url')
    v.set_rules('ftp://google.com', 'url')
    with pytest.raises(ValidateError):
        v.set_rules('baidu.com', 'url')
        v.set_rules('//baidu.com', 'url')
        v.set_rules('www.baidu.com', 'url')
        v.set_rules(None, 'url')

def test_range():
    '''test range rule'''
    v.set_rules(20, 'range:1-21')
    v.set_rules(20, 'range:20')
    v.set_rules(20.0, 'range:20.0-100.0')
    with pytest.raises(ValidateError):
        v.set_rules(0, 'range:10-100')
        v.set_rules(0, 'range:1')
        v.set_rules(None, 'range:0')
    with pytest.raises(RulesError):
        v.set_rules('20', 'range:20')
        v.set_rules(dict(), 'range:0')
        v.set_rules(20, 'range:a-z')
        v.set_rules('string', 'range:hello')


def test_function():
    '''用户自定义验证函数'''
    '''
    支持匿名函数
    '''

    def valid(key):
        if key == 'string':
            return True
        else:
            return False

    v.set_rules('string', callback=valid)
    v.set_rules('string', callback=lambda x: x == 'string')
    v.set_rules('string', callback=None)
    v.set_rules(['hello'], callback=lambda x: x == ['hello'])
    v.set_rules({'name': 'vlde'}, callback=lambda x: x == dict(name='vlde'))
    v.set_rules(('name', 'vlde'), callback=lambda x: x == ('name', 'vlde'))
    v.set_rules(123, callback=lambda x: x == 123)
    v.set_rules(123.4, callback=lambda x: x == 123.4)
    v.set_rules(True, callback=lambda x: x == True)
    v.set_rules(bytes(123), callback=lambda x: x == bytes(123))

    with pytest.raises(ValidateError):
        v.set_rules('string', callback=lambda x: x == 'key')
        v.set_rules(bytes(123), callback=lambda x: x == bytes(1234))

    with pytest.raises(RulesError):
        v.set_rules('string', callback='str', warning_rule=True)


def test_email():
    '''email rule validate'''
    v.set_rules('xiaojieluoff@gmail.com', 'email')
    v.set_rules('1234@163.com', 'email')

    with pytest.raises(ValidateError):
        v.set_rules('emailemail', 'email')


def test_set_rules():
    '''set_rules 參數測試'''
    v.set_rules(None)
    v.set_rules('string', rule=None)
    v.set_rules('string', schema='str')
    v.set_rules(dict(hello='world'), schema=dict())

def test_object():
    '''测试 object 类型的验证信息'''
    v = Validator(return_format='object')
    result1 = v.set_rules('string', 'str')
    assert result1.status is True
    result2 = v.set_rules('string', 'dict')
    assert result2.status is False

def test_schema_dict():
    v.set_rules(dict(name='llnhhy'), schema=dict(name='str'))
    v.set_rules(dict(name='llnhhy', age=17), schema=dict(name='str', age='int'))
    v.set_rules(dict(name='luo', girlfriend=dict(name='wu', age=20)), schema=dict(name='str', girlfriend=dict(name='str', age='int')))
    v.set_rules(dict(name='luo', girlfriend=dict(name='wu', age=20)), schema=dict(name='str', girlfriend='dict'))
    v.set_rules(dict(name='luo', girlfriend=['wu', 'sun', 'li']), schema=dict(name='str', girlfriend=['str', 'str', 'max_length:2']))
    v.set_rules({'name':'luo', 'age':20}, schema={'name':'str', 'age':'int'})
    v.set_rules({'name':'luo', 'age':20}, schema={'name':'str'})
    v.set_rules({'name':'luo', 'age':20}, schema={'name':'str', 'age':'int|min_length:2'})
    v.set_rules({'name':'luo', 'age':20}, rule='dict|max_length:2', schema={'name':'str', 'age':'int'})

def test_schema_list():
    v.set_rules([10, 20, 'string'], schema=['int', 'int', 'str'])
    v.set_rules([20, 30, ['hello']], schema=['int', 'int', ['str']])
    # self.v.set_rules([10, 'string', [20, 'hello']], schema=['int', 'str', ['int', 'str']
def test_schema_tuple():
    pass

#
# class TestValidate(unittest.TestCase):
#
#     def setUp(self):
#         self.v = Validator(warning_rule=True)
#
#     def test_required(self):
#         '''
#         test required
#         not None and not ''
#         '''
#         self.v.set_rules('hello world', 'required')
#         self.v.set_rules(dict(name='python'), 'required')
#         self.v.set_rules(int(), 'required')
#         self.v.set_rules(bool(), 'required')
#         self.v.set_rules(float(), 'required')
#         self.v.set_rules(-1, 'required')
#         self.v.set_rules((1, 2, 3), 'required')
#         self.v.set_rules(object, 'required')
#
#         self.assertRaises(RequiredError, self.v.set_rules, tuple(), 'required')
#         self.assertRaises(RequiredError, self.v.set_rules, dict(), 'required')
#         self.assertRaises(RequiredError, self.v.set_rules, list(), 'required')
#         self.assertRaises(RequiredError, self.v.set_rules, str(), 'required')
#         self.assertRaises(RequiredError, self.v.set_rules, '', 'required')
#         self.assertRaises(RequiredError, self.v.set_rules, 'hello'[:0], 'required')
#         self.assertRaises(RequiredError, self.v.set_rules, None, 'required')
#
#     def test_schema_dict(self):
#         self.v.set_rules(dict(name='llnhhy'), schema=dict(name='str'))
#         self.v.set_rules(dict(name='llnhhy', age=17), schema=dict(name='str', age='int'))
#         self.v.set_rules(dict(name='luo', girlfriend=dict(name='wu', age=20)), schema=dict(name='str', girlfriend=dict(name='str', age='int')))
#         self.v.set_rules(dict(name='luo', girlfriend=dict(name='wu', age=20)), schema=dict(name='str', girlfriend='dict'))
#         self.v.set_rules(dict(name='luo', girlfriend=['wu', 'sun', 'li']), schema=dict(name='str', girlfriend=['str', 'str', 'max_length:2']))
#         self.v.set_rules({'name':'luo', 'age':20}, schema={'name':'str', 'age':'int'})
#         self.v.set_rules({'name':'luo', 'age':20}, schema={'name':'str'})
#         self.v.set_rules({'name':'luo', 'age':20}, schema={'name':'str', 'age':'int|min_length:2'})
#         self.v.set_rules({'name':'luo', 'age':20}, schema='dict|max_length:2')
#
#     def test_schema_list(self):
#         self.v.set_rules([10, 20, 'string'], schema=['int', 'int', 'str'])
#         self.v.set_rules([20, 30, ['hello']], schema=['int', 'int', ['str']])
#         # self.v.set_rules([10, 'string', [20, 'hello']], schema=['int', 'str', ['int', 'str']
#     def test_schema_tuple(self):
#         pass
#
#     def test_range(self):
#         self.v.set_rules(10, 'range:10')
#         self.v.set_rules(10, 'range:1-10')
#
#         warning_rule=False
#         self.assertRaises(RangeError, self.v.set_rules, 10, 'range:abc', warning_rule=warning_rule)
#         self.assertRaises(RulesError, self.v.set_rules, 'str', 'range:1-10', warning_rule=True)
#         self.assertRaises(RulesError, self.v.set_rules, '10', 'range:1-10', warning_rule=True)
#         self.assertRaises(RulesError, self.v.set_rules, list(), 'range:1-10', warning_rule=True)
#         self.assertRaises(RulesError, self.v.set_rules, str(), 'range:1-10', warning_rule=True)
#         self.assertRaises(RulesError, self.v.set_rules, dict(), 'range:1-10', warning_rule=True)
#         self.assertRaises(RulesError, self.v.set_rules, tuple(), 'range:1-10', warning_rule=True)
#         self.assertRaises(RulesError, self.v.set_rules, True, 'range:1-10', warning_rule=True)
#         self.assertRaises(RulesError, self.v.set_rules, None, 'range:1-10', warning_rule=True)
#
#     def test_length(self):
#         rule = 'length:{}'
#
#         self.v.set_rules('hello', 'length:5')
#         self.v.set_rules(123, 'length:3')
#         self.v.set_rules(dict(name='luo'), 'length:1')
#         self.v.set_rules({'name':'luo', 'age':18}, 'length:2')
#         self.v.set_rules({'name':'luo', 'girlfriend':[]}, 'length:2')
#         self.v.set_rules(['1', '2'], 'length:2')
#         self.v.set_rules([1, 2], 'length:2')
#         self.v.set_rules([1, [2, 3], 4], 'length:3')
#         self.v.set_rules((1, 2, 3), 'length:3')
#         self.v.set_rules(123.123, 'length:7')
#
#         self.assertRaises(Exact_lengthError, self.v.set_rules, None, 'length:2')
#
#
#     def test_max_length(self):
#         '''
#         test max_length
#         '''
#         string = 'hello world'
#         self.assertRaises(Max_lengthError, self.v.set_rules, string, 'max_length:2')
#         self.v.set_rules(string, 'max_length:20')
#         self.v.set_rules(string, 'max_length:a')
#
#     def test_min_length(self):
#         string = 'hello world'
#         self.v.set_rules(string, 'min_length:1')
#         self.v.set_rules(string, 'min_length:a')
#         self.assertRaises(Min_lengthError, self.v.set_rules, 'helo world', 'min_length:100')
#         self.assertRaises(Min_lengthError, self.v.set_rules, '', 'min_length:1')
#
#
#
#     def test_in_list(self):
#         '''
#         in list test
#         '''
#         self.v.set_rules('hello', 'in_list[hello, hellos]')
#         self.v.set_rules('hello', 'in_listp[hello ]')
#         self.v.set_rules('hello', 'in_list[hello,]')
#         self.v.set_rules('hello world', 'in_list[hello world, hello]')
#         self.v.set_rules('hello "world"', 'in_list[hello "world"]')
#         self.assertRaises(In_listError, self.v.set_rules, 'hello', 'in_list:h')
#         self.assertRaises(ValidateError, self.v.set_rules, 'hello', 'in_list:hell0')
#
#     def test_str(self):
#         '''
#         test variable type
#         '''
#         self.v.set_rules('hello', 'str')
#         self.v.set_rules('h', 'str')
#         self.v.set_rules(str(float()), 'str')
#         self.v.set_rules(str(bool()), 'str')
#
#         self.assertRaises(GenreError, self.v.set_rules, 10, 'str')
#         self.assertRaises(GenreError, self.v.set_rules, float(), 'str')
#         self.assertRaises(GenreError, self.v.set_rules, bool(), 'str')
#         self.assertRaises(GenreError, self.v.set_rules, dict(name='hello'), 'str')
#         self.assertRaises(GenreError, self.v.set_rules, list('hello'), 'str')
#         self.assertRaises(GenreError, self.v.set_rules, None, 'str')
#
#     def test_dict(self):
#         '''
#         test attribute type of dict
#         '''
#         rule = 'dict'
#         self.v.set_rules(dict(), rule)
#         self.v.set_rules(dict(hello='hello'), rule)
#         self.v.set_rules({'hello':'world'}, rule)
#
#         self.assertRaises(GenreError, self.v.set_rules, 'dict', rule)
#         self.assertRaises(GenreError, self.v.set_rules, list(), rule)
#         self.assertRaises(GenreError, self.v.set_rules, tuple(dict()), rule)
#
#
#     def test_ipv4(self):
#         self.v.set_rules('192.168.1.1', 'ipv4')
#         self.v.set_rules('0.0.0.0', 'ipv4')
#
#         self.assertRaises(Ipv4Error, self.v.set_rules, '888.888.888.888', 'ipv4')
#         self.assertRaises(Ipv4Error, self.v.set_rules, 'hello', 'ipv4')
#         self.assertRaises(Ipv4Error, self.v.set_rules, 192, 'ipv4')
#         self.assertRaises(Ipv4Error, self.v.set_rules, dict(), 'ipv4')
#         self.assertRaises(Ipv4Error, self.v.set_rules, list("192.168.1.1"), 'ipv4')
#         self.assertRaises(Ipv4Error, self.v.set_rules, bool(), 'ipv4')
#         self.assertRaises(Ipv4Error, self.v.set_rules, tuple("192,168,1,1"), 'ipv4')
#         self.assertRaises(Ipv4Error, self.v.set_rules, str('1920.168.1.1'), 'ipv4')
#         self.assertRaises(Ipv4Error, self.v.set_rules, [192, 168, 1, 1], 'ipv4')
#
#     def test_ipv6(self):
#         rule = 'ipv6'
#
#         self.v.set_rules('5e:0:0:0:0:0:5668:eeee', rule)
#         self.v.set_rules('5e:0:0:023:0:0:5668:eeee', rule)
#         self.v.set_rules('5e::5668:eeee', rule)
#         self.v.set_rules('::1:8:8888:0:0:8', rule)
#         self.v.set_rules('1::', rule)
#         self.v.set_rules('::1:2:2:2', rule)
#         self.v.set_rules('::', rule)
#
#         self.assertRaises(Ipv6Error, self.v.set_rules, '192.168.1.1', rule)
#         self.assertRaises(Ipv6Error, self.v.set_rules, '55555:5e:0:0:0:0:0:5668:eeee', rule)
#
#     def test_email(self):
#         rule = 'email'
#
#         self.v.set_rules('baidu@baidu.com', rule)
#         self.v.set_rules('cadwqd233@cascsan.com', rule)
#         self.assertRaises(EmailError, self.v.set_rules, '1234@@gs.com', rule)
#         self.assertRaises(EmailError, self.v.set_rules, '123@gmail', rule)
#         self.assertRaises(EmailError, self.v.set_rules, '123@gmail\.com', rule)
#         self.assertRaises(EmailError, self.v.set_rules, list('123@gmail'), rule)
#
#     def test_url(self):
#         rule = 'url'
#
#         self.v.url('ftp://www.baidu.com')
#         self.v.set_rules('http://baidu.com', rule)
#         self.v.set_rules('https://baidu.com', rule)
#         self.v.set_rules('ftp://www.baidu.com', rule)
#
#         # self.assertRaises(UrlError, self.v.set_rules, 'hsda//baidu.com', rule)
#         # self.assertRaises(UrlError, self.v.set_rules, 'baidu.com', rule)
#
#     def callback(self, key):
#         print(key)
#         if key == 'name':
#             return True
#
#     def test_callback(self):
#         self.v.set_rules('name', callback=self.callback)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)
