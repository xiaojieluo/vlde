vlde: easy-to-use for validate data
=========

.. image:: https://travis-ci.org/xiaojieluo/vlde.svg?branch=master
    :target: https://travis-ci.org/xiaojieluo/vlde
.. image:: https://codecov.io/gh/xiaojieluo/vlde/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/xiaojieluo/vlde

# TODO
* 将 unittest 测试框架换成 pytest

# This is a data integrity check library
### validate 内置规则
#### 规则参考
下表列出了 vlde 可用的规则

| 规则 | 参数 | 描述 | 例子|
| :-- | :--  | :-- | :-- |
|   required    |           |   如果变量值为空或者为 None, 验证不通过   |   `v.set_rules(None, 'required')`           |
|   min_length  |   int     |   如果变量值长度小于参数值, 验证不通过     |   `v.set_rules('hello', 'min_length:6')`    |
|   max_length  |   int     |   如果变量值长度大于参数值, 验证不通过     |   `v.set_rules('hello', 'max_length:2')`    |
|   exact_length    |   int |   如果变量值长度不等于参数值, 验证不通过   |   `v.set_rules('hello', 'exact_length:5')`  |
|   in_list     |   list    |   如果变量值不在规定的列表中，验证不通过   |   `v.set_rules('hello', 'in_list[hello, helloss]')`|
|   str     |       |   如果变量类型不为 str, 验证不通过     |   `v.set_rules('hello', 'str')` |
|   dict    |   |   如果变量类型不为 dict， 验证不通过    |   `v.set_rules({'name':'luo'}, 'dict')` |
|   list    |   |   如果变量类型不为 list， 验证不通过    |   `v.set_rules([1, 2, 3], 'list')`  |
|   bool    |   |   如果变量类型不为 bool， 验证不通过    |   `v.set_rules(True, 'bool')`  |
|   float   |   |   如果变量类型不为 foat， 验证不通过    |   `v.set_rules(1.1, 'float')`   |
|   int,integer     |   |   如果变量类型不为 int， 验证不通过 |   `v.set_rules(10, 'int')`    |
|   tuple, tup  |   |   如果变量类型不为 tuple， 验证不通过   |   `v.set_rules((1, 2, 3), 'tuple')`   |
|   ipv4    |   str |   如果变量值不为 ipv4 地址, 验证不通过   |   `v.set_rules('192.168.1.1', 'ipv4')`    |
|   ipv6    |   str |   如果变量值不为 ipv6 地址, 验证不通过   |   `v.set_rules('5e:0:0:0:0:0:5668:eeee', 'ipv6')` |
|   email   |   str |   如果变量值不为邮箱地址, 验证不通过      |   `v.set_rules('xiaojieluoff@gmail.com' 'email')` |

#### 规则容错
* `int , integer` 都指代 int 类型
* `tuple, tup` 都指代 tuple 类型

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
