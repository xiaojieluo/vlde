import pytest
from vlde import Validator, ValidateError, RulesError

def test_str():
    '''test str type'''

    v = Validator()

    v.set_rules('hello', 'str|string')
    v.set_rules('', 'str|string')
    v.set_rules(str(123), 'str|string')

    with pytest.raises(ValidateError):
        v.set_rules(123, 'str')
    with pytest.raises(ValidateError):
        v.set_rules([], 'str')
    with pytest.raises(ValidateError):
        v.set_rules({}, 'str')
    with pytest.raises(ValidateError):
        v.set_rules((), 'str')
    with pytest.raises(ValidateError):
        v.set_rules(None, 'str')
    with pytest.raises(ValidateError):
        v.set_rules(bool(), 'str')
    with pytest.raises(ValidateError):
        v.set_rules(float(), 'str')
    with pytest.raises(ValidateError):
        v.set_rules(bytes(), 'str')
