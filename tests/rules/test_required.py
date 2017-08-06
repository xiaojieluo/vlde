import pytest

from vlde.error import *
from vlde.validate import Validator

def test_required():
    '''
    rule 测试： required
    '''
    v = Validator()

    v.set_rules('string', 'required')
    v.set_rules(1024, 'required')
    v.set_rules(12.04, 'required')
    v.set_rules(bool(), 'required')
    v.set_rules(['luo', 'ff'], 'required')
    v.set_rules({'name': 'vlde'}, 'required')
    v.set_rules(('name', 'age'), 'required')
    v.set_rules(bytes('hello'.encode('utf-8')), 'required')

    with pytest.raises(ValidateError):
        v.set_rules('', 'required')
    with pytest.raises(ValidateError):
        v.set_rules([], 'required')
    with pytest.raises(ValidateError):
        v.set_rules({}, 'required')
    with pytest.raises(ValidateError):
        v.set_rules((), 'required')
    with pytest.raises(ValidateError):
        v.set_rules(bytes(), 'required')
    with pytest.raises(ValidateError):
        v.set_rules(None, 'required')

    with pytest.raises(RulesError):
        v.set_rules('string', 'requireds')
