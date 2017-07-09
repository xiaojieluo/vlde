import pytest
from vlde.error import *
from vlde.validate import Validator

v = Validator()

def test_parse_rules():
    '''测试规则'''
    v.set_rules('string', 'str')
    v.set_rules('string', ['str'])
