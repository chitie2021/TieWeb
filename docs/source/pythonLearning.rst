Python学习
=====

.. _introduction:

Python语言概述
----------------

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
---------------

 - 变量的命名和使用：

  变量名只能包含字母、数字和下划线。变量名能以字母或下划线打头，但不能以数字打头。例如可以是message_1，但不能是1_message。

  变量名不能包含空格，但能使用下划线来分隔其中的单词。例如变量名 greeting_message可行，但是 greeting message会引发错误。

  同时不能将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，比如print。

  变量名应简短又有描述性。例如name比n好。

  慎用小写字母l和大写字母O，因为他们可能被人看错成数字1和0。

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

这里的f是format的简写，是Python通过把花括号内的变量替换为其值来设置字符串的格式。

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

空白很重要，因为你经常需要比较两个字符串是否相同。比如，在用户登录网站时检查其用户名。Python中删除空白的命令包括rstrip()、lstrip()和strip()。

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

   注意：索引是从 0 开始而不是从 1 开始。同时，最后一个元素可以用 -1 来索引。



