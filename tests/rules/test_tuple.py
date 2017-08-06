import pytest
from vlde import Validator, ValidateError, RulesError

def test_tuple():
    '''test tuple type '''

    v = Validator()

    v.set_rules((), 'tuple')
    v.set_rules((123,), 'tuple')

    with pytest.raises(ValidateError):
        v.set_rules('', 'tuple')
    with pytest.raises(ValidateError):
        v.set_rules({}, 'tuple')
    with pytest.raises(ValidateError):
        v.set_rules(float(), 'tuple')
    with pytest.raises(ValidateError):
        v.set_rules([], 'tuple')
    with pytest.raises(ValidateError):
        v.set_rules(int(), 'tuple')
    with pytest.raises(ValidateError):
        v.set_rules(bool(), 'tuple')
    with pytest.raises(ValidateError):
        v.set_rules(bytes(), 'tuple')
    with pytest.raises(ValidateError):
        v.set_rules(None, 'tuple')
