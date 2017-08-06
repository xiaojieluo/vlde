import pytest
from vlde import Validator, ValidateError, RulesError

def test_list():
    '''test list type'''
    v = Validator()

    v.set_rules(list(), 'list')
    v.set_rules([], 'list')

    with pytest.raises(ValidateError):
        v.set_rules('', 'list')
    with pytest.raises(ValidateError):
        v.set_rules({}, 'list')
    with pytest.raises(ValidateError):
        v.set_rules((), 'list')
    with pytest.raises(ValidateError):
        v.set_rules(int(), 'list')
    with pytest.raises(ValidateError):
        v.set_rules(float(), 'list')
    with pytest.raises(ValidateError):
        v.set_rules(bytes(), 'list')
    with pytest.raises(ValidateError):
        v.set_rules(bool(), 'list')
    with pytest.raises(ValidateError):
        v.set_rules(None, 'list')
