# Python学习

## Python语法
- 在Python中以".py"作为文件扩展名
- Python中缩进必须全部一致
- Python没有声明变量的命令（不像Java，C++那么严格）
- Python中使用注释为“#”符号（单行注释）
- Python中使用"""作为"""三行注释

## Python变量

创建变量

变量是存放数据值的容器。

与其他编程语言不同，Python 没有声明变量的命令。

首次为其赋值时，才会创建变量。

```python
x = 5
y = "John"
print(x)
print(y)
```

变量名称

变量可以使用短名称（如 x 和 y）或更具描述性的名称（age、carname、total_volume）。

Python 变量命名规则:

- 变量名必须以字母或下划线字符开头
- 变量名称不能以数字开头
- 变量名只能包含字母数字字符和下划线（A-z、0-9 和 _）

```python
# 合法的变量名:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# 非法变量名:
2myvar = "John"
my-var = "John"
my var = "John"
```

向多个变量赋值
Python 允许在一行中为多个变量赋值:

```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```

您可以在一行中为多个变量分配相同的值:

```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

输出变量
Python 的 print语句通常用于输出变量。

如需结合文本和变量，Python 使用 + 字符:

```python
x = "awesome"
print("Python is " + x)
```
全局变量
在函数外部创建的变量（如上述所有实例所示）称为全局变量。

全局变量可以被函数内部和外部的每个人使用。

```python
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
```

如果在函数内部创建具有相同名称的变量，则该变量将是局部变量，并且只能在函数内部使用。具有相同名称的全局变量将保留原样，并拥有原始值。

```python
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
```

global 关键词
通常，在函数内部创建变量时，该变量是局部变量，只能在该函数内部使用。

要在函数内部创建全局变量，您可以使用global关键字。

```python
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

另外，如果要在函数内部更改全局变量，请使用 global 关键字。

```python
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

## Python数据类型

Python 数据类型
内置数据类型
在编程中，数据类型是一个重要的概念。

变量可以存储不同类型的数据，并且不同类型可以执行不同的操作。

在这些类别中，Python 默认拥有以下内置数据类型:

文本类型:	str
数值类型:	int, float, complex
序列类型:	list, tuple, range
映射类型:	dict
集合类型:	set, frozenset
布尔类型:	bool
二进制类型:	bytes, bytearray, memoryview

获取数据类型
可以使用 type() 函数获取任何对象的数据类型:

```python
x = 5
print(type(x))
```

设置数据类型
在 Python 中，当您为变量赋值时，会设置数据类型:

|实例|	数据类型	|
|----|----|
|x = "Hello World"	|str	|
|x = 20	|int	|
|x = 20.5	|float	|
|x = 1j	|complex	|
|x = ["apple", "banana", "cherry"]|	list|	
|x = ("apple", "banana", "cherry")	|tuple	|
|x = range(6)	|range	|
|x = {"name" : "John", "age" : 36}	|dict	|
|x = {"apple", "banana", "cherry"}|	set	|
|x = frozenset({"apple", "banana", "cherry"})|	frozenset	|
|x = True	|bool	|
|x = b"Hello"|	bytes	|
|x = bytearray(5)|	bytearray	|
|x = memoryview(bytes(5))	|memoryview|


设定特定的数据类型
如果希望指定数据类型，则可以使用以下构造函数:

|实例	|数据类型|	
|----|----|
|x = str("Hello World")	|str	|
|x = int(20)	|int|

## Python数值类型

类型转换
可以使用 int(), float(), complex()方法从一种类型转换为另一种类型

```python
x = 1
y = 2.8
z = 1j

# 从Int装欢为float
a = float(x)

# 从浮点数转换为整数
b = int(y)

# 从 int 转换为 complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```

> 注释: 无法将复数转换为其他数字类型。

随机数
Python 没有 random() 函数来创建随机数，但 Python 有一个名为 random 的内置模块，可用于生成随机数:

```python
import random

print(random.randrange(1, 10))
```

## Python字符串
字符串字面量
python 中的字符串字面量由单引号或双引号括起。

'hello' 等同于 "hello".

可以使用 print() 函数显示字符串字面量:

```python
print("Hello")
print('Hello')
```

