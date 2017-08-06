import pytest
from vlde import Validator, ValidateError, RulesError

def test_range():
    '''test range rule'''

    v = Validator()

    v.set_rules(20, 'range:1-21')
    v.set_rules(20, 'range:20')
    v.set_rules(20.0, 'range:20.0-100.0')
    v.set_rules(int('20'), 'range:20')

    with pytest.raises(ValidateError):
        v.set_rules(0, 'range:10-100')
    with pytest.raises(ValidateError):
        v.set_rules(0, 'range:1')

    with pytest.raises(RulesError):
        v.set_rules('20', 'range:20')
    with pytest.raises(RulesError):
        v.set_rules(dict(), 'range:0')
    with pytest.raises(RulesError):
        v.set_rules(20, 'range:a-z')
    with pytest.raises(RulesError):
        v.set_rules('string', 'range:hello')
    with pytest.raises(RulesError):
        v.set_rules(None, 'range:0')
