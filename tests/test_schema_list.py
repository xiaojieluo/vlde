import pytest
from vlde import Validator, ValidateError, RulesError

def test_schema_list():
    v = Validator()

    v.set_rules([10, 20, 'string'], schema=['int', 'int', 'str'])
    v.set_rules([20, 30, ['hello']], schema=['int', 'int', ['str']])
    v.set_rules([20, 30, ['']], schema=['int', 'int', 'required'])
