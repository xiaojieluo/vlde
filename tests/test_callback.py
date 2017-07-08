from vlde.error import *
from vlde.validate import Validator
from nose.tools import raises

v = Validator()

def function(key):
    return True if key == 'string' else False

@raises(RulesError)
def test_callback_str():
    '''测试 callback 为str'''
    v.set_rules('string', callback='hello')

@raises(ValidateError)
def test_lambda_error():
    '''测试 lambda 匿名函数'''
    v.set_rules('string', callback=lambda x:x=='strings')


def test_callback_none():
    '''测试 callback 为 None'''
    v.set_rules('string', callback=None)

def test_lambda():
    '''测试 lambda 函数'''
    v.set_rules('string', callback=lambda x:x=='string')
