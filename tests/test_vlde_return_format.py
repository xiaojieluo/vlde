import pytest
from vlde import Validator, ValidateError, RulesError

def test_vlde_return_format_is_object():
    '''
    测试返回 object 类型的验证信息
    '''
    v = Validator(return_format='object')
    result1 = v.set_rules('string', 'str')
    assert result1.status is True
    result2 = v.set_rules('string', 'dict')
    assert result2.status is False

def test_vlde_return_format_is_exception():
    '''
    test return_format is exception
    '''
    v = Validator(return_format='exception')

    try:
        hello = 'hello, world'
        world = 'world, hello'
        v.set_rules(hello, 'required|str')
        v.set_rules(world, 'required|str')
    except ValidateError as e:
        print(e)
