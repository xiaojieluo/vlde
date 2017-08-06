import pytest
from vlde import Validator, ValidateError, RulesError

def test_function():
    '''
    用户自定义验证函数
    支持匿名函数
    '''

    def valid(key):
        if key == 'string':
            return True
        else:
            return False

    v = Validator()

    v.set_rules('string', callback=valid)
    v.set_rules('string', callback=lambda x: x == 'string')
    v.set_rules('string', callback=None)
    v.set_rules(['hello'], callback=lambda x: x == ['hello'])
    v.set_rules({'name': 'vlde'}, callback=lambda x: x == dict(name='vlde'))
    v.set_rules(('name', 'vlde'), callback=lambda x: x == ('name', 'vlde'))
    v.set_rules(123, callback=lambda x: x == 123)
    v.set_rules(123.4, callback=lambda x: x == 123.4)
    v.set_rules(True, callback=lambda x: x == True)
    v.set_rules(bytes(123), callback=lambda x: x == bytes(123))

    with pytest.raises(ValidateError):
        v.set_rules('string', callback=lambda x: x == 'key')
    with pytest.raises(ValidateError):
        v.set_rules(bytes(123), callback=lambda x: x == bytes(1234))

    with pytest.raises(RulesError):
        v.set_rules('string', callback='str', warning_rule=True)
