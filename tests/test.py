from vlde.validate import Validator

v = Validator()

v.set_rules('str', 'range:1-10')
