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
from error import *

class Validate(object):
    '''
    数据完整性验证
    '''
    def __init__(self):
        # self.message = list()
        self.init_re()
        pass

    def init_re(self):
        '''
        编译正则表达式
        '''
        self.re_required = re.compile(r'^required$')
        # self.re_min_length = re.compile(r'^min_length\[(\d+)\]$')
        self.re_min_length = re.compile(r'^min_length\:(\d+)$')
        self.re_max_length = re.compile(r'^max_length\:(\d+)$')
        self.re_exact_length = re.compile(r'^exact_length\[(\d+)\]$')
        self.re_in_list = re.compile(r'^in_list\[(.*)\]$')
        self.re_matches = re.compile(r'^matches\[(.*)\]$')

    def required(self, name):
        '''
        如果 name 变量为空或者为 None，抛出 RequiredError 异常
        '''
        if name is None or len(name) == 0:
            raise RequiredError('The variable is empty')

    def set_rules(self, name, rules, **kw):
        '''
        设置验证规则
        '''
        # print(kw)
        # if isinstance(type(name), kw['type']):
        #     print("Y")
        # return
        for rule in rules.split('|'):
            self.validate(name, rule)

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

    def error(self):
        '''
        显示错误信息
        '''
        pass
        # print(self.message)

    def in_list(self, name, lists):
        s = list()
        for k in lists.split(','):
            try:
                k = int(k)
            except:
                k = k.strip()
            s.append(k)

        if name not in s:
            raise In_listError('The variable value is not in the specified list')

    def exact_length(self, name, num):
        '''
        如果变量 name 的长度不等于 num，抛出 Exact_lengthError
        '''
        if len(name) != num:
            raise Exact_lengthError('The length of the variable {} is not equal to num:{}'.format(name, num))

    def max_length(self, name, num):
        '''
        最大长度
        '''
        if len(name) > num:
            raise Max_lengthError('The length of the variable {} is higher the max:{}'.format(name, num))

    def min_length(self, name, num):
        '''
        最小长度
        '''
        if len(name) < num:
            raise Min_lengthError('The length of the variable {} is below the minimum:{}'.format(name, num))

if __name__ == '__main__':
    v = Validate()
    name = 'xiaojieluo'
    # name = dict(name='xiaojieluo')
    # name = ''
    v.set_rules(name, 'required|min_length:3|max_length:20|in_list[xiaojie, xiaojieluo , 10]|type[str]')
    # name_rules = ['required', 'min_length[3]']
    # v.set_rules(name, name_rules)
    # v.set_rules(name, ['required', 'min_length[3]', 'max_length[20]'])
    print(name)
    # try:
    #     v.set_rules(name, 'required|min_length[3]')
    # except ValidateError as e:
    #     print(e)
