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
import re
from vlde.error import *


class Status(object):

    def __init__(self):
        self.error = list()
        self.status = bool(True)


class Validator(object):
    '''
    数据完整性验证
    '''

    def __init__(self, **kw):
        self.compile_re()
        self.status = Status()
        # 解析变量
        self.return_format = 'exception'
        self.language = 'en'
        self.warning_rule = True
        self.parse_args(kw)

    def compile_re(self):
        '''编译正则表达式'''
        self.re_required = re.compile(r'^required$')
        self.re_min_length = re.compile(r'^min_length\:(\d+)$')
        self.re_max_length = re.compile(r'^max_length\:(\d+)$')
        self.re_length = re.compile(r'length\:(\d+)$')
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
        self.re_range = re.compile(r'^range\:(.*)$')

    def parse_args(self, kw):
        '''
        解析参数
        '''
        self.return_format = kw.get('return_format', self.return_format)
        # 是否开启规则验证， 当传入的参数或者规则名有错误时，抛出异常
        self.warning_rule = kw.get('warning_rule', self.warning_rule)
        self.lang = kw.get('language', self.language)

    def set_rules(self, key, rules=None, schema=None, callback=None, **kw):
        '''
        设置验证规则
        callback 用户验证函数
        '''
        self.parse_args(kw)

        if schema is not None:
            self.schema(key, schema)
        if rules is not None:
            self.parse_rules(key, rules)
        if callback is not None:
            self.function(callback, key)

        return self.status

    def parse_rules(self, name, rules):
        '''
        解析并验证规则
        '''
        if isinstance(rules, str):
            for rule in rules.split('|'):
                self.validate(name, rule)
        elif isinstance(rules, list):
            # TODO
            # list
            print(rules)

    def schema(self, name, schema):
        '''
        schema
        '''
        if isinstance(schema, dict):
            for k in schema:
                self.schema(name[k], schema[k])
        elif isinstance(schema, (list, tuple)):
            for index, k in enumerate(schema):
                self.schema(name[index], k)
        elif isinstance(schema, str):
            self.parse_rules(name, schema)

    def validate(self, name, rule):
        '''
        验证
        '''
        if self.re_required.search(rule):
            self.required(name)
        elif self.re_min_length.search(rule):
            self.min_length(
                name, int(
                    self.re_min_length.search(rule).group(1)))
        elif self.re_max_length.search(rule):
            self.max_length(
                name, int(
                    self.re_max_length.search(rule).group(1)))
        elif self.re_length.search(rule):
            self.length(name, int(self.re_length.search(rule).group(1)))
        elif self.re_in_list.search(rule):
            self.in_list(name, self.re_in_list.search(rule).group(1))
        elif self.re_str.search(rule):
            self.vali_type(name, str)
        elif self.re_dict.search(rule):
            self.vali_type(name, dict)
        elif self.re_list.search(rule):
            self.vali_type(name, list)
        elif self.re_bool.search(rule):
            self.vali_type(name, bool)
        elif self.re_float.search(rule):
            self.vali_type(name, float)
        elif self.re_tuple.search(rule):
            self.vali_type(name, tuple)
        elif self.re_int.search(rule):
            self.vali_type(name, int)
        elif self.re_ipv4.search(rule):
            self.ipv4(name)
        elif self.re_ipv6.search(rule):
            self.ipv6(name)
        elif self.re_email.search(rule):
            self.email(name)
        elif self.re_url.search(rule):
            self.url(name)
        elif self.re_range.search(rule):
            self.range_(name, self.re_range.search(rule).group(1))
        else:
            self._error(RulesError, '不支持的验证方式：{}'.format(rule))

    def function(self, func, *args, **kw):
        '''
        使用用户自定义的函数进行数据验证
        '''
        if not callable(func):
            self._error(RulesError, 'callback 不支持非函数参数:{}'.format(func))
        # try:
        if func(*args, **kw) is False:
            self._error(
                CallbackError,
                'Function validation failed：{}'.format(
                    func.__name__))
        # except TypeError:
        #     pass

    def range_(self, key, num):
        '''
        限定变量值的数值范围，
        支持 int, float 类型的变量
        当传入一个参数时， 限定为固定值
        当传入两个参数时， 分别为上差和下差
        '''
        num = num.split('-')

        # 排除 bool， 因为在 python 中， isinstance(True, int) == True..
        if isinstance(key, (int, float)) and not isinstance(key, bool):
            try:
                num = sorted(list(map(type(key), num)))
            except ValueError:
                self._error(RulesError, 'range 参数类型不正确')
            if len(num) == 2:
                if key < num[0] or key > num[1]:
                    self._error(RangeError, '{} Not in scope {}'.format(
                        key, '-'.join(list(map(str, num)))))
            elif len(num) == 1:
                if key != num[0]:
                    self._error(
                        RangeError, '{} Not in scope {}'.format(
                            key, num[0]))
        else:
            self._error(RulesError, 'range 不支持非 int, float 类型的变量')

    def required(self, name):
        '''
        如果 name 变量为空或者为 None，抛出 RequiredError 异常
        '''
        if isinstance(name, type(None)):
            self._error(
                RequiredError,
                'The attribute {} is empty'.format(name))
        elif isinstance(name, (bool, int, float)):
            pass
        elif isinstance(name, (str, tuple, list, dict, bytes)):
            if len(name) == 0:
                self._error(RequiredError, 'The attribute is empty')
        else:
            self._error(RulesError, '不支持的 required 类型：{}'.format(name))

    def url(self, key):
        '''
        url rule
        '''
        url = re.compile(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')
        if url.search(str(key)) is None:
            self._error(UrlError, 'Url format is incorrect')

    def email(self, key):
        '''
        email rule
        '''
        email = re.compile(
            r'^[\w!#$%&\'*+/=?^_`{|}~-]+(?:\.[\w!#$%&\'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?$')
        if email.search(str(key)) is None:
            self._error(EmailError, 'email format is incorrect')

    def ipv4(self, key):
        '''
        ip4 rule
        '''
        ipv4 = re.compile(
            r'^(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))$')
        if ipv4.search(str(key)) is None:
            self._error(Ipv4Error, 'Ipv4 address is not standardized')

    def ipv6(self, key):
        '''
        ipv6 rule
        '''
        ipv6 = re.compile(r'^([\da-fA-F]{1,4}:){6}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|::([\da−fA−F]1,4:)0,4((25[0−5]|2[0−4]\d|[01]?\d\d?)\.)3(25[0−5]|2[0−4]\d|[01]?\d\d?)|::([\da−fA−F]1,4:)0,4((25[0−5]|2[0−4]\d|[01]?\d\d?)\.)3(25[0−5]|2[0−4]\d|[01]?\d\d?)|^([\da-fA-F]{1,4}:):([\da-fA-F]{1,4}:){0,3}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da−fA−F]1,4:)2:([\da−fA−F]1,4:)0,2((25[0−5]|2[0−4]\d|[01]?\d\d?)\.)3(25[0−5]|2[0−4]\d|[01]?\d\d?)|([\da−fA−F]1,4:)2:([\da−fA−F]1,4:)0,2((25[0−5]|2[0−4]\d|[01]?\d\d?)\.)3(25[0−5]|2[0−4]\d|[01]?\d\d?)|^([\da-fA-F]{1,4}:){3}:([\da-fA-F]{1,4}:){0,1}((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)|([\da−fA−F]1,4:)4:((25[0−5]|2[0−4]\d|[01]?\d\d?)\.)3(25[0−5]|2[0−4]\d|[01]?\d\d?)|([\da−fA−F]1,4:)4:((25[0−5]|2[0−4]\d|[01]?\d\d?)\.)3(25[0−5]|2[0−4]\d|[01]?\d\d?)|^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}|:((:[\da−fA−F]1,4)1,6|:)|:((:[\da−fA−F]1,4)1,6|:)|^[\da-fA-F]{1,4}:((:[\da-fA-F]{1,4}){1,5}|:)|([\da−fA−F]1,4:)2((:[\da−fA−F]1,4)1,4|:)|([\da−fA−F]1,4:)2((:[\da−fA−F]1,4)1,4|:)|^([\da-fA-F]{1,4}:){3}((:[\da-fA-F]{1,4}){1,3}|:)|([\da−fA−F]1,4:)4((:[\da−fA−F]1,4)1,2|:)|([\da−fA−F]1,4:)4((:[\da−fA−F]1,4)1,2|:)|^([\da-fA-F]{1,4}:){5}:([\da-fA-F]{1,4})?|([\da−fA−F]1,4:)6:')
        if ipv6.search(str(key)) is None:
            self._error(Ipv6Error, 'Ipv6 address is not standardized')

    def vali_type(self, name, types):
        '''
        变量类型验证
        '''
        if isinstance(name, bool) and types == int:
            # 由于在 python 中， isinstance(bool(), int) 为 True,
            # 所以在这里要先排除掉 bool 类型
            self._error(GenreError, '{} is not {}'.format(name, types))
        elif isinstance(name, types):
            pass
        else:
            self._error(GenreError, '{} is not {}'.format(name, types))

    def in_list(self, key, lists):
        '''
        验证变量值是否在指定列表中
        '''
        if not isinstance(key, (str, int, float)):
            self._error(
                RulesError,
                'in_list 只支持整型，浮点型，字符型变量，不支持 {}:{}'.format(
                    key,
                    type(key)))
        else:
            s = list()
            for k in lists.split(','):
                try:
                    k = type(key)(k)
                except BaseException:
                    k = k.strip()
                s.append(k)

            if key not in s:
                self._error(
                    InListError,
                    'The variable {} is not in the specified list'.format(key))

    def length(self, key, num):
        '''
        指定变量值的长度长度
        如果变量 name 值的长度不等于 num，抛出 LengthError
        '''
        if isinstance(key, (str, list, dict, tuple)):
            if len(key) != num:
                self._error(
                    LengthError,
                    'The length of the variable {} is not equal to num:{}'.format(
                        key,
                        num))
        elif isinstance(key, (int, float)):
            if len(str(key)) != num:
                self._error(
                    LengthError,
                    'The length of the variable {} is not equal to num:{}'.format(
                        key,
                        num))
        elif isinstance(key, type(None)):
            if num != 0:
                self._error(
                    LengthError,
                    'The length of the variable {} is not equal to num:{}'.format(
                        key,
                        num))
        else:
            self._error(
                RulesError,
                'length 只支持 str, list, dict, tuple, int, float 类型的变量')

    def max_length(self, name, num):
        '''
        最大长度
        '''
        if isinstance(name, (str, list, dict, tuple)):
            if len(name) > num:
                self._error(
                    MaxLengthError,
                    'The length of the variable {} is higher the max:{}'.format(
                        name,
                        num))
        elif isinstance(name, (int, float)):
            if len(str(name)) > num:
                self._error(
                    MaxLengthError,
                    'The length of the variable {} is higher the max:{}'.format(
                        name,
                        num))
        elif name is None:
            if num != 0:
                self._error(
                    MaxLengthError,
                    'the length of the variable {} is velow the minimum：{}'.format(
                        name,
                        num))

        else:
            self._error(
                RulesError,
                'max_length 只支持 str, list, dict, tuple, int, float 类型的变量')

    def min_length(self, name, num):
        '''
        最小长度
        '''
        if isinstance(name, (str, list, dict, tuple)):
            if len(name) < num:
                self._error(
                    MinLengthError,
                    'The length of the variable {} is below the minimum:{}'.format(
                        name,
                        num))
        elif isinstance(name, (int, float)) and not isinstance(name, bool):
            if len(str(name)) < num:
                self._error(
                    MinLengthError,
                    'The length of the variable {} is below the minimum:{}'.format(
                        name,
                        num))
        elif name is None:
            if num != 0:
                self._error(
                    MinLengthError,
                    'the length of the variable {} is below the minimum：{}'.format(
                        name,
                        num))
        else:
            self._error(
                RulesError,
                'min_length 只支持 str, list, dict, tuple, int, float 类型的变量')

    def _error(self, exc, message):
        '''
        有两种返回验证结果的方法
        一种是返回对象， 使用 if... else 来判断验证结果
        .. testcode::

            from validate.validate  import Validator

            v = Validator(return_format='object')

            result = v.set_rules('hello', 'required|dict')

            if result.status is False:
                print('\n'.join(result.error))

        .. testoutput::
           :hide:

        另一种是抛出异常，使用 try... exception 捕获异常来处理

        .. testcode::

            from validate.validate  import Validator

            v = Validator()
            try:
                v.set_rules('hello', 'required|dict')
            exception ValidateError as e:
                print(e)

        .. testoutput::
           :hide:

        '''
        if self.return_format == 'object':
            self.status.error.append(message)
            self.status.status = False
        else:
            if exc.__name__ == RulesError.__name__:
                if self.warning_rule:
                    raise RulesError(message)
            else:
                raise exc(message)
