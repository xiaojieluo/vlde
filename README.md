# This is a data integrity check library

### 返回格式
有两种方式获取验证信息，一种是 object 模式， 另一种是 exception 模式， 默认为 exception 模式

推荐在验证多个变量时使用 exception 模式，将 set_rules 放在 try: 块中， 捕获 ValidateError 进行处理

两种返回格式的区别：
* object 模式返回的错误信息类型是列表， 可以一次得到所有不符合验证规则的信息
* exception 模式遇到一个未通过的验证就抛出一个异常，无法一次性获取到所有的未通过验证信息

#### 对象

```python

v = Validator(return_format='object')

result = v.set_rules('hello', 'required|dict|max_length:3')

if result.status is False:
    print('\n'.join(result.error))

```

#### 异常

```python

v = Validator(return_format='exception')

try:
    v.set_rules('hello', 'required|dict')
except ValidateError as e:
    print(e)

```

-------

### 使用字符串类型的验证规则
