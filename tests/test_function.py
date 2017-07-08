from vlde.error import *
from vlde.validate import Validator
from nose.tools import raises

v = Validator()

def function(key):
    return True if key == 'string' else False

@raises(RulesError)
def test_func():
    '''测试函数'''
    v.set_rules('string', callback='hello')
