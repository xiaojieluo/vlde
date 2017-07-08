'''
This is vlde exception
'''


class ValidateError(Exception):
    '''Validate Error'''

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class RequiredError(ValidateError):
    '''Required Error'''
    pass


class MinLengthError(ValidateError):
    '''min length error'''
    pass


class MaxLengthError(ValidateError):
    '''max length error'''
    pass


class LengthError(ValidateError):
    '''length error'''
    pass


class StrError(ValidateError):
    '''str error'''
    pass


class Ipv4Error(ValidateError):
    '''ipv4 error'''
    pass


class Ipv6Error(ValidateError):
    '''ipv6 error'''
    pass


class EmailError(ValidateError):
    '''email error'''
    pass


class UrlError(ValidateError):
    '''url error'''
    pass


class RangeError(ValidateError):
    '''range error'''
    pass


class GenreError(ValidateError):
    '''类型错误，与系统错误 TypeError 区分开'''
    pass


class InListError(ValidateError):
    '''in list error'''
    pass


class CallbackError(ValidateError):
    '''用户自定义验证函数抛出异常'''
    pass


class RulesError(Exception):
    '''规则错误， 抛出 RulesError 异常'''
    pass
