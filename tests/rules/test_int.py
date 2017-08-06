import pytest
from vlde import Validator, ValidateError, RulesError

def test_int():
    '''test int type'''

    v = Validator()

    v.set_rules(int(), 'int')
    v.set_rules(123, 'int')
    v.set_rules(0, 'int')
    with pytest.raises(ValidateError):
        v.set_rules('', 'int')
    with pytest.raises(ValidateError):
        v.set_rules({}, 'int')
    with pytest.raises(ValidateError):
        v.set_rules(float(), 'int')
    with pytest.raises(ValidateError):
        v.set_rules([], 'int')
    with pytest.raises(ValidateError):
        v.set_rules((), 'int')
    with pytest.raises(ValidateError):
        v.set_rules(bool(), 'int')
    with pytest.raises(ValidateError):
        v.set_rules(bytes(), 'int')
    with pytest.raises(ValidateError):
        v.set_rules(None, 'int')
