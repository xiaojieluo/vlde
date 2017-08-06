import pytest
from vlde import Validator, ValidateError, RulesError

def test_ipv6():
    '''test ipv6 rule'''

    v = Validator()

    v.set_rules('0000:0000:0000:0000:0000:0000:0000:0000', 'ipv6')
    v.set_rules('ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'ipv6')
    v.set_rules('0:0:0:0:0:0:0:0', 'ipv6')
    v.set_rules('f:f:f:f:f:f:f:f', 'ipv6')
    v.set_rules('::', 'ipv6')
    v.set_rules('a::a', 'ipv6')

    with pytest.raises(ValidateError):
        v.set_rules('ff', 'ipv6')
    with pytest.raises(ValidateError):
        v.set_rules('192.168.1.1', 'ipv6')
