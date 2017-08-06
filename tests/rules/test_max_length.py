import pytest
from vlde import Validator, ValidateError, RulesError

def test_max_length():
    '''
    rule test: max_lenght
    '''
    v = Validator()
    v.set_rules('string', 'max_length:6')
    v.set_rules('', 'max_length:0')
    v.set_rules(None, 'max_length:0')
    v.set_rules({'hello': 'world'}, 'max_length:1')

    with pytest.raises(ValidateError):
        v.set_rules('string', 'max_length:1')
    with pytest.raises(ValidateError):
        v.set_rules({'dict': 'world'}, 'max_length:0')
    with pytest.raises(ValidateError):
        v.set_rules(('tuple'), 'max_length:0')
    with pytest.raises(ValidateError):
        v.set_rules(['list'], 'max_length:0')
    with pytest.raises(ValidateError):
        v.set_rules(None, 'max_length:1')

    with pytest.raises(RulesError):
        v.set_rules('string', 'max_length:-1')
    with pytest.raises(RulesError):
        v.set_rules('string', 'max_length:abc')
    with pytest.raises(RulesError):
        v.set_rules('string', 'max_length:')
    with pytest.raises(RulesError):
        v.set_rules('string', 'max_length:1 3/4')
