from vlde import Validator, ValidateError

v = Validator()
try:
    v.set_rules('string', 'max_length:1')
except ValidateError as e:
    print(e)
