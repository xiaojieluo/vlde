import pytest
from vlde import Validator, ValidateError, RulesError

def test_url():
    '''test url rule'''

    v = Validator()

    v.set_rules('http://google.com', 'url')
    v.set_rules('https://www.google.com', 'url')
    v.set_rules('ftp://google.com', 'url')
    v.set_rules('www.baidu.com', 'url')

    with pytest.raises(ValidateError):
        v.set_rules('baidu.com', 'url')
    with pytest.raises(ValidateError):
        v.set_rules('//baidu.com', 'url')
    with pytest.raises(ValidateError):
        v.set_rules(None, 'url')
