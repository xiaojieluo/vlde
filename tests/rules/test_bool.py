import pytest
from vlde import Validator, ValidateError, RulesError

def test_bool():
    '''test bool type '''
    v = Validator()

    v.set_rules(bool(), 'bool')
    v.set_rules(True, 'bool')
    v.set_rules(False, 'bool')

    with pytest.raises(ValidateError):
        v.set_rules('', 'bool')
    with pytest.raises(ValidateError):
        v.set_rules({}, 'bool')
    with pytest.raises(ValidateError):
        v.set_rules((), 'bool')
    with pytest.raises(ValidateError):
        v.set_rules([], 'bool')
    with pytest.raises(ValidateError):
        v.set_rules(int(), 'bool')
    with pytest.raises(ValidateError):
        v.set_rules(float(), 'bool')
    with pytest.raises(ValidateError):
        v.set_rules(bytes(), 'bool')
    with pytest.raises(ValidateError):
        v.set_rules(None, 'bool')
