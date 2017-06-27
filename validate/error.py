
class ValidateError(Exception):
    def __init__(self, message):
            super().__init__(message)
            self.message = message
            # self.status = status

class RequiredError(ValidateError):
    pass

class Min_lengthError(ValidateError):
    pass

class Max_lengthError(ValidateError):
    pass
class Exact_lengthError(ValidateError):
    pass
class StrError(ValidateError):
    pass
class Ipv4Error(ValidateError):
    pass
class Ipv6Error(ValidateError):
    pass
class EmailError(ValidateError):
    pass
class UrlError(ValidateError):
    pass

class GenreError(ValidateError):
    '''
    类型错误，与系统错误 TypeError 区分开
    '''
    pass

class In_listError(ValidateError):
    pass

class RulesError(Exception):
    '''
    规则错误， 抛出 RulesError 异常
    '''
    pass
