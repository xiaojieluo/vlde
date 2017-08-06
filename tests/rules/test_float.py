import pytest
from vlde import Validator, ValidateError, RulesError

def test_float():
    '''test float type '''
    v = Validator()
    v.set_rules(float(), 'float')
    v.set_rules(123.456, 'float')
    v.set_rules(123.00, 'float')

    with pytest.raises(ValidateError):
        v.set_rules('', 'float')
    with pytest.raises(ValidateError):
        v.set_rules({}, 'float')
    with pytest.raises(ValidateError):
        v.set_rules((), 'float')
    with pytest.raises(ValidateError):
        v.set_rules([], 'float')
    with pytest.raises(ValidateError):
        v.set_rules(int(), 'float')
    with pytest.raises(ValidateError):
        v.set_rules(bool(), 'float')
    with pytest.raises(ValidateError):
        v.set_rules(bytes(), 'float')
    with pytest.raises(ValidateError):
        v.set_rules(None, 'float')
