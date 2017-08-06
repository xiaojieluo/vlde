import pytest
from vlde import Validator, ValidateError, RulesError

def test_schema_dict():
    v = Validator()
    
    v.set_rules(dict(name='llnhhy'), schema=dict(name='str'))
    v.set_rules(dict(name='llnhhy', age=17), schema=dict(name='str', age='int'))
    v.set_rules(dict(name='luo', girlfriend=dict(name='wu', age=20)), schema=dict(name='str', girlfriend=dict(name='str', age='int')))
    v.set_rules(dict(name='luo', girlfriend=dict(name='wu', age=20)), schema=dict(name='str', girlfriend='dict'))
    v.set_rules(dict(name='luo', girlfriend=['wu', 'sun', 'li']), schema=dict(name='str', girlfriend=['str', 'str', 'max_length:2']))
    v.set_rules({'name':'luo', 'age':20}, schema={'name':'str', 'age':'int'})
    v.set_rules({'name':'luo', 'age':20}, schema={'name':'str'})
    v.set_rules({'name':'luo', 'age':20}, schema={'name':'str', 'age':'int|min_length:2'})
    v.set_rules({'name':'luo', 'age':20}, rule='dict|max_length:2', schema={'name':'str', 'age':'int'})
