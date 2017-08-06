import pytest
from vlde import Validator, ValidateError, RulesError

def test_length():
    '''rule test length'''
    v = Validator()

    v.set_rules('string', 'length:6')
    v.set_rules('', 'length:0')
    v.set_rules(['list1'], 'length:1')
    v.set_rules({'dict': 'dict'}, 'length:1')
    v.set_rules(('hello', 'world'), 'length:2')
    v.set_rules(None, 'length:0')
    v.set_rules(20, 'length:2')

    with pytest.raises(ValidateError):
        v.set_rules('string', 'length:0')
    with pytest.raises(ValidateError):
        v.set_rules(None, 'length:1')
    with pytest.raises(ValidateError):
        v.set_rules(20, 'length:20')

    with pytest.raises(RulesError):
        v.set_rules('string', 'length:-1')
    with pytest.raises(RulesError):
        v.set_rules('string', 'length:')
    with pytest.raises(RulesError):
        v.set_rules('string', 'length:3/4')
