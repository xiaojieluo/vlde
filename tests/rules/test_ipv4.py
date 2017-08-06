import pytest
from vlde import Validator, ValidateError, RulesError

def test_ipv4():
    '''test ipv4 rule'''

    v = Validator()

    v.set_rules('192.168.1.1', 'ipv4')
    v.set_rules('255.255.255.255', 'ipv4')
    v.set_rules('0.0.0.0', 'ipv4')

    with pytest.raises(ValidateError):
        v.set_rules('192.168.1111', 'ipv4')
    with pytest.raises(ValidateError):
        v.set_rules('-1-1-1-1', 'ipv4')
    with pytest.raises(ValidateError):
        v.set_rules(None, 'ipv4')
