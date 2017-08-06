import pytest
from vlde import Validator, ValidateError, RulesError

def test_in_list():
    '''
    rule test length
    只支持字符串，整型，浮点型变量
    '''
    
    v = Validator()
    v.set_rules('hello', 'in_list:hello, world')
    v.set_rules(123, 'in_list:123, 321')
    v.set_rules(123.4, 'in_list:123.4')

    with pytest.raises(ValidateError):
        v.set_rules('str', 'in_list:string')
    with pytest.raises(ValidateError):
        v.set_rules('ss', 'in_list:hello, world')

    with pytest.raises(RulesError):
        v.set_rules({}, 'in_list:dict')
    with pytest.raises(RulesError):
        v.set_rules([], 'in_list:list')
    with pytest.raises(RulesError):
        v.set_rules((), 'in_list:tuple')
    with pytest.raises(RulesError):
        v.set_rules(None, 'in_list:None')
