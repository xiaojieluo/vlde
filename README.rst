vlde: easy-to-use for validate data
=========
.. image:: https://img.shields.io/pypi/v/vlde.svg
    :target: https://pypi.org/project/vlde/

.. image:: https://img.shields.io/pypi/l/vlde.svg
    :target: https://pypi.org/project/vlde/

.. image:: https://travis-ci.org/xiaojieluo/vlde.svg?branch=master
    :target: https://travis-ci.org/xiaojieluo/vlde

.. image:: https://codecov.io/gh/xiaojieluo/vlde/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/xiaojieluo/vlde

使用
-----

.. code-block:: python

    from vlde import Validator

    v = Validator(return_format='object')
    result = v.set_rules('hello', 'required|dict|max_length:3')
    if result.status is False:
        print('\n'.join(result.error))

或者捕获异常：

.. code-block:: python

    from vlde import ValidateError, Validator

    v = Validator(return_format='exception')
    try:
        v.set_rules('hello', 'required|dict')
    except ValidateError as e:
        print(e)

开启规则错误提示
--------------
默认情况下，若传入错误的规则名称， vlde 会找不到验证规则，并返回验证通过。如果想关闭此功能，只需要在定义变量时，传入 `warning_rule = True` 即可

.. code-block:: python

    from vlde import ValidateError, Validator, RulesError

    v = Validator(warning_rule=True)
    try:
        v.set_rules('hello' 'strssss')
    except RulesError as e:
        print(e)

也可以为单个的 set_rules 单独设置 warning_rule:

.. code-block:: python

    from vlde import ValidateError, Validator

    v = Validator()
    v.set_rules('hello', 'strssss', warning_rule=False)
    try:
        v.set_rules('hello', 'strssss', warning_rule=True)
    except RulesError as e:
        print(e)


validate 内置规则
------------------------

规则参考
^^^^^^^^^^^^^

下表列出了 vlde 可用的规则

+--------------+------+----------------------------------------+---------------------------------------------------+
| 规则         | 参数 | 描述                                   | 例子                                              |
+==============+======+========================================+===================================================+
| required     |      | 如果变量值为空或者为 None, 验证不通过  | `v.set_rules(None, 'required')`                   |
+--------------+------+----------------------------------------+---------------------------------------------------+
| min_length   | int  | 如果变量值长度小于参数值, 验证不通过   | `v.set_rules('hello','min_length:6')`             |
+--------------+------+----------------------------------------+---------------------------------------------------+
| max_length   | int  | 如果变量值长度大于参数值, 验证不通过   | `v.set_rules('hello', 'max_length:2')`            |
+--------------+------+----------------------------------------+---------------------------------------------------+
| exact_length | int  | 如果变量值长度不等于参数值, 验证不通过 | `v.set_rules('hello', 'exact_length:5')`          |
+--------------+------+----------------------------------------+---------------------------------------------------+
| in_list      | list | 如果变量值不在规定的列表中，验证不通过 | `v.set_rules('hello', 'in_list[hello, helloss]')` |
+--------------+------+----------------------------------------+---------------------------------------------------+
| str          |      | 如果变量类型不为 str， 验证不通过      | `v.set_rules('hello', 'str')`                     |
+--------------+------+----------------------------------------+---------------------------------------------------+
| dict         |      | 如果变量类型不为 dict， 验证不通过     | `v.set_rules({'name':'luo'}, 'dict')`             |
+--------------+------+----------------------------------------+---------------------------------------------------+
| list         |      | 如果变量类型不为 list， 验证不通过     | `v.set_rules([1, 2, 3], 'list')`                  |
+--------------+------+----------------------------------------+---------------------------------------------------+
| bool         |      | 如果变量类型不为 bool， 验证不通过     | `v.set_rules(True, 'bool')`                       |
+--------------+------+----------------------------------------+---------------------------------------------------+
| float        |      | 如果变量类型不为 foat， 验证不通过     | `v.set_rules(1.1,'float')`                        |
+--------------+------+----------------------------------------+---------------------------------------------------+
| int,integer  |      | 如果变量类型不为 int， 验证不通过      | `v.set_rules(10, 'int')`                          |
+--------------+------+----------------------------------------+---------------------------------------------------+
| tuple, tup   |      | 如果变量类型不为 tuple， 验证不通过    | `v.set_rules((1, 2, 3), 'tuple')`                 |
+--------------+------+----------------------------------------+---------------------------------------------------+
| ipv4         | str  | 如果变量值不为 ipv4 地址, 验证不通过   | `v.set_rules('192.168.1.1', 'ipv4')`              |
+--------------+------+----------------------------------------+---------------------------------------------------+
| ipv6         | str  | 如果变量值不为 ipv6 地址, 验证不通过   | `v.set_rules('5e:0:0:0:0:0:5668:eeee', 'ipv6')`   |
+--------------+------+----------------------------------------+---------------------------------------------------+
| email        | str  | 如果变量值不为邮箱地址, 验证不通过     | `v.set_rules('xiaojieluoff@gmail.com' 'email')`   |
+--------------+------+----------------------------------------+---------------------------------------------------+

规则容错
^^^^^^
* `int , integer` 都指代 int 类型
* `tuple, tup` 都指代 tuple 类型
