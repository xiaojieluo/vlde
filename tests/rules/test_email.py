import pytest
from vlde import Validator, ValidateError, RulesError

def test_email():
    '''email rule validate'''
    v = Validator()
    
    v.set_rules('xiaojieluoff@gmail.com', 'email')
    v.set_rules('1234@163.com', 'email')

    with pytest.raises(ValidateError):
        v.set_rules('emailemail', 'email')
