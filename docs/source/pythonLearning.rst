Python学习
=====

.. _introduction:

Python语言概述
=================

Python是一种高级、解释型、通用的编程语言，由Guido van Rossum于1991年首次发布。其设计哲学强调代码的可读性和简洁性，尤其是使用显式的缩进来划分代码块，这一特性使得Python代码显得干净且易于理解。

.. _mainFeatures:

主要特点
---------

 - 易读易写：

   Python的语法简洁明了，接近自然语言，使得新手也能较快上手。
   使用缩进而不是大括号来分隔代码块，提高代码的可读性。

 - 丰富的标准库：

   Python拥有一个庞大且功能丰富的标准库，涵盖了文件I/O、系统调用、网络编程、数据库访问、文本处理等各个方面。
   标准库的强大使得很多任务可以直接使用内置模块完成，减少了开发时间和代码量。

 - 跨平台：

   Python是跨平台的，可以在Windows、Mac OS、Linux等多个操作系统上运行。
   只要Python解释器可以运行，Python代码就可以不做修改地运行在不同的操作系统上。

 - 多种编程范式支持：

   Python支持面向对象编程（OOP）、函数式编程、过程式编程等多种编程范式。
   这种灵活性使得Python适用于各种编程任务。

 - 动态类型和垃圾回收：

   Python是动态类型语言，变量类型在运行时确定，无需提前声明。
   内置垃圾回收机制自动管理内存，减少内存泄漏和管理复杂度。

常见应用领域
-----------

 - Web开发：

   使用Django、Flask等Web框架可以快速构建高效的Web应用程序。

 - 数据科学与人工智能：

   丰富的科学计算库（如NumPy、Pandas）和机器学习库（如TensorFlow、PyTorch）使得Python成为数据科学和AI领域的首选语言。

 - 自动化脚本：

   由于语法简单、库丰富，Python非常适合编写各种自动化脚本，处理日常任务。

 - 系统运维：

   系统管理员常用Python编写脚本来管理服务器、自动化运维任务。

 - 软件测试：

 - Python的unittest、pytest等测试框架简化了测试脚本的编写和执行，广泛应用于软件测试领域。

Python的缺点
-----------

 - 性能：

   由于是解释型语言，Python的运行速度通常比编译型语言（如C/C++）慢。
   对性能要求极高的场景，Python可能不是最佳选择。

 - 移动开发：

   虽然有Kivy等框架支持，Python在移动应用开发方面不如Java、Kotlin（Android）和Swift（iOS）等语言流行和成熟。

 - 全局解释器锁（GIL）：

   Python的多线程模型受到GIL的限制，多线程在CPU密集型任务中表现不佳。

变量和简单数据类型
===================

 - 变量的命名和使用：

  变量名只能包含字母、数字和下划线。变量名能以字母或下划线打头，但不能以数字打头。例如可以是 `message_1` ，但不能是 `1_message` 。

  变量名不能包含空格，但能使用下划线来分隔其中的单词。例如变量名 `greeting_message` 可行，但是 `greeting message` 会引发错误。

  同时不能将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，比如print。

  变量名应简短又有描述性。例如 `name` 比 `n` 好。

  慎用小写字母 `l` 和大写字母 `O` ，因为他们可能被人看错成数字 `1` 和 `0` 。

变量是标签
------------------

变量通常被描述为可用于存储值的盒子。

.. code-block:: python

    message = "Hello world!"
    print(message)

字符串
-----------------

字符串就是一系列字符。在Python中用引号括起的都涉及字符串，其中的引号可以是单引号，也可以是双引号，如下段代码所示：

.. code-block:: python

    "This is a string."
    "This is also a string."

使用方法修改字符串的大小
~~~~~~~~~~~~~~~~~~~~

对字符串的处理最简单的就是修改其中的单词的大小写。

.. code-block:: python

    name = "ada lovelace"
    print(name.title())

这段代码的输出是

::

    Ada Lovelace

类似操作还有

.. code-block:: python

    name = "Ada Lovelace"
    print(name.upper())
    print(name.lower())

输出如下

::

    ADA LOVELACE
    ada lovelace

在字符串中使用变量
~~~~~~~~~~~~~~~~~~

在字符串中使用变量的值的方法。

.. code-block:: python

    first_name = "ada"
    last_name = "lovelace"
    full_name = f"{first_name} {last_name}"
    print(full_name)

输出为

::

    ada lovelace

这里的 `f` 是 `format` 的简写，是Python通过把花括号内的变量替换为其值来设置字符串的格式。

使用制表符或换行符来添加空白
~~~~~~~~~~~~~~~~~~~~~~~

在编程中，**空白**泛指任何非打印字符，如空格、制表符和换行符。制表符为 "\t"，换行符为"\n"。

.. code-block:: python

    print("Languages:\n\tPython\n\tC\n\tJavascript")
    Languages:
        Python
        C
        Javescript

删除空白
~~~~~~~~~~~~~~~~~~~~~~

空白很重要，因为你经常需要比较两个字符串是否相同。比如，在用户登录网站时检查其用户名。Python中删除空白的命令包括 `rstrip()、lstrip()和strip()` 。

但是如果要永久删除字符串中的空白，还需要将删除操作的结果关联到变量中

.. code-block:: python

    favorite_language = "python "
    favorite_language = favorite_language.rstrip()

这样再次询问这个变量的值时，python面的空格也不会出现了。

同时给多个变量赋值
~~~~~~~~~~~~~~~~~~~~

可以在一行代码中给多个变量赋值，有助于缩短程序并提高其可读性。

.. code-block:: python

    x, y, z = 0, 0, 0

数
------------------

常量
~~~~~~~~~~~~~~~~~~~

Python程序员会使用全大写来指出应将某个变量视为常量，其值应始终不变：

.. code-block:: python

    MAX_CONNECTIONS = 5000

列表简介
=================

列表
------------------

列表由一系列按特定顺序排列的元素组成。在Python中使用（[]）表示列表，并用逗号分隔其中的元素。

.. code-block:: python

    bicycles = ['trek','cannondale','redline','specialized']
    print(bicycles)
  
打印的结果是

::

    ['trek','cannondale','redline','specialized']

同时，列表是有序集合，因此有

.. code-block:: python

    bicycles = ['trek','cannondale','redline','specialized']
    print(bicycles[0])

这样就可以根据索引得到列表中的第一个元素，即

::

    trek

.. note::

   注意：索引是从 `0`` 开始而不是从 `1` 开始。同时，最后一个元素可以用 `-1` 来索引。

组织列表
-----------------------

使用方法 `sort()` 对列表永久排序
~~~~~~~~~~~~~~~~~~~~~~~

Python可以使用 `sort()` 永久地修改列表元素的排列顺序。比如有汽车列表：

.. code-block:: python

    cars = ['bmw','audi','toyota','subaru']

我们使用sort()命令

.. code-block:: Python

    cars.sort()
    print(cars)

我们可以得到根据按照字母顺序排列的列表

.. code-block:: python

    ['audi','bmw','subaru','toyota']

同时，我们也可以让字母按照逆序来排列，只需要向 `sort()` 方法传递参数 `reverse=True` 即可

.. code-block:: python

    cars = ['bmw','audi','toyota','subaru']
    cars.sort(reverse=True)
    print(cars)

这样，我们得到的即为逆序排列的列表

.. code-block:: python

    ['toyota','subaru','bmw','audi']

使用函数 `sorted()` 对列表临时排序
~~~~~~~~~~~~~~~~~~~~~~

使用函数 `sorted()` 可以保留列表元素原来的排列顺序，并以特定的顺序呈现它们。

.. code-block:: python

    cars = ['bmw','audi','toyota','subaru']
    print(sorted(cars))
    print(cars)

这两段的输出分别是

.. code-block:: python

    ['audi','bmw','subaru','toyota']
    ['bmw','audi','toyota','subaru']

可以看出列表元素的顺序并没有发生改变，但是我们用特定顺序呈现了它们。当然我们也可以使用函数 `reverse=True` 来逆序排列。

倒着打印列表
~~~~~~~~~~~~~~~~~~~~~~~

要反着打印列表，可以使用方法reverse()。

.. code-block:: python

    cars = ['bmw','audi','toyota','subaru']
    print(cars)

    cars.reverse()
    print(cars)

这样可以得到如下输出

.. code-block:: python

    ['bmw','audi','toyota','subaru']
    ['subaru','toyota','audi','bmw']

.. note::

   注意：reverse()不是按照与字母顺序相反的顺序来排列列表元素，而只是反转列表元素的排列顺序，同时该方法也是永久性的修改列表元素的排列顺序。

确定列表的长度
~~~~~~~~~~~~~~~~~~~

使用len()可以快速获取列表的长度。

::

    >>> cars = ['bmw','audi','toyota','subaru']
    >>> len(cars)

输出如下

::

    4

.. note::

   注意：Python计算列表元素长度时从1开始，因此确定列表长度时，应该不会遇到差一错误。

操作列表
===================

遍历整个列表
--------------------

需要对列表中的每个元素都执行相同的操作时，可使用Python中的 `for` 循环。比如下方代码

.. code-block:: python

        magicians = ['alice','david','carolina']
        for magician in magicians:
            print(magician)

该段代码的输出为

.. code-block:: python

        alice
        david
        carolina

创建数值列表
--------------------

使用函数range()
~~~~~~~~~~~~~~~~~~~~~

Python函数range()可以轻松的生成一系列数。例如

.. code-block:: python

        for value in range(1,5):
            print(value)

下面是输出，可以发现包含了1，但是没有包含5

.. code-block:: python

        1
        2
        3
        4

使用range()创建数字列表
~~~~~~~~~~~~~~~~~~~

要创建数字列表，可以使用函数list()将range()的结果直接转换成列表，如

.. code-block:: python

        numbers = list(range(1,6))
        print(numbers)

输出如下

.. code-block:: python

        [1, 2, 3, 4, 5]

使用 `range()` 时，可以指定步长。如打印 `1 ~ 10` 的偶数

.. code-block:: python

        even_numbers = list(range(2, 11, 2))
        print(even_numbers)

输出如下

.. code-block:: python

        [2, 4, 6, 8, 10]

可以看出从2到11，每隔2输出了一个数字。

对数字列表执行简单的统计计算
~~~~~~~~~~~~~~~~~~~~

专门用于处理数字列表的Python函数包括：

::

    >>> min()
    >>> max()
    >>> sum()

列表解析
~~~~~~~~~~~~~~~~~~~~~~

列表解析即使用较短的代码实现长代码相同的操作，比如下面这两段代码

代码a：

.. code-block:: python

        lifang1 = []
        for value in range(1,10):
            lifang = value ** 3
            lifang1.append(lifang)
        
        print(lifang1)

代码b：

.. code-block:: python

        lifang2 = [ value ** 3 for value in range(1,10) ]
        print(lifang2)

这两段代码的输出都为

.. code-block:: python

        [1, 8, 27, 64, 125, 216, 343, 512, 729]

使用列表的一部分
---------------

切片
~~~~~~~~~~~~~~

要创建切片，可以指定要使用的第一个元素和最后一个元素的索引。与 `range()` 一样，Python在到达第二个索引之前的元素后停止。比如：

.. code-block:: python

        players = ['charles','martina','michael','florence','eli']
        print(players[0:3])

这样我们得到的输出为第0个元素、第1个元素和第2个元素：

.. code-block:: python

        ['charles','martina','michael']

遍历列表
~~~~~~~~~~~~~~

如果要遍历列表中的部分元素，可以在for循环中使用切片

.. code-block:: python

        players = ['charles','martina','michael','florence','eli']
        print("Here are the first three players on my team:")
        for player in players[:3]:
            print(player.title())

我们可以得到如下输出

::
    
    Here are the first three players on my team:
    Charles
    Martina
    Michael

复制列表
~~~~~~~~~~~~~~~~

我们可以通过同时省略起始索引和终止索引([:])来创建一个包含整个列表的切片。

元组
----------------

Python将不能修改的值称为不可变的，而不可变的列表被称为元组。

定义元组
~~~~~~~~~~~~~~~~~~

元组看起来像列表，但使用圆括号而非中括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。

比如，

.. code-block:: python

        dimensions = ( 200 , 50 )
        print(dimensions[0])
        print(dimensions[1])

输出如下

.. code-block:: python

        200
        50

同样，我们也可以使用 `for` 循环来遍历元组中的所有值

.. code-block:: python

        dimensions = ( 200 , 50 )
        for dimension in dimensions:
            print(dimension)

输出同上一个代码块一样。

.. note::

    元组可以被重修赋值，但是不能被修改。

如果想要修改元组中的变量，可以通过重新赋值的方式

.. code-block:: python

        dimensions = ( 200, 50 )
        print("Original dimensions:")
        for dimension in dimensions:
            print(dimension)

        dimensions = ( 400 , 100 )
        print("\nModified dimensions:")
        for dimension in dimensions:
            print(dimension)

输出如下

.. code-block:: python

        Original dimensions:
        200
        50
        
        Modified dimensions:
        400
        100

if语句
==================

简单示例
-------------

.. code-block:: python

        cars = ['audi', 'bmw', 'subaru', 'toyota']

        for car in cars:
            if car == 'bmw':
                print(car.upper())

            else:
                print(car.title())

得到的输出如下

.. code-block:: python

    Audi
    BMW
    Subaru
    Toyota

条件测试
-------------

每条if语句的核心都是一个值为 `True` 或 `False` 的表达式，这种表达式称为条件测试。

比如 `==` 符号则为判断两侧是否相等的符号

.. code-block:: python

    car = 'bmw'
    car == 'bmw'
    True
    car == 'audi'
    False

同样，还有 `!=` 来判断是否前面的值和该符号后边的值是否不等，如果不等则执行后续代码

.. code-block:: python

    requested_topping = 'mushrooms'

    if requested_topping != 'anchovies':
        print('Hold the anchovies!')

输出为

.. code-block:: python

    Hold the anchovies!

上述方法同样适用于数值，可以引申到符号 `>=` 和 `<=`，这些符号中间还可以穿插 `and` 或者 `or`来实现多个条件的同时判断。


if语句
----------------

可以看下面代码进行理解

.. code-block:: python

    age = 19
    if age >= 18:
        print("You are old enough to vote!")
        print("Have you vote yet?")
    print("emmm")

当 `age=19` 时，输出为

.. code-block::

    You are old enough to vote!
    Have you vote yet?
    emmm

而当 `age=17` 时，输出为

.. code-block::

    emmm

上段代码中的print("emmm")可以理解为

.. code-block:: python

    age = 19
    if age >= 18:
        print("You are old enough to vote!")
        print("Have you vote yet?")
    else:
        print("emmm")

当然，还可以用更复杂的形式

.. code-block:: python

    age = 19
    if age >= 18 and age < 60:
        print("You are old enough to vote!")
        print("Have you vote yet?")
    elif age >= 60:
        print("Good year!")
    else:
        print("emmm")

还可以通过 `elif` 实现更多的分段。

对于 `for` 和 `if` 联用的方式可以参考下面的代码

.. code-block:: python

    available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
    requested_toppings = ['mushrooms','french fries','extra cheese']

    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry! We don't have {requested_topping}.")
    print("\nFinished making your pizza!")

这段代码的输出为

.. code-block:: python

    Adding mushrooms.
    Sorry! We don't have french fries.
    Adding extra cheese.

    Finished making your pizza! 

字典
==================

使用字典
---------------

在Python中，字典是一系列键值对。每个键都与一个值相关联，你可使用键来访问相关联的值。在Python中，字典用放在花括号（{}）中的一系列键值对表示，如前面的示例所示：

.. code-block:: python

    alien_0 = {'color':'green','points': 5}
    print(alien_0['color'])

这样输出的就是 `color` 键对应的值

.. code-block:: python

    green

当你想给上述的字典中添加键值对时，可以直接使用以下代码

.. code-block:: python

    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(alien_0)

这样，输出就会变成

.. code-block:: python

    {'color':'green','points': 5,'x_position': 0,'y_position': 25}

同时，当你想建立一个字典，但是不知道其中的键值对时，可以建立一个空字典，即

.. code-block:: python

    alien_0 = {}

后面再用添加键值对的方式像这个字典中添加键值对。

当然，字典中的值不是写死的，可以通过重新赋予键的值来进行替换，下面是一个示例

.. code-block:: python

    alien_0 = {'color':'yellow'}
    alien_0['color']='green'

如果不想要这个字典中的某个键值对，则可以使用 `del` 命令，比如

.. code-block:: python

    alien_0 = {'color':'green','points': 5}
    del alien_0['points']
    print(alien_0)

这样就删除了字典alien_0中的 `points` 键值对，得到下面的结果

.. code-block:: python

    {'color':'green'}

对于代码的结构来说，存储相似信息的字典一般的写法如下

.. code-block:: python

    favorite_languages = {
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python',
        }

通过这样的结构，能够更好的阅读代码的信息

对于查找字典中是否有我们需要的键值对时，可以使用 `get()`来访问值

.. code-block:: python

    alien_0 = {'color':'green','speed': 'slow'}

    point_value = alien_0.get('points','No point value assigned')
    print(point_value)

这样，即使在字典中没有这个键也不会报错，输出是

.. code-block:: python

    No point value assigned

如果 `points`后面没有第二个参数，则会输出 `None`。

遍历字典
---------------
