import pytest
from vlde import Validator, ValidateError, RulesError

def test_dict():
    '''test dict type'''

    v = Validator()
    v.set_rules({}, 'dict')
    v.set_rules(dict(), 'dict')
    with pytest.raises(ValidateError):
        v.set_rules('', 'dict')
    with pytest.raises(ValidateError):
        v.set_rules([], 'dict')
    with pytest.raises(ValidateError):
        v.set_rules((), 'dict')
    with pytest.raises(ValidateError):
        v.set_rules(int(), 'dict')
    with pytest.raises(ValidateError):
        v.set_rules(float(), 'dict')
    with pytest.raises(ValidateError):
        v.set_rules(bytes(), 'dict')
    with pytest.raises(ValidateError):
        v.set_rules(bool(), 'dict')
    with pytest.raises(ValidateError):
        v.set_rules(None, 'dict')
