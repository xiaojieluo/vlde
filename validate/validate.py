'''
import validate as v
# 预处理数据
去除两边空白：只对字符串有效，若传入的是列表，则去除列表中所有元素的两边空白
required ： 非空， 非None
min_length[num] : 限定变量长度最小值， 如果是列表或者字典，限定最少元素

v.set_rules('username', 'required')
v.set_rules('password', 'required|min_length[3]|max_length[20]|callback_check_password['hello']')
v.set_rules('passconf', 'required|matches[password]')

or
v.set_rules('password', list('required', 'min_length[3]', 'max_length[20]'))
'''
# TODO
# range 数值类型的变量值类型 range:10-20
import re

try:
    from validate.error import *
except:
    from error import *

class Validator(object):
    '''
    数据完整性验证
    '''
    def __init__(self):
        self.compile_re()

    def compile_re(self):
        '''
        编译正则表达式
        '''
        self.re_required = re.compile(r'^required$')
        self.re_min_length = re.compile(r'^min_length\:(\d+)$')
        self.re_max_length = re.compile(r'^max_length\:(\d+)$')
        self.re_exact_length = re.compile(r'^exact_length\:(\d+)$')
        self.re_in_list = re.compile(r'^in_list:(.*)$')
        self.re_str = re.compile(r'^(str|string)$')
        self.re_dict = re.compile(r'^dict$')
        self.re_list = re.compile(r'^list$')
        self.re_bool = re.compile(r'^bool$')
        self.re_int = re.compile(r'^(int|integer)$')
        self.re_float = re.compile(r'^float$')
        self.re_tuple = re.compile(r'^(tuple|tup)$')
        self.re_ipv4 = re.compile(r'^ipv4$')
        self.re_ipv6 = re.compile(r'^ipv6$')
        self.re_email = re.compile(r'^email$')
        self.re_url = re.compile(r'^url$')


    def set_rules(self, name, rules=None, schema=None):
        '''
        设置验证规则
        '''
        # if schema is not None and isinstance(schema, type(name)):
        if schema is not None:
            self.schema(name, schema)

        if rules is not None:
            self.parse_rules(name, rules)


    def parse_rules(self, name, rules):
        '''
        解析并验证规则
        '''
        for rule in rules.split('|'):
            self.validate(name, rule)

    def schema(self, name, schema):
        '''
        schema
        '''
        if isinstance(schema, dict):
            self.schema_dict(name, schema)
        elif isinstance(schema, list):
            self.schema_list(name, schema)
        elif isinstance(schema, str):
            self.parse_rules(name, schema)

    def schema_list(self, name, schema):
        '''
        schema list
        '''
        pass
        # for index, k in enumerate(schema):
        #     try:
        #         self.validate(name[index], k)
        #     except IndexError:
        #         pass

    def schema_dict(self, name, schema):
        '''
        schema_dict
        '''

        for k in schema:
            # if isinstance(schema[k], str):
            #     self.validate(name[k], schema[k])
            # else:
            self.schema(name[k], schema[k])

    def validate_schema(self, key):
        '''
        验证 Schema 规则
        '''
        pass

    def validate(self, name, rule):
        '''
        验证
        '''
        if self.re_required.search(rule):
            self.required(name)
        if self.re_min_length.search(rule):
            self.min_length(name, int(self.re_min_length.search(rule).group(1)))
        if self.re_max_length.search(rule):
            self.max_length(name, int(self.re_max_length.search(rule).group(1)))
        if self.re_exact_length.search(rule):
            self.exact_length(name, int(self.re_exact_length.search(rule).group(1)))
        if self.re_in_list.search(rule):
            self.in_list(name, self.re_in_list.search(rule).group(1))
        # if self.re_str.search(rule):
        #     self.vali_type(name, eval(rule))
        # if self.re_dict.search(rule) or self.re_str.search(rule) or self.re_list.search(rule) or self.re_bool.search(rule) or self.re_float.search(rule) or self.re_tuple.search(rule) or self.re_int.search(rule):
        #     self.vali_type(name, eval(rule))
        if self.re_str.search(rule):
            self.vali_type(name, str)
        if self.re_dict.search(rule):
            self.vali_type(name, dict)
        if self.re_list.search(rule):
            self.vali_type(name, list)
        if self.re_bool.search(rule):
            self.vali_type(name, bool)
        if self.re_float.search(rule):
            self.vali_type(name, float)
        if self.re_tuple.search(rule):
            self.vali_type(name, tuple)
        if self.re_int.search(rule):
            self.vali_type(name, int)
        if self.re_ipv4.search(rule):
            self.ipv4(name)
        if self.re_ipv6.search(rule):
            self.ipv6(name)
        if self.re_email.search(rule):
            self.email(name)
        if self.re_url.search(rule):
            self.url(name)

    def required(self, name):
        '''
        如果 name 变量为空或者为 None，抛出 RequiredError 异常
        '''
        try:
            if name is None or len(name) == 0:
                raise RequiredError('The variable is empty')
        except TypeError :
            pass

    def url(self, key):
        '''
        url rule
        '''
        url = re.compile(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')
        if url.search(str(key)) is None:
            raise UrlError('Url format is incorrect')

    def email(self, key):
        '''
        email rule
        '''
        email = re.compile(r'^[\w!#$%&\'*+/=?^_`{|}~-]+(?:\.[\w!#$%&\'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?$')
        if email.search(str(key)) is None:
            raise EmailError('email format is incorrect')

    def ip(self, key):
        '''
        ip rule
        contains ipv4 and ipv6
        '''
        # TODO
        pass

    def ipv4(self, key):
        '''
        ip4 rule
        '''
        ipv4 = re.compile(r'^(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))$')
        if ipv4.search(str(key)) is None:
            raise Ipv4Error('Ipv4 address is not standardized')

    def ipv6(self, key):
        '''
        ipv6 rule
        '''
        ipv6 = re.compile(r'^([\da-fA-F]{1,4}:){6}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|::([\da−fA−F]1,4:)0,4((25[0−5]|2[0−4]\d|[01]?\d\d?)\.)3(25[0−5]|2[0−4]\d|[01]?\d\d?)|::([\da−fA−F]1,4:)0,4((25[0−5]|2[0−4]\d|[01]?\d\d?)\.)3(25[0−5]|2[0−4]\d|[01]?\d\d?)|^([\da-fA-F]{1,4}:):([\da-fA-F]{1,4}:){0,3}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da−fA−F]1,4:)2:([\da−fA−F]1,4:)0,2((25[0−5]|2[0−4]\d|[01]?\d\d?)\.)3(25[0−5]|2[0−4]\d|[01]?\d\d?)|([\da−fA−F]1,4:)2:([\da−fA−F]1,4:)0,2((25[0−5]|2[0−4]\d|[01]?\d\d?)\.)3(25[0−5]|2[0−4]\d|[01]?\d\d?)|^([\da-fA-F]{1,4}:){3}:([\da-fA-F]{1,4}:){0,1}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da−fA−F]1,4:)4:((25[0−5]|2[0−4]\d|[01]?\d\d?)\.)3(25[0−5]|2[0−4]\d|[01]?\d\d?)|([\da−fA−F]1,4:)4:((25[0−5]|2[0−4]\d|[01]?\d\d?)\.)3(25[0−5]|2[0−4]\d|[01]?\d\d?)|^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}|:((:[\da−fA−F]1,4)1,6|:)|:((:[\da−fA−F]1,4)1,6|:)|^[\da-fA-F]{1,4}:((:[\da-fA-F]{1,4}){1,5}|:)|([\da−fA−F]1,4:)2((:[\da−fA−F]1,4)1,4|:)|([\da−fA−F]1,4:)2((:[\da−fA−F]1,4)1,4|:)|^([\da-fA-F]{1,4}:){3}((:[\da-fA-F]{1,4}){1,3}|:)|([\da−fA−F]1,4:)4((:[\da−fA−F]1,4)1,2|:)|([\da−fA−F]1,4:)4((:[\da−fA−F]1,4)1,2|:)|^([\da-fA-F]{1,4}:){5}:([\da-fA-F]{1,4})?|([\da−fA−F]1,4:)6:')
        if ipv6.search(str(key)) is None:
            raise Ipv6Error('Ipv6 address is not standardized')

    def vali_type(self, name, types):
        '''
        str rule
        '''
        if isinstance(name, types):
            pass
        else:
            raise GenreError('{} is not {}'.format(name, types))

    def in_list(self, name, lists):
        '''
        验证变量值是否在指定列表中
        '''
        s = list()
        for k in lists.split(','):
            try:
                k = int(k)
            except:
                k = k.strip()
            s.append(k)

        if name not in s:
            raise In_listError('The variable value is not in the specified list')

    def exact_length(self, key, num):
        '''
        指定变量值的长度长度
        如果变量 name 值的长度不等于 num，抛出 Exact_lengthError
        '''
        if isinstance(key, (str, list, dict, tuple)):
            if len(key) != num:
                raise Exact_lengthError('The length of the variable {} is not equal to num:{}'.format(key, num))
        elif isinstance(key, (int, float)):
            if len(str(key)) != num:
                raise Exact_lengthError('The length of the variable {} is not equal to num:{}'.format(key, num))


    def max_length(self, name, num):
        '''
        最大长度
        '''
        if isinstance(name, (str, list, dict, tuple)):
            if len(name) > num:
                raise Max_lengthError('The length of the variable {} is higher the max:{}'.format(name, num))
        elif isinstance(name, (int,float)):
            if len(str(name)) > num:
                raise Max_lengthError('The length of the variable {} is higher the max:{}'.format(name, num))
        else:
            pass

    def min_length(self, name, num):
        '''
        最小长度
        '''
        if isinstance(name, (str, list, dict, tuple)):
            if len(name) < num:
                raise Min_lengthError('The length of the variable {} is below the minimum:{}'.format(name, num))
        elif isinstance(name, (int, float)):
            if len(str(name)) < num:
                raise Min_lengthError('The length of the variable {} is below the minimum:{}'.format(name, num))

if __name__ == '__main__':
    v = Validator()
    # name = 'xiaojieluo'
    name = '192.168.1.1'
    # name = dict(name='xiaojieluo')
    # name = ''
    # v.set_rules(name, 'required|min_length:3|max_length:20|str|ip4')
    # v.set_rules(10, 'str')
    # v.set_rules(dict(name=176), schema=dict(name='int'))
    # v.set_rules([10, 20, 'hello'], schema=['int', 'int', 'str'])
    # v.set_rules(dict(name='wu', girlfriend=dict(name='luo', age=20)), schema=dict(name='str', girlfriend='dict'))
    v.set_rules({'name':'luo', 'age':20}, schema='max_length:2')
    v.set_rules({'name':'luo', 'age':20}, 'exact_length:2')

    # name_rules = ['required', 'min_length[3]']
    # v.set_rules(name, name_rules)
    # v.set_rules(name, ['required', 'min_length[3]', 'max_length[20]'])
    # print(name)
    # try:
    #     v.set_rules(name, 'required|min_length[3]')
    # except ValidateError as e:
    #     print(e)
