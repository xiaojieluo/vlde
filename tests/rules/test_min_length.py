import pytest

from vlde.error import *
from vlde.validate import Validator

def test_min_length():
    '''
    rule test: min_length
    '''
    v = Validator()
    v.set_rules('string', 'min_length:6')
    v.set_rules('', 'min_length:0')
    v.set_rules(None, 'min_length:0')
    
    with pytest.raises(ValidateError):
        v.set_rules(100, 'min_length:4')
    with pytest.raises(ValidateError):
        v.set_rules('', 'min_length:1')
    with pytest.raises(ValidateError):
        v.set_rules([], 'min_length:1')
    with pytest.raises(ValidateError):
        v.set_rules({}, 'min_length:1')
    with pytest.raises(ValidateError):
        v.set_rules((), 'min_length:1')
    with pytest.raises(ValidateError):
        v.set_rules(None, 'min_length:10')
    with pytest.raises(RulesError):
        v.set_rules('string', 'min_length:-1')
    with pytest.raises(RulesError):
        v.set_rules(bool(), 'min_length:1')
    with pytest.raises(RulesError):
        v.set_rules('string', 'min_length:abc')
    with pytest.raises(RulesError):
        v.set_rules('string', 'min_length:')
    with pytest.raises(RulesError):
        v.set_rules('string', 'min_length:3/4')
