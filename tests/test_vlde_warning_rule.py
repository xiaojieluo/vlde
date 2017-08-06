import pytest
from vlde import ValidateError, RulesError,Validator

v = Validator(warning_rule=True)

def test_warning_rule_is_true():
    '''
    test if Validator warning_rule is True
    '''
    v = Validator(warning_rule=True)

    with pytest.raises(RulesError):
        v.set_rules('hello', 'i see')


def test_warning_rule_is_false():
    '''
    test if Validator warning_rule is False
    '''
    v = Validator(warning_rule=False)

    v.set_rules('hello', 'i see')
