
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

class In_listError(ValidateError):
    pass
