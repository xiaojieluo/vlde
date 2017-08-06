import pytest
from vlde import Validator, ValidateError, RulesError

def test_set_rules():
    '''set_rules 參數測試'''

    v = Validator()

    v.set_rules(None)
    v.set_rules('string', rule=None)
    v.set_rules('string', schema='str')
    v.set_rules(dict(hello='world'), schema=dict())

def test_set_rules_warning_rule_is_true():
    '''
    test set_rules method warning_rule is true
    '''
    v = Validator()

    with pytest.raises(RulesError):
        v.set_rules('string', 'strssss', warning_rule=True)

def test_set_rules_warning_rule_is_false():
    '''
    test_set_rules method warning_rule is false
    '''
    v = Validator()

    v.set_rules('string', 'strssss', warning_rule=False)
