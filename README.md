# This is a data integrity check library

## How to use

### 使用字符串类型的验证规则

```python
from validate import Validate
v = Validate()
name = 'xiaojieluo'
try:
    v.validate(name, 'required|max_length:10|min_length:3')
except ValidateError as e:
    print(e)
```

### 使用列表类型的验证规则

```python

from validate import Validate

v = Validate()
name = 'xiaojieluo'
rules = ['required', 'min_length:3', 'max_length:10']

try:
    v.validate(name, rules)
except ValidateError as e:
    print(e)
```
