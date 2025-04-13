[toc]

# 简介

## 备注与特点

- 备注："#"表示一行注释**'''或"""表示多行注释**
- 分行代表一个语句的结束
- 对大小写敏感
- 赋值相当于用的是指向，此时一个变另一个也变
- **定义常量：全大写**
- 如果你在该长度下写不完你的代码，可以使用连接 符 \（反斜线）。把它放在一行的结束位置

## 类、对象、方法、函数和属性的区别和理解

- 类： 采用 Class 作为关键字进行定义的代码块，表示的是一种类别

- **对象： 实例化之后的类，对类中的形参进行了赋值，赋予其真正的含义或数值**

- **方法： 使用 def 作为关键词，定义在类内的函数**

  > **方法是依附于一个类或对象（例如列表）的，通常由对象来调用（需要先有对象），而函数则可以直接由模块调用。**

- **函数： 使用 def 作为关键词，但是没有在类内进行定义，即 定义在类外**

  > **函数不需要一个对象，可以直接输入参数使用，不用对象**

- **属性： 类内的称呼，其实就是类内的变量，同一个类内的不同方法内的变量都是这个类的属性，也就是这个类的变量**

下面这些是重点，请仔细看，多看几遍，只要你能看懂下面这句话，也就理解了这些混淆概念的区别了！

- 主要区别【函数与方法】：

  | 函数的调用        | 方法的调用        | 属性的使用      |
  | ----------------- | ----------------- | --------------- |
  | **库名.函数名()** | **对象.方法名()** | **对象.属性名** |

  > 因此**函数和方法都有括号（）**
  >
  > 而**属性就没有括号（）**

```python
定义一个类
class Person:
    num=1   # 类的属性，使用前需要对其进行声明，否则会报错
    print("您实例化了Person类，初始化的num=",num)
    #定义一个实例属性
    def __init__(self,model):
        self.model=model
    def setName(self,name):
        self.name=name       # 第一个内部是类内部的属性
    def getName(self):
        return self.name
    def count(self):
        self.num+=1   # 使用之前已经对其进行了声明
 上面的三个函数在类的内部所以叫做方法，而对于 setName 方法下面的 变量name, count方法下面的变量num ，我们都可以称之为 类 Person 下面的属性，而类在进行使用时，我们需要对其进行实例化，才能使用这些属性


定义了一个类之后要实例化才能使用
Person类的实例化
p=Person()  

访问类属性
print(p.num)

访问实例属性
print(p.model)
虽然两者都是属性，但一个是类的属性，另一个是实例的属性，生效的范围应该不一样

 调用setName和getName方法
p.setName("小猴")
print(p.getName())
 调用实例方法
p.count()
```

> 当我们不调用count方法时，可以发现其下面的num属性值和初始化的num值1保持一致，num=1保持不变；
> 当我们首先调用count方法时，然后再查看count方法下的num属性时，其值就发生了改变，此时有num=2；
> 当我们第二次调用count方法时，我们可以发现其下面的num属性值其实时是将上次调用之后的运算结果num=2作为初始值进行了运算，得到了此次的运算结果。
>
> 
>
> **这说明当类被实例化之后，类内的代码会被执行，但是其内部的方法在没有被调用之前不会被执行，方法中的属性也不会发生改变，而当方法被调用之后，方法内部的属性值也会发生相应的改变，改变之后的属性值会传递到整个类内，当再次进行调用该类的方法时，其属性的初始值是上次运算之后的属性值结果。**

## Jupyter Notebook快捷键

> 类似于vim

- **在当前单元格下方新建一个单元格：`b`**
- 在当前单元格上方新建一个单元格：`a`
- 运行当前单元格：`shift + enter`
- **删除当前单元格：`dd`**
- **复制当前单元格：`c`**
- **粘贴复制了的单元格：`v`**
- **剪切当前单元格：`x`**
- **查找与替换当前单元格的内容：`f` (ps: 这个快捷键在重构代码时非常好用）**
- **设置当前单元格为Markdown：`m`**
- **查看所有快捷键：`h`** **查看快捷键的快捷键是Jupyter Notebook里一大妙笔，忘记了快捷键就可以查看**

## 查看命令帮助

```
#执行以下命令
命令?
```

# 语法与应用

## 数据类型

- 基本数据类型

  - 数字类型（整数、浮点数、复数）、布尔类型

    | 进制 | 引导符号 | 表示 |
    | :--: | :------: | :--: |
    |  二  |  0B或0b  | 0b10 |
    |  八  |  0O或0o  | 0o23 |
    | 十六 |  0X或0x  | 0x13 |

    

- 组合数据类型

  - 字符串、元组、列表、集合、字典

## 选择结构

```python
if :
    
elif :
    
else:
    
```

> for语句和while语句也能使用else



## 导入库

> #### Python语言功能之所以强大，其中很重要的原因之一是它有很多标准模块可以调用，也有很多第三方模块可以调用，调用方法主要有四种： 
>
> (1) import 库名，引用函数时，使用库名.函数名
>
> (2) import 库名 as 别名，引用函数时，使用别名.函数名
>
> (3) **from 库名 import 函数名||\***，引用函数时，直接函数名
>
> (4) **from 库名 import 函数名 as 别名**，引用函数时，可以使用别名来使用函数



| 操作符 |     描述     |
| :----: | :----------: |
|  x//y  | x与y的整数商 |
|  x**y  |   x的y次幂   |

> x**y相当于pow(x,y)

## 格式化输出

### 方式1：%

> 类似于c的格式化方法

```python
s = 'hello, %s, %d!' % ('python', 2018)
print(s)
```

### 方式2：f"{}"

```python
print(f"哈喽{'hello'},世界{'world'}")
print(f"哈喽{'hello':~>15},世界{'world':*^10}")
```

> 以上是用f"{}"的情况下对格式化要求的办法，变量放前面，用冒号分割格式化操作

### 方式3：format

```python
print("这是format{1:*<10,.2f},{0:-^20}".format("hello","world"))
1：表示用*填充占10个字符，左对齐，三位数字一个‘，’，保留两位小数
2：表示用-填充占20个字符，居中对齐
```

## 变量赋值

- 可变对象

  > **表示可以改变对象的数据，并且该对象的地址不会因此改变的对象**
  >
  > **有列表**

- 不可变对象

  > **表示如果改变对象的数据，则对象的地址也会随之改变的对象**。例如各种数据类型的运算

- 小整数对象池

  > 对于**[-5,257)的整数数字，他们都有固定的地址，只要值没变，地址都不会变化**。但是**超出这个范围后的数字，即使值相同，地址也不同**

  ```python
  #值相同，地址不变
  >>> a = 1
  >>> b = 1
  >>> id(a) == id(b)
  True
  #值不同，地址不变
  >>> c = 1000000
  >>> d = 1000000
  >>> id(c) == id(d)
  False
  ```

  

- **特殊操作**

```python
x = 3==3, 5
x=(True,5)。这里是先进行==判断后“x=True,5”符合元组定义，故正常运行

x,y="ab"
x,y=1,2  #等价于x,y=(1,2)
x,y=[1,2]
x,y={1,2}
x,y={1:"x=1",2:"y=2"}
都可以正常运行，如未说明，字典默认都是键
```

- 运算

  对于有序的同类型的数据类型都可以进行+-*的运算

  > 对于字典与集合无法使用运算

  ```python
  str="ab"
  print(str+'cd')
  list=[1,2]
  print(list+[3])
  tu=1,
  print(tu+(2,))
  ```


## 赋值问题

​	在 Python 中，所有的东西都是对象，每个对象都有一个唯一的 id，你可以认为 id 就是该对象在内存中的地址。当你创建一个变量并赋值，实际上变量只是对那个 id（地址）的引用，指向实际的对象。



​	**当你赋值一个变量给另一个变量时，实际上是复制了对象的地址，也就是说两个变量现在引用的是同一个对象**。这就是为什么改变一个变量的值，另一个变量也会跟着变化，因为它们指向的是同一个对象。例如，对于列表、字典或其他可变对象，会出现这样的情况：

```python
list1 = [1, 2, 3]
list2 = list1  # list2 现在引用的是和 list1 同一个对象
list2.append(4)  # 改变 list2
print(list1)  # 输出: [1, 2, 3, 4]，list1 也跟着变化了
```

> 需要注意，**对于一些不可变的类型（如 int、float、str、tuple 等），因为它们的值是不可变的，所以即使两个变量指向同一个对象，你也不能通过改变一个变量来改变另一个变量的值。**

## 其他

### 三元运算符

```python
value_if_true if condition else value_if_false

a = 10
b = 20
max_value = a if a > b else b
print(max_value)  # 输出：20
```

> 它先检查条件 `condition`，如果条件为真（True），则返回 `value_if_true`；如果条件为假（False），则返回 `value_if_false`。

### input()函数 

​    input() 函数接受一个标准输入数据，返回为 string 类型。

- input输入多个变量

  ```python
  a,b,c=eval(input("输入三个变量，用逗号分割"))
  print(a,b,c)
  ```

  > **这里一定要用eval转换，用int那些会报错**
  >
  > **可以输入整数、浮点数、字符串（需要带引号）**

### eval()函数 

​    eval()函数能够以Python表达式的方式解析并执行字符串，将返回结果输出。如果用户希望输入一个数字，并用程序对这个数字进行计算，可以采用eval(input(<输入提示字符串>))的组合。

# 各种数据结构

## 字符串
- 定义三种方式
  - ''
  
  - ""

  - **'''**
  
    **内容**用用三个单|双引号包起来
  
    **'''**

> **注意区分：注释没有赋值，字符串定义有赋值，都是单双引号都可以**

- 转义字符

  | 转义符  | 意思       |
  | ------- | ---------- |
  | **\\'** | **单引号** |
  | **\\\** | **反斜杠** |
  | **\n**  | **换行**   |
  | **\r**  | **回车**   |
  | **\t**  | **Tab**    |
  | \b      | 退格       |
  | \f      | 换页       |
  | \o??    | 八进制值   |
  | \x??    | 十六进制值 |
  | \e      | 转义       |

- **原始字符串（操作符r）**

  > **r可以使字符串里面就是字符串内容本身，没有转义等**

  ```python
  print(r"hello\\nwww")
  hello\\nwww
  
  print("hello\\nwww")
  hello\nwww
  ```

- **字符串的方法**

| 方法名                             | 描述                                                         | 例子                                 | 返回值                         |
| ---------------------------------- | ------------------------------------------------------------ | ------------------------------------ | ------------------------------ |
| str.title()                        |                                                              |                                      |                                |
| str.upper()                        |                                                              |                                      |                                |
| str.lower()                        |                                                              |                                      |                                |
| rstrip()                           | 删除右边空格                                                 |                                      |                                |
| lstrip()                           | 删左边空格                                                   |                                      |                                |
| strip()                            | 同时去除左右的空格，默认为空格或换行，可以特别指定别的：'\0' | str.strip('左右')                    | 返回原字符串的副本             |
| `split`(*sep=None*, *maxsplit=-1*) | 返回一个由字符串内单词组成的列表，使用 *sep* 作为分隔字符串。**sep**没给的话是**默认是空格**，几个空格都可以。 如果给出了 **maxsplit**，则**最多**进行 **maxsplit** 次拆分。如果给出了 *sep*，则连续的分隔符不会被组合在一起而是被视为分隔空字符串 | '1<>2'.split('<>',1)                 |                                |
| rsplit                             |                                                              |                                      |                                |
| lsplit                             |                                                              |                                      |                                |
| `join`(*iterable*)                 | **返回**一个由 *iterable* （可迭代的对象，如**字符串组成的列表**）中的字符串拼接而成的**字符串**。 如果 *iterable* 中存在任何非字符串值包括`bytes`对象则会引发`TypeError`。 调用该方法的字符串将作为元素之间的分隔。 | ':'.join("2020 09 05 13 54".split()) | '2020:09:05:13:54'             |
| `replace`(*old*, *new*[, *count*]) | 返回字符串的副本，其中出现的**所有**子字符串 *old* 都将被替换为 *new*。 如果给出了可选参数 *count*，则只替换前 *count* 次出现。 | '111'.replace('1','2',1)             |                                |
| `count`(*sub*[, *start*[, *end*]]) | 返回子字符串 *sub* 在 [*start*, *end*] 范围内非重叠出现的次数，默认是整个字符串。 可选参数 *start* 与 *end，* 会被解读为切片表示法。 | 'www.example.com'.count('w',1,7)     | 2                              |
| `find`(*sub*[, *start*[, *end*]])  | 返回子字符串 *sub* 在 `s[start:end]` 切片内被找到的最小索引  | 'www.example.com'.find('w',1,7)      | 如果 *sub* 未被找到则返回 `-1` |
| `isalpha`()                        | 全是字母                                                     |                                      |                                |
| `isdecimal`()                      | 全是数字                                                     |                                      |                                |
| `chr`(*i*)                         | 返回 Unicode 码位为整数 *i* 的字符的字符串格式               | chr(97)                              | a                              |
| `ord`(*c*)                         | 对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。 | ord('a')                             | 97                             |

> upper这些是字符串的方法，而在oracle中这些是函数

- 字符串中使用变量(f)

  ```python
  first = "ada"
  last = "lovelace"
  full_name = f"{first} {last}"  
  print(full_name)    #等价于print("{} {}".format(first,last))
  
  -------------
  bicycles = ['trek', 'cannondale', 'redline', 'specialized']
  message = f"My first bicycle was a {bicycles[0].title():*}."  #左边是变量，右边是填充规则
  print(message)
  ```

  > f是format（设置格式）的简写

  

## 列表

列表也可以像字符串一样乘*与相加+的操作：

```python
x = [1,2,3]
print(x * 3)
=[1,2,3,1,2,3,1,2,3]

x = [1,2,3]
print(x+[4])  #等价于x+=4,  后print(x)
=[1, 2, 3, 4]

l = [6,6,6]
print(sum(l,2))
=20   #是sum(l)+2，不是sum(l[:2])
```

> **注：一切有序的结构都可以进行乘*与＋的操作**
>
> print(*列表名)可以去掉括号

```python
l=[1,2]
print(l[2:])
=[]  #列表索引访问若无数据则是空列表
l[len(l):len(l)]=[x]  #等价于l.append(x)。这里表示索引为-1的后一位数据设置为x
此时l=[1,2,x]
```

- 列表方法总结

| 方法名                            | 描述                                                         | 例子                    | 返回值     |
| --------------------------------- | ------------------------------------------------------------ | ----------------------- | ---------- |
| append()                          | 末尾添加                                                     |                         |            |
| extend()                          | 末尾添加列表                                                 |                         |            |
| insert(i,x)                       | 在第i个位置插入x                                             |                         |            |
| pop(i)                            | **删除下标为i的元素，默认为末尾**                            |                         |            |
| remove(x)                         | 删除第一个值为x的元素，没有valueerror                        |                         |            |
| clear()                           | 清除所有                                                     |                         |            |
| 列表内置方法                      |                                                              |                         |            |
| copy()                            | 等价于list[:]或str[:]。不会对原本数据进行修改                |                         |            |
| count()                           |                                                              |                         |            |
| index(x[, i[, j]])                | *x* 首次出现项的索引号（范围[i,j)），没有找到时ValueError。不确定是否存在时，先使用in进行检查。 |                         |            |
| len()                             |                                                              |                         |            |
| 列表专属方法                      |                                                              |                         |            |
| reverse()                         | 将列表中的元素逆序，就地反转。若不想使列表，那就[::-1]       |                         | 没有返回值 |
| sort(*key=None*, *reverse=False*) | 此方法会对列表进行升序排序，只使用 `<` 来进行各项间比较。*reverse* 值默认为False。 如果设为 `True`，则每个列表元素将按降序进行排序。*key* 指定带有一个参数的函数，用于从每个列表元素中提取比较键，(例如 `key=str.lower`)，此时会先将每个元素转换成小写再比较 | list.sort(reverse=True) | none       |
|                                   |                                                              |                         |            |
| reversed（）函数                  | 反转                                                         |                         |            |
| sorted()函数                      | 返回一个新的排序列表。key参数对特定段进行排序                |                         |            |

### 列表切片

> 列表切片的通用格式为：列表名[start:end :step],step表示步长，注意切片的结果不包含结束索引位置，左闭右开，即**不包含最后的一位**
>
> 可以[:]表示复制一整份表出来，对其修改不会影响原来的列表
>
> 当start参数用-n表示的n超过列表长度时，会从第一个元素开始
>
> 如：
>
> - ### x = [1,2,3]
>
> - ### x[-5:]
>
> - =[1,2,3]

### 列表解析（列表推导式）

> 列表解析 将for 循环和创建新元素的代码合并成一 行，并自动附加新元素。

```python
squares = [value**2 for value in range(1, 11)]
print(squares)
---结果
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list1=[3,5,1,2,6,8,7,7,6,5,4,9,3,2]
new_list=[]
[new_list.append(i) for i in list1 if i not in new_list]
print(new_list)
---结果
[3, 5, 1, 2, 6, 8, 7, 4, 9]
```



## 元组

> 不可改变的有序列表，**不可改变的只是地址，若不改变地址的情况下改变元素则是可以的**
>
> 可以通过id函数判断地址
>
> 定义：a1，
>
> 定义至少要有**一个逗号，括号可以省略**
>
> 修改元组只能重新定义
>
> **用*元祖名也可以去掉（）括号**

- 特殊操作

  ```python
  t=([1,2],3,4)
  t[0].append(3)
  print(t)
  #结果t=([1,2,3],3,4)
  ```

  > 元祖不可修改，但要是元祖的某一成分是列表，则该列表可以修改。原因在于对列表元素的修改不会影响列表的地址，对于元祖来说，只要地址没有变化，就算作没有改变。



## 集合

> 集合（set）是一种可迭代的、无序的、不能包含重复元素的容器类 型的数据。
>
> 空集合必须用set()创立，因为{}表示空字典

### 增加集合元素

> **add（elem）：添加元素，如果元素已经存在，则不能添加，不会 抛出错误。**
>
> None

### 删除集合元素

> **remove（elem）：删除元素**，如果**元素不存在，则抛出错误**。
> clear（）：清除集合。
>
> 返回None

### 交集并集差集

> 交：set1|set2
>
> 并：set1&set2
>
> 差：set1-set2

### 集合推导式

```python
{expression for expression in iterable }
>>> a_set = {number for number in range(1,6) if number % 3 == 1}
>>> a_set
{1, 4}
```





## 字典

> 字典 是一系列键值对 。每个键 都与一个值相关联，你可使用键来访问相关联的值。与键相关联的值可以任何python对象
>
> dict()函数：转换成字典类型
>
> ### **x in d表示判断x是否是字典d中的键**

### 定义

```python
alien_0 = {'color': 'green', 'points': 5}
```

> 键和值之间用冒号分隔，而键值对之间用逗号分隔，每个逗号的左边是字典中的一项
>
> 字典用{}花括号包着

### 访问字典中的值

1. 直接访问

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
```

> 指定字典名和放在**方括号**内的键来访问值
>
> **问题：键不存在时报错**
2. get()方法

   ```python
   alien_0 = {'color': 'green', 'speed': 'slow'}
   point_value = alien_0.get('111', 'No point value assigned.')
   print(point_value)
   ```

   > 方法get() 的**第一个参数用于指定键**，是必不可少的；**第二个参数为指定的键不存 在时要返回的值，是可选**的：

### 遍历字典

```python
 user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key in user_0:
    print(key)  #默认都是访问字典的键
    
for key, value in user_0.items():
 	print(f"\nKey: {key}")
 	print(f"Value: {value}")
```

> 方法items() （见❶），它返回一个键值对**列表**

| 方法     | 作用                                 | 使用          |
| -------- | ------------------------------------ | ------------- |
| items()  | 返回一个字典键型的所有键名和对应的值 |               |
| keys()   | 返回一个字典键型的所有键名           | 字典.keys()   |
| values() | 返回一个字典键型的所有值             | 字典.values() |

### 用列表对字典排序

#### 通过键来对字典排序

```python
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
print(sorted(list(user_0.items()))
```

#### 通过值来对字典排序

> **sorted(列表,key=lambda x:x[1])**
>
> **x[1]：表示列表每个元素取出索引1的数据作为排序关键字**
>
> **默认为x[0]**

```python
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
user=list(user_0.items())
print(sorted(user,key=lambda x:x[0]))
print(sorted(user,key=lambda x:x[1]))
```

> 表示传进去每一项，每一项返回对应的下标元素
>
> x[0]表示按username排序
>
> x[1]表示按efermi排序

#### 对键值对进行排序

```python
d={1: 3, 4: 5, 6: 6, 7: True, 2: 10}

>>> sorted(d.items(),key=lambda d:d[0])
[(1, 3), (2, 10), (4, 5), (6, 6), (7, True)]
>>> sorted(d.items(),key=lambda d:d[0],reverse=True)
[(7, True), (6, 6), (4, 5), (2, 10), (1, 3)]
>>> sorted(d.items(),key=lambda d:d[1])
[(7, True), (1, 3), (4, 5), (6, 6), (2, 10)]
>>> sorted(d.items(),key=lambda d:d[1],reverse=True)
[(2, 10), (6, 6), (4, 5), (1, 3), (7, True)]
```

### 字典推导式

> {key: value for (key, value) in iterable}

```python
d = {key: value for (key, value) in zip('0123456789',range(10))}

d = dict(zip('0123456789',range(10)))
```

> 上一个为推导式，后面的使用构造函数，结果一样



# 函数

def

> **将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修 改都是永久性的**。原因就是传递列表相当于给了列表的地址进去
>
> **禁止函数修改列表的方式：切片表示法[:] 创建列表的副本**

## 传递参数

### 指定参数、返回值类型

使用冒号:和箭头->

```python
def plus(a: int, b: int) -> int:
    """
    :param a: a number
    :param b: a number
    :return: a+b
    """
    return a + b
 
print(type(plus(3, 4)))
print(plus(3, 4))
```

结果：

> <class 'int'>
> 7

### 局部变量变全局参数

global让变量使用全局变量

```python
x=0
def x():
    global x
    x=1
x()
print(x)
```

### 传递默认值参数

> **在Python的函数调用中，位置参数必须在所有的关键字参数之前**
>
> ```python
> def f(x, y = 0, z = 0):‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬
>       pass
> f(x = 1, 2)
> ```
>
> 会报错
>
> ***注意*：** 默认值只会**执行一次**。这条规则在默认值为**可变对象**（列表、字典以及大多数类实例）时很重要。比如，下面的函数会存储在后续调用中传递给它的参数:

```python
def f(a, L=[]):
    L.append(a)
    return L
 
print(f(1))
print(f(2))
print(f(3))

结果
[1]
[1, 2]
[1, 2, 3]
-------------------------
如果你不想要在后续调用之间共享默认值，你可以这样写这个函数:
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
结果为
[1]
[2]
[3]
```

> 注意：有默认值的参数必须在无默认值参数的后面

> 可写为：

> def power(n, x=2):
>     return x ** n
> 对于包含 参数有默认值的 函数，而且已经调用了，不易改动，不方便添加不含默认值的参数，保证健壮性，只能添加默认值。

> power(x,n=2)添加y参数时power(x,n=2,y)是不对的，只能是power(x,n=2,y=None)，y可以赋值为其他默认值。



> 可变参数位置参数和默认参数使用时也要注意顺序：位置参数、默认参数或`*args`、`**kwargs`
>
> 即def func(a,c=1,*b,**d):
>
> 或者def func(a,*b,c=1,**d):

### 传递任意数量的实参

> 有时候，预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中 收集任意数量的实参

```python
def make_pizza(*args,**kwargs):
	for i in args:
        print(i)
make_pizza(1,2,3)
```

> 形参名*args中的星号让Python创建一个名为toppings 的**空元组，并将收 到的所有值都封装到这个元组中**
>
> **`kwargs`的类型是字典**
>
> **`*args`必须写在`**kwargs`前面**

### keyword-only参数

**keyword-only参数**是 Python3 中新加入的特性，比较不多见。

定义时有一个单独的*号，其实这也只是一种规定，*号看上去像是一个参数，其实它不占参数个数，是给解释器看的。规定`*`号后面的参数，能且只能用`key=value`的方式传入

```python
def func(a,b,*,c,d):
    print(a,b,c,d)
func(1,2,c=3,d=4)
```





## 将函数存储在模块中
> 模块的独立文件中，再将模块导入到主程序中。import 语句允许在当前运行的程序文件中使用模块中的代码。
> 其中模块是.py的文件

```python
pizza.py
def make_pizza(i="这是形参定义默认值"):  #该形参若没有参数，则默认为该字符串
  print("这是定义的模块")

make_pizza.py
import pizza
pizza.make_pizza()
```

## lambda匿名函数

lambda 形参:返回值

```python
def x(a,b):
    return a+b
print(x(1,2))
--3
等价于
x=lambda a,b:a+b
print(x(1,2))
```

> 表示传进去两个值，返回两值之和

- 应用：对字典排序

  ```python
  gdpdict={"美国":1,
          "加拿大":2
          }
  gdplist=list(gdpdict.items())
  print(f"原本{gdplist}")
  print("按list[0]排序")
  blist=sorted(gdplist,key=(lambda x:x[0]))
  print(blist)
  print("按list[1]排序")
  clist=sorted(gdplist,key=(lambda x:x[1]))
  print(clist)
  ```


## sorted函数及匿名函数的使用

sorted(iterable, cmp=None, key=None, reverse=False)

> - iterable -- 可迭代对象。
> - cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
> - key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
> - reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。

- 关键参数key

  [`list.sort()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort) 和 [`sorted()`](https://docs.python.org/zh-cn/3/library/functions.html#sorted) 都有一个 *key* 形参用来指定在进行比较前要在每个列表元素上调用的函数（或其他可调用对象）。

  - 例如，下面是一个不区分大小写的字符串比较：

  ```python
  >>> sorted("This is a test string from Andrew".split(), key=str.lower)
  ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
  ```

  *key* 形参的值应该是个函数（或其他可调用对象），它接受一个参数并返回一个用于排序的键。 这种机制速度很快，因为对于每个输入记录只会调用一次键函数。

  一种常见的模式是使用对象的一些索引作为键对复杂对象进行排序。

  - 例如：

  ```python
  >>> student_tuples = [
  ...     ('john', 'A', 15),
  ...     ('jane', 'B', 12),
  ...     ('dave', 'B', 10),
  ... ]
  >>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
  [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
  ```

## sorted函数与operator模块函数的使用

- Operator 模块函数

上面显示的键函数模式非常常见，因此 Python 提供了便利功能，使访问器功能更容易，更快捷。 [`operator`](https://docs.python.org/zh-cn/3/library/operator.html#module-operator) 模块有 [`itemgetter()`](https://docs.python.org/zh-cn/3/library/operator.html#operator.itemgetter) 、 [`attrgetter()`](https://docs.python.org/zh-cn/3/library/operator.html#operator.attrgetter) 和 [`methodcaller()`](https://docs.python.org/zh-cn/3/library/operator.html#operator.methodcaller) 函数。

> itemgetter()返回一个使用操作数的 [`__getitem__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getitem__) 方法从操作数中获取 *item* 的可调用对象。 如果指定了多个条目，则返回一个查找值的元组。 例如：
>
> - 在 `f = itemgetter(2)` 之后，调用 `f(r)` 将返回 `r[2]`。
> - 在 `g = itemgetter(2, 5, 3)` 之后，调用 `g(r)` 将返回 `(r[2], r[5], r[3])`。

使用这些函数，上述示例变得更简单，更快捷：

```python
>>> from operator import itemgetter, attrgetter
>>> sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

>>> sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

Operator 模块功能允许多级排序。 例如，按 *grade* 排序，然后按 *age* 排序：

```python
>>> sorted(student_tuples, key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

>>> sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```

- 排序稳定性和排序复杂度

排序保证是 [稳定](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability) 的。 这意味着当多个记录具有相同的键值时，将保留其原始顺序。

```python
>>> data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
>>> sorted(data, key=itemgetter(0))
[('blue', 1), ('blue', 2), ('red', 1), ('red', 2)]
```

注意 *blue* 的两个记录如何保留它们的原始顺序，以便 `('blue', 1)` 保证在 `('blue', 2)` 之前。

这个美妙的属性允许你在一系列排序步骤中构建复杂的排序。例如，要按 *grade* 降序然后 *age* 升序对学生数据进行排序，请先 *age* 排序，然后再使用 *grade* 排序：

```python
>>> s = sorted(student_objects, key=attrgetter('age'))     # sort on secondary key
>>> sorted(s, key=attrgetter('grade'), reverse=True)       # now sort on primary key, descending
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

## 内置函数

| **abs()**     | delattr()   | hash()       | memoryview() | set()          |
| ------------- | ----------- | ------------ | ------------ | -------------- |
| all()         | dict()      | help()       | min()        | setattr()      |
| any()         | dir()       | hex()        | next()       | slicea()       |
| ascii()       | divmod()    | **id()**     | object()     | sorted()       |
| bin()         | enumerate() | input()      | oct()        | staticmethod() |
| bool()        | **eval()**  | int()        | open()       | str()          |
| breakpoint()  | exec()      | isinstance() | ord()        | sum()          |
| bytearray()   | filter()    | issubclass() | pow()        | super()        |
| bytes()       | float()     | iter()       | print()      | tuple()        |
| callable()    | format()    | len()        | property()   | type()         |
| chr()         | frozenset() | list()       | range()      | vars()         |
| classmethod() | getattr()   | locals()     | repr()       | zip()          |
| compile()     | globals()   | map()        | reversed()   | __import__()   |
| complex()     | hasattr()   | max()        | **round()**  |                |

> id()python的内置函数可以查看数据的地址，类似于c语言的&访问地址
>
> 帮助手册：
>
> [内置函数 — Python 3.11.5 文档](https://docs.python.org/zh-cn/3/library/functions.html#abs)

- zip()并行迭代

  用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后**返回由这些元组组成的列表**。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同

  ```python
  >>> days = ['Monday', 'Tuesday', 'Wednesday']
  >>> fruits = ['banana', 'orange', 'peach']
  >>> drinks = ['coffee', 'tea', 'beer']
  >>> desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
  >>> for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
  ... print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
  ...
  Monday : drink coffee - eat banana - enjoy tiramisu
  Tuesday : drink tea - eat orange - enjoy ice cream
  Wednesday : drink beer - eat peach - enjoy pie
  ```

  > 通过 zip() 函数对多个序 列进行并行迭代：**zip() 函数在最短序列“用完”时就会停止**

  

- pass函数





# 类

class 类名：

​	def...

​	def...

>类里可以定义很多的函数，在外面使用就叫做使用方法
>
>**类名要首字母大写**
>
>所有的方法都可以self参数，代表的是类本身，在类中引用时都需要，self.属性=...
>
>定义多个实例时，要用不同的名字表示

### 方法\_\_init\_\_() 

> 是一个特殊方法，每当你根据类创建新实例时，Python都会自动运行它
>
> 创建类时，该方法自动运行
>
> \_\_init()\_\_必须要使用self参数

```python
class Dog:
	def __init__(self, name, age):
		"""初始化属性name和age。"""	
		self.name = name
 		self.age = age
	def sit(self):
 		print(f"{self.name} is now sitting.")
 	def roll_over(self):
 		print(f"{self.name} rolled over!")
```

上述定义的类的使用

```python
dog=Dog("名字","19")
print(dog.name,dog.age)
dog.sit()
dog.roll_over()
```

### 继承

> 一个类继承另一个类时，将自动获得另一个类的所有属性和方法。 原有的类称为父类 ，而新类称为子类 。
>
> 创建子类时，父类必须包含在当前文件中，且位于子类前面。
>
> 父类也称为超类 （superclass）

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
print(my_tesla.get_descriptive_name())
```

> super() 是一个特殊函数，让你能够调用父类的方法。这行代码让Python调 用Car类的方法__init__()
>
> **super().父类属性()**
>
> 因为子继承了父所以，用子类创建的实例，也可以用父里有而子没有的方法
>
> 当子需要与父不同时，再用def定义相同名字的属性来实现特殊的要求

### 将实例用作属性

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size  #在被用作属性的实例中增加需要的属性
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
class ElectricCar(Car):
     #电动汽车的独特之处。
    def __init__(self, make, model, year):
         #初始化父类的属性。
         #再初始化电动汽车特有的属性。
        super().__init__(make, model, year)
        self.battery = Battery()  #建立新的属性并将新创建的实例作为赋值方
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```

### 导入



# 文件

- 文件可分为文本文件和二进制文件两大类

## 文件常用操作

### 文件的打开

- f=open(file,mode="r",encoding=None,errors=None)

> - file参数 file参数用于表示要打开的文件，可以是字符串或整数。如果file是 字符串，则表示文件名，文件名既可以是当前目录的相对路径，也可以 是绝对路径；**如果file是整数，则表示一个已经打开的文件**。
>
> - encoding参数 encoding用来指定打开文件时的文件编码，**默认是UTF-8编码**，主要用于打开文本文件。
>
> - errors参数 errors参数用来指定在文本文件发生编码错误时如何处理。**推荐erro rs参数的取值为'ignore'，表示在遇到编码错误时忽略该错误，程序会继 续执行，不会退出**。
>
> - mode参数 mode参数用于设置文件打开模式，用字符串表示，例如rb表示以只 读模式打开二进制文件。用于设置文件打开模式的字符串中的每一个字 符都表示不同的含义，对这些字符的具体说明如下。
>
>   - t：以文本文件模式打开文件。
>
>   - b：以二进制文件模式打开文件。
>
>   - r：以只读模式打开文件。
>
>   - w：以只写模式打开文件，不能读内容。如果文件不存在，则创建 文件；如果文件存在，则覆盖文件的内容。
>
>   - x：以独占创建模式打开文件，如果文件不存在，则创建并以写入模式打开；如果文件已存在，则引发FileExistsError异常。
>
>   - a：以追加模式打开文件，不能读内容。如果文件不存在，则创建文件；如果文件存在，则在文件末尾追加。
>
>   - +：以更新（读写）模式打开文件，必须与r、w或a组合使用，才能设置文件为读写模式。 这些字符可以进行组合，以表示不同类型的文件的打开模式，如下表所示。
>
>     > **仅有r+文件不存在时，不能创建文件，而是报错**
>     
>     ![](img/01.png)

```python
f=open("1.txt","rw",encoding="utf-8",errors='ignore')
f.close()
```

> f只是文件地址名，可以任取

### 文件的读写

| 读写方法                                 | 描述                                                         | 例子                       |
| ---------------------------------------- | ------------------------------------------------------------ | -------------------------- |
| read(size=-1)                            | size=-1表示对读取的字符数没有限制，否则**读取指定字符数**    |                            |
| readline(size=-1)                        | 在读取到换行符或文件尾时返回单行字符串 。如果已经到文件尾，则返回一个空字符串 |                            |
| readlines（）                            | 读取文件数据到一个字符串列表中，每一行数据都是列表的一个元素。 | ls=f.readlines()           |
| write（s）                               | 将字符串s写入文件中，并返回写入的字符数。                    |                            |
| writelines（lines）                      | 向文件中写入一个字符串列表。**不添加行分隔符**，因此通常为每一行末尾都提供行分隔符。 |                            |
| seek([offset],origin)                    | 将文件移动到指定位置origin：**0--文件开头**，1--当前位置，2--文件末尾。距离origin位置的偏移量：offset | seek(-1,2) #表尾前一个字节 |
| for i in f:print(i)                      | f是open打开返回的文件地址，此时f[0]对应文件第一行，以此类推。所以这里的操作是输出全文 |                            |
| with open("1.txt","rw") as f:print(f[0]) | 用with语句打开文件，可以避免忘记关闭文件，因为with自动关闭文件 |                            |

```python
f=open("1.txt","rw")
一行读取
f.seek(0)
print(f.readline())
全文读取1
f.seek(0)
print(f.read())
全文读取2
ls=f.readlines()
for i in ls:
    print(i,end="")
全文读取3
f.seek(0)
for i in f:
    print(i,end="")
用with打开文件
with open("1.txt","rw") as f:
    print(f.read())
    
文件的写入
print(f.write("lalala"))
print(f.write(f.readlines()))
f.close()
```

## excel文件操作openpyxl库

> **from openpyxl import Workbook：创建excel文件的导入方式**
>
> **from openpyxl import load_workbook：读写excel文件的导入方式**

- **必备操作：**

  - **wb=Workbook()  #新建excel文件**
  - **ws=wb.worksheets[0]  或者 ws=wb.active      #一般都是用工作簿1**

  | 属性                                | 描述                           | 例子                            |
  | ----------------------------------- | ------------------------------ | ------------------------------- |
  | wb.worksheets                       | 获得所有的工作簿               | worksheets[0]表示工作簿1        |
  | wb.read_only                        | 只读                           |                                 |
  | **ws.append(x)**                    | 在表格中添加一行数据，自动换行 | ws.append([1,2,3,4])            |
  | wb.save("url")                      | 保存文件                       |                                 |
  | **wb=load_workbook("url")**         | 读取url文件                    | wb=load_workbook("d:/1.xsl")    |
  | ws['a-z+1-9'].value                 | 获取单元格的值1                | ws['A1'].value                  |
  | **ws.cell(row=x,column=y).value**   | 获取单元格的值1                | ws.cell(row=1,column=2).value   |
  | ws['A1']=xx                         | 单元格赋值1                    |                                 |
  | **ws.cell(row=x,column=y,value=z)** | 单元格赋值2                    | ws.cell(row=1,column=1,value=1) |
  | **ws.max_row**                      | 获得数据占的最大行数           |                                 |
  | **ws.max_column**                   | 获得数据占的最大列数           |                                 |
  | ws.cell(row=x,column=y) 或 ws['xx'] | 表示某个单元格                 |                                 |

  ```python
  #遍历所有单元格
  for i in range(ws.max_row):
      for j in range(ws.max_column):
          print(ws.cell(row=i+1,column=j+1).value,end=" ")
  ```


## os库

```python
#列出某个目录下的所有文件及文件夹
import os
file_list=os.listdir(某个目录)
for file in file_list:
    print(file)
```

# 第三方库的使用

## Mysql库

在Python中使用MySQL可以通过以下步骤实现，这里以`mysql-connector-python`库为例：

### 安装MySQL连接库
```bash
pip install mysql-connector-python
```

### 连接MySQL数据库
```python
import mysql.connector

# 建立数据库连接
conn = mysql.connector.connect(
    host="localhost",      # 数据库主机地址
    user="your_username",  # 数据库用户名
    password="your_password",  # 数据库密码
    database="your_database"   # 数据库名称（可选）
)
```

### 创建游标对象
```python
cursor = conn.cursor()
```

### 执行SQL操作
#### 创建表
```python
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255)
    )
""")
```

#### 插入数据（参数化查询防止SQL注入）
```python
sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
values = ("Alice", "alice@example.com")
cursor.execute(sql, values)
conn.commit()  # 提交事务
```

#### 查询数据
```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()  # 获取所有结果
for row in rows:
    print(row)
```

#### 更新数据
```python
sql = "UPDATE users SET email = %s WHERE name = %s"
values = ("new_email@example.com", "Alice")
cursor.execute(sql, values)
conn.commit()
```

#### 删除数据
```python
sql = "DELETE FROM users WHERE name = %s"
values = ("Alice",)
cursor.execute(sql, values)
conn.commit()
```

### 异常处理和资源关闭
```python
try:
    # 执行数据库操作...
except mysql.connector.Error as e:
    print(f"数据库错误: {e}")
    conn.rollback()  # 回滚事务
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("数据库连接已关闭")
```

### 完整示例
```python
import mysql.connector

try:
    # 连接数据库
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="test_db"
    )
    cursor = conn.cursor()

    # 创建表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255)
        )
    """)

    # 插入数据
    insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    user_data = ("Bob", "bob@example.com")
    cursor.execute(insert_query, user_data)
    conn.commit()

    # 查询数据
    cursor.execute("SELECT * FROM users")
    for (user_id, name, email) in cursor:
        print(f"ID: {user_id}, Name: {name}, Email: {email}")

except mysql.connector.Error as err:
    print(f"Error: {err}")
    if 'conn' in locals() and conn.is_connected():
        conn.rollback()
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("Connection closed")
```

### 注意事项
- **参数化查询**：始终使用`%s`占位符避免SQL注入。
- **事务管理**：执行写操作后需调用`conn.commit()`提交事务。
- **资源释放**：操作完成后关闭游标和连接。
- **错误处理**：使用`try-except`块捕获数据库操作异常。
- **字符编码**：可在连接时添加`charset="utf8mb4"`参数支持中文。

对于其他库如`PyMySQL`，用法类似，只需将`mysql.connector`替换为`pymysql`，连接方式可能略有差异。

```python
import pymysql
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    db="test",
    charset="utf8mb4"  # 通常需要显式指定字符集
)
```

## Selenium自动化



以下是 Python 中使用 Selenium 的全面指南，涵盖从安装到常用操作的完整语法和示例：

---

### 一、环境准备
#### 1. 安装 Selenium 库
```bash
pip install selenium
```

#### 2. 下载浏览器驱动
- **Chrome**: [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- **Firefox**: [GeckoDriver](https://github.com/mozilla/geckodriver)
- **Edge**: [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- **Safari**: 内置（需启用远程自动化）

将驱动文件放在：
- Windows: 系统 `PATH` 路径或项目目录
- macOS/Linux: `/usr/local/bin` 或指定路径

---

### 二、基础用法
#### 1. 启动浏览器
```python
from selenium import webdriver

# Chrome 示例
driver = webdriver.Chrome()  # 驱动在 PATH 中
# 或指定驱动路径
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Firefox 示例
driver = webdriver.Firefox()

# 无头模式（无界面运行）
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
```

#### 2. 打开网页
```python
driver.get("https://www.example.com")
```

#### 3. 关闭浏览器
```python
driver.quit()  # 完全关闭
# 或
driver.close()  # 关闭当前标签页
```

---

### 三、元素定位
Selenium 提供 **8 种定位方式**，常用方法如下：

#### 1. 通过 ID
```python
element = driver.find_element_by_id("element_id")
```

#### 2. 通过 Name
```python
element = driver.find_element_by_name("username")
```

#### 3. 通过 Class Name
```python
element = driver.find_element_by_class_name("btn-primary")
```

#### 4. 通过 Tag Name
```python
element = driver.find_element_by_tag_name("input")
```

#### 5. 通过 Link Text
```python
element = driver.find_element_by_link_text("点击这里")
```

#### 6. 通过 Partial Link Text
```python
element = driver.find_element_by_partial_link_text("登录")
```

#### 7. 通过 XPath
```python
element = driver.find_element_by_xpath("//div[@class='header']/a[1]")
```

#### 8. 通过 CSS Selector
```python
element = driver.find_element_by_css_selector("input.form-control")
```

---

### 四、元素操作
#### 1. 输入文本
```python
element.send_keys("Hello Selenium")
```

#### 2. 点击元素
```python
element.click()
```

#### 3. 清除输入框
```python
element.clear()
```

#### 4. 获取元素属性
```python
text = element.text
value = element.get_attribute("value")
class_name = element.get_attribute("class")
```

---

### 五、浏览器操作
#### 1. 窗口控制
```python
# 最大化窗口
driver.maximize_window()

# 设置窗口尺寸
driver.set_window_size(1024, 768)

# 前进/后退
driver.forward()
driver.back()

# 刷新页面
driver.refresh()
```

#### 2. 获取页面信息
```python
title = driver.title
current_url = driver.current_url
page_source = driver.page_source
```

---

### 六、等待机制
#### 1. 强制等待（不推荐）
```python
import time
time.sleep(3)
```

#### 2. 隐式等待（全局等待）
```python
driver.implicitly_wait(10)  # 最多等10秒
```

#### 3. 显式等待（推荐）
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "dynamic_element"))
)
```

---

### 七、表单与下拉菜单
#### 1. 处理下拉选择框
```python
from selenium.webdriver.support.select import Select

select = Select(driver.find_element_by_id("country"))
select.select_by_visible_text("China")  # 通过文本选择
select.select_by_value("cn")  # 通过value属性选择
select.select_by_index(1)  # 通过索引选择
```

#### 2. 单选/复选框
```python
checkbox = driver.find_element_by_css_selector("input[type='checkbox']")
if not checkbox.is_selected():
    checkbox.click()
```

---

### 八、高级操作
#### 1. 执行 JavaScript
```python
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
element = driver.execute_script("return document.getElementById('element_id');")
```

#### 2. 文件上传
```python
file_input = driver.find_element_by_css_selector("input[type='file']")
file_input.send_keys("/path/to/file.txt")
```

#### 3. 处理弹窗
```python
alert = driver.switch_to.alert
alert.accept()  # 确认
alert.dismiss()  # 取消
text = alert.text  # 获取文本
```

#### 4. 切换窗口/Frame
```python
# 切换窗口
main_window = driver.current_window_handle
for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)

# 切换Frame
driver.switch_to.frame("frame_name")
driver.switch_to.default_content()  # 返回主文档
```

---

### 九、文件下载
```python
# Chrome 下载配置示例
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": "/path/to/download",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)
```

---

### 十、截图与日志
#### 1. 页面截图
```python
driver.save_screenshot("screenshot.png")
element.screenshot("element.png")
```

#### 2. 控制台日志
```python
logs = driver.get_log("browser")
for log in logs:
    print(log)
```

---

### 十一、实战示例：登录操作
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://example.com/login")

# 输入用户名密码
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("testuser")
password.send_keys("password123")

# 点击登录按钮
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.login-btn"))
)
login_button.click()

# 验证登录成功
WebDriverWait(driver, 10).until(
    EC.url_contains("dashboard")
)
print("登录成功！")

driver.quit()
```

---

### 十二、常见问题
#### 1. `ElementNotInteractableException`
- 原因：元素被遮挡或未加载完成
- 解决：使用显式等待确保元素可交互

#### 2. `NoSuchElementException`
- 原因：定位器错误或元素未加载
- 解决：检查定位器，增加等待时间

#### 3. `StaleElementReferenceException`
- 原因：元素已从DOM中移除
- 解决：重新定位元素

---

### 十三、最佳实践
1. **使用显式等待** 代替 `time.sleep()`
2. **优先使用 CSS Selectors**（比 XPath 更快）
3. **封装常用操作** 为独立函数或类
4. **配置日志记录** 方便调试
5. **结合 Page Object 模式** 提高代码可维护性

---

通过以上内容，你可以覆盖 Selenium 在 Python 中的 90% 以上使用场景。具体问题可结合浏览器开发者工具（F12）分析元素结构和网络请求。

# 数据结构

# 数据分析

> 主要是对python第三方库的应用
>
> ①numpy②matplotlib③pandas

## numpy

> **学习目标**
>
> - Numpy创建多维数组和生成随机数的方法
> - 数组的索引与变换
> - Numpy中数组矩阵的运算及通用函数的基本使用方法
> - Numpy读写文件的方法和常用的统计分析函数

### 准备工作

```python
 显示所有变量
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

```python
 显示最后一个变量
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "last_expr"
```

### numpy的数据类型

| 符号           | 含义                        |
| -------------- | --------------------------- |
| bool           | True和Flase                 |
| inti           | 支持int的32或64位           |
| int8           | 8位的整形(-128~127)         |
| int16          | -32768~32767                |
| int32          | -2 ** 31 ~ 2 ** 31 - 1      |
| int64          | -2 ** 63 ~ 2 ** 63 - 1      |
| uint8          | 8位的整形(0~255)            |
| uint16         | -32768~32767                |
| uint32         | 0 ~ 2 ** 32 - 1             |
| uint64         | 0 ~ 2 ** 64 - 1             |
| float16        | 1位符号位，5位指数位，10位  |
| float32        | 1位符号位，8位指数位，23位  |
| float64、float | 1位符号位，11位指数位，52位 |

> 上面的数字单位是位，例如int默认是4B=int32、float默认是8B=float64

**对于每种类型都有同名的转换函数可以将数据转为某种数据类型的数据。**

```python
import numpy as np
 34.5转为8位整形，即1字节
np.int8(34.5)
 34.5转为布尔值即True或Flase
np.bool(34.5)
```

而许多的NumPy下的函数有可选的参数dtype可以指定数据的类型，类型值。

```python
import numpy as np
np.arange(10, dtype=uint8)
n2=np.arange(7, dtype = 'u2')
n2.itemsize
n2.dtype
```

> ```
> 34
> ```
>
> ```
> True
> ```
>
> ```
> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=uint8)
> ```
>
> ```
> 2
> ```
>
> ```python
> dtype('uint16')
> ```

### NumPy 数组对象 ndarray

> Python 提供了一个array 模块。array 和list 不同，它直接保存数值，和C 语言的一维 数组比较类似。但是由于Python 的array 模块不支持多维，也没有各种运算函数，因此也 不适合做数值运算。NumPy 的诞生弥补了这些不足。NumPy 提供了一种**存储单一数据类型 的多维数组——ndarray**。
>
> 注：**numpy只有两种类型，ndarray和ufunc**。
>
> > ufunc的特点：对整个数组进行操作
>
> numpy中维度称为轴，几维对应的就是几轴；**如二维数组，0轴就是指行，1轴就是指列，轴都是从0开始算的**

- ndarray 内部由以下内容组成：

  • 一个指向数据(内存或内存映射文件中的一块数据)的指针。

  • 数据类型或 dtype，描述在数组中的固定大小值的格子。

  • 一个表示数组形状(shape)的元组，表示各维度大小的元组。形状为(row×col)

-  **数据类型**
  numpy 支持的数据类型比 Python 内置的类型要多很多，基本上可以和C语言的数据类型对应上主要包括int8、int16、int32、int64、uint8、uint16、uint32、uint64、float16、float32、float64

### 创建数组对象

#### 常用函数

| （np.）函数名 | 说明 | 例子 |
| ------ | ---- | ------ |
|**array(object[, dtype, copy, order, subok, ndmin])**|创建一个数组|n2=np.array([[1,2,3,4],[5,6,7,8],[5,6,7,8],[5,6,7,8]])|
|**arange(start[,stop,step])**|像range一样创建数组|**arange(1,10,2)**|
|**loadtxt(fname[, dtype,skiprows, delimiter,usecols,encoding …])**|从文本文件加载数据|peoples = np.loadtxt("data/人口.csv",skiprows=2,delimiter=',',usecols=(range(1,13)),encoding="utf-8")|
| ones(shape[, dtype, order])                                  | 返回给定形状和类型的新数组，并填充为1          | np.ones(100,int).reshape(4,25)                               |
| eye(N[, M, k, dtype, order])                                 | 返回一个二维数组，对角线上有一个，其他地方为零 | np.eye(4)=np.eye(4,4)                                        |
| zeros(shape[, dtype, order])                                 | 返回给定形状和类型的新数组，并用零填充         | np.zeros((2,3,4))                                            |
| diag(v[, k])                                                 | 提取对角线或构造对角线数组                     | np.diag([8,7,6,5])                                           |
| ndarray.T                                                    | 转置数组。                                     |                                                              |
| copy(a[, order])                                             | 返回给定对象的数组副本                         |                                                              |
| linspace(start,stop)                                         | 等差数列                                       | np.linspace(1,99)                                            |
| logspace(start,stop)                                         | 等比数列                                       |                                                              |

#### 数组的常用属性

| （对象.)属性名    | 说明                   | 返回                                    |
| ----------------- | ---------------------- | --------------------------------------- |
| **对象.ndim**     | **返回数组的维度**     | **n维**                                 |
| **对象.shape**    | **返回数组结构**       | **(n,m)，几行几列，几个数就是几维**     |
| **对象.dtype**    | **返回数组类型**       | **dtype('data_type')，type的单位是bit** |
| **对象.size**     | **返回数组元素个数**   | **n个**                                 |
| **对象.itemsize** | **返回数组的元素大小** | **n个byte**                             |

> 修改属性的方式：对象.属性名=要修改的内容
>
> 如：a1.shape=4,2

#### 数组的常用方法

| (对象名.)属性名() | 说明                                  | 例子            |
| ----------------- | ------------------------------------- | --------------- |
| **reshape()**     | 重新修改原数组的shape，不会修改原内容 | a2.reshape(4,2) |

> 方法的使用是对对象而言的，并不是第三方模块

#### 生成随机数数组

**np模块下random函数下的方法**

| （np.random.）函数名                           | 说明                             | 返回                               |
| ---------------------------------------------- | -------------------------------- | ---------------------------------- |
| random(n)                                      | 生成n个[0-1)的小数               | np.random.random(10).reshape(2,5)  |
| rand(shape)                                    | 生成服从**均匀分布**的随机数数组 | np.random.rand(2,3,3)              |
| **randn**(shape)                               | 生成服从**正态分布**的随机数数组 | np.random.randn(3,2)               |
| **randint(left_range,right_range,size=shape)** | 生成给定上下限的随机整数数组     | np.random.randint(1,43,size=[2,5]) |
| seed()                                         | 随机数种子                       |                                    |

#### 纯数学函数

NumPy里提供了很多的数学相关的函数，如下表所示：

| 函数                             | 说明                                                 |
| -------------------------------- | ---------------------------------------------------- |
| np.abs() np.fabs()               | 计算数组各元素的绝对值                               |
| np.sqrt()                        | 计算数组各元素的平方根                               |
| np.square()                      | 计算数组各元素的平方                                 |
| np.log(x),np.log10(x),np.log2(x) | 计算数组各元素的自然对数、10底对数和2底对数          |
| np.ceil(x),np.floor(x)           | 计算数组各元素的ceiling值或floor值                   |
| np.rint(x)                       | 计算数组各元素的四舍五入值                           |
| np.modf(x)                       | 将数据各元素的整数和小数部分以两个独立的数组形式返回 |
| np.cos/cosh/sin/sinh/tan/tanh    | 计算数据各元素的普通型和双典型的三角函数             |
| np.exp(x)                        | 计算数组各元素的指数值                               |

#### numpy函数大全：

| 命令                                            | 说明                                               |
| ----------------------------------------------- | -------------------------------------------------- |
| sort()                                          | 排序**函数**，可以选择排序算法，**有返回值**       |
| a.sort()                                        | 排序**方法**，**无返回值**，原地操作               |
| asarray(a[, dtype, order])                      | 将输入转换为数组                                   |
| ravel(a[, order])                               | 返回一个连续的扁平数组。                           |
| rollaxis(a, axis[, start])                      | 向后滚动指定的轴，直到其位于给定的位置。           |
| swapaxes(a, axis1, axis2)                       | 互换数组的两个轴。                                 |
| diagflat(v[, k])                                | 使用展平的输入作为对角线创建二维数组               |
| tri(N[, M, k, dtype])                           | 在给定对角线处及以下且在其他位置为零的数组         |
| tril(m[, k])                                    | 数组的下三角                                       |
| triu(m[, k])                                    | 数组的上三角                                       |
| copyto(dst, src[, casting, where])              | 将值从一个数组复制到另一个数组，并根据需要进行广播 |
| zeros_like(a[, dtype, order, subok, shape])     | 返回形状与类型与给定数组相同的零数组。             |
| full(shape, fill_value[, dtype, order])         | 返回给定形状和类型的新数组，并用 fill_value 填充   |
| full_like(a, fill_value[, dtype, order, …])     | 返回形状和类型与给定数组相同的完整数组             |
| fromstring(string[, dtype, count, sep])         | 从字符串中的文本数据初始化的新一维数组             |
| ones_like(a[, dtype, order, subok, shape])      | 返回形状与类型与给定数组相同的数组                 |
| empty(shape[, dtype, order])                    | 返回给定形状和类型的新数组，而无需初始化条目       |
| empty_like(prototype[, dtype, order, subok, …]) | 返回形状和类型与给定数组相同的新数组               |
| identity(n[, dtype])                            | 返回标识数组                                       |
| transpose(a[, axes])                            | 排列数组的尺寸                                     |
| concatenate((a1, a2, …)                         | 沿现有轴连接一系列数组。                           |
| stack(arrays[, axis, out])                      | 沿新轴连接一系列数组。                             |
| column_stack(tup)                               | 将一维数组作为列堆叠到二维数组中。                 |
| dstack(tup)                                     | 沿深度方向（ 沿第三轴）按顺序堆叠数组。            |
| hstack(tup)                                     | 水平（ 按列）顺序堆叠数组。                        |
| vstack(tup)                                     | 垂直（ 行）按顺序堆叠数组。                        |
| block(arrays)                                   | 从块的嵌套列表中组装一个 nd 数组。                 |
| split(ary, indices_or_sections[, axis])         | 将数组拆分为多个子数组，作为 ary 的视图。          |
| array_split(ary, indices_or_sections[, axis])   | 将一个数组拆分为多个子数组。                       |
| dsplit(ary, indices_or_sections)                | 沿第 3 轴（ 深度）将数组拆分为多个子数组。         |
| **hsplit**(ary, indices_or_sections)            | **水平**（ 按列）将一个数组**拆分**为多个子数组。  |
| **vsplit**(ary, indices_or_sections)            | **垂直**（ 行）将数组**拆分**为多个子数组。        |
| delete(arr, obj[, axis])                        | 返回一个新的数组，该数组具有沿删除的轴的子数组。   |
| insert(arr, obj, values[, axis])                | 沿给定轴在给定索引之前插入值。                     |
| append(arr, values[, axis])                     | 将值附加到数组的末尾。                             |
| resize(a, new_shape)                            | 返回具有指定形状的新数组。                         |
| trim_zeross(filt[, trim])                       | 修剪一维数组或序列中的前导和 / 或尾随零。          |
| unique(ar[, return_index, return_inverse, …])   | 查找数组的唯一元素。                               |
| flip(m[, axis])                                 | 沿给定轴颠倒数组中元素的顺序。                     |
| fliplr(m)                                       | 左右翻转数组。                                     |
| flipud(m)                                       | 上下翻转阵列。                                     |
| roll(a, shift[, axis])                          | 沿给定轴滚动数组元素。                             |
| rot90(m[, k, axes])                             | 在轴指定的平面中将阵列旋转 90 度。                 |

### 索引访问数组

- 一维度

```python
a=np.arange(1,10)
整数作为下标访问，分别访问0和5
a[[0,5]]    #只能用列表，不能元组，访问了索引0和5的元素，共两个，而不是切片
步长为负数时，切片的开始下标必须大于结束下标（也可以不，只是没数据，不报错）
a[-1::-2]
```

- **二维度**

  **每个维度用逗号隔开**，而每一个维度里都可以使用切片，**只能省略第二个维度，不能省略第一个维度**

  ```python
  a2=np.arange(1,21).reshape(4,5)
  #二维数组只有一个下标索引代表行
  a2[1]
  #索引访问第0行的第3和第4列
  a2[0,3:]
  #索引第2和第3行的3-4列
  a2[2:,3:]
  #索引第2列
  a2[:,2:3]
  #从两个序列对应位置取出整数组成下标索引
  a2[0:3,1:4]
  a2[[0,1,2],[1,2,0]]  #错误的：a2[[0,1,2],[1,2]]
  #索引第2，4行中的第0，2，3列（不连续的列使用元组表示）
  a2[2:5:2,(0,1,2)]
  ```

- 用布尔数组来索引

  ```python
  a2=np.arange(1,21).reshape(4,5)
  a2[[True,False,True,False],2:4]  #等价于a2[[::2],2:4]
  ```
  
  > **布尔索引常用函数**
  >
  > | 命令                                         | 说明                                                    | 例子                                                         |
  > | -------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
  > | **np.any([condition1,condition2..],axis=0)** | 返回任意符合条件的行                                    | **peoples[np.any([province=="河北",province=="山西",province=="内蒙古"],axis=0)]** |
  > | **np.all([condition1,condition2..],axis=0)** | 同理，**都必须加上axis=0**                              |                                                              |
  > | \|                                           | 或操作，多个相当于any                                   | np.where((province=="北京")                                  |
  > | &                                            | 与                                                      |                                                              |
  > | **np.where(condition)[0]**                   | 返回符合条件的索引的ndarray类型，可以直接用这个进行索引 | peoples[[np.where(province=="北京")[0],np.where(province=="天津")[0]]] |
  > |                                              |                                                         |                                                              |


- 花式索引

  ```python
  # 首先，你将有一个原始的NumPy数组，假设它是这样创建的：
  arr = np.array([[1, 2, 3, 4], 
                  [3, 4, 5, 6], 
                  [5, 6, 7, 8]])
  # 接着，要得到你想要的2x2数组，你可以这样做：
  arr[:,(1,3)][(0,2),:]
  arr[(0,2),:][:,(1,3)]
  #错误答案
  #arr[[0,2],[1,3]]
  #arr[(0,2),(1,3)]
  ```

  > 前两个操作用的索引访问都没用多个[]包起来，所以都是先访问了索引了一部分，之后再一次用索引到最后结果，相当于用了两次索引
  >
  > 后两个就是只索引一次，分别是索引（0，1）和（1，3）这两个元素

- 案例

  ```python
  # 从文本文件读取人口数据
  peoples = np.loadtxt("data/人口.csv",skiprows=2,delimiter=',',usecols=(range(1,13)),encoding="utf-8")
  province = np.loadtxt("data/人口.csv",skiprows=2,delimiter=',',usecols=0,encoding="utf-8",dtype=str)
  province
  
  # 读取北京的数据
  peoples[0]
  # 读取上海的人口数据
  flag=province=="上海"
  peoples[flag]
  #peoples[True]  #等价于peoples
  
  
  # 读取上海1994年的人口数据
  peoples[province=="上海",4]
  
  
  # 读取北京、上海、广东所有年份的人口数据
  f1=province=="上海"
  f2=province=="北京"
  f3=province=="广东"
  f4=f1+f2+f3
  f4
  peoples[f4]
  
  
  # 读取北京、上海、广东1993到2000年的数据
  peoples[f4,3:11]
  
  
  # 读取北京1991年、上海1994年，广东1995年的数据
  peoples[(0,8,18),(1,4,5)]
  
  
  #读取北京、上海，广东1991年、1994年、1995年的数据
  peoples[[[0],[8],[18]],(1,4,5)]
  peoples[[0,8,18],[[1,4,5],[1,4,5],[1,4,5]]]
  peoples[np.ix_([0,8,18],[1,4,5])]
  ```

  

### 数组的广播机制

广播机制是Numpy让两个不同shape的数组能够做一些运算，需要对参与运算的两个数组做一些处理或者说扩展，最终是参与运算的两个数组的shape一样，然后广播计算(对应位置数据进行某运算)得到结果。



广播机制首先需要判断参与计算的两个数组能否被广播机制处理？即判断是否广播兼容，**广播机制规则是，比较两个数组的shape，从shape的尾部开始一一比对。**

- (1). 如果**两个数组的维度相同，对应位置上轴的长度相同或其中一个的轴长度为1，则广播兼容**，可在轴长度为1的轴上进行广播机制处理。
- (2). 如果两个数组的维度不同，那么给低维度的数组**前扩展**提升一维，扩展维的轴长度为1,然后在扩展出的维上进行广播机制处理。

> 两数组有行相同或列相同或有一个数组只有一行或一列的元素应该就可以

- 广播机制与布尔数组的应用

  ```python
  a2=np.arange(1,21).reshape(4,5)
  a2>5  #广播机制，返回的shape不变，条件真就是true,否则False
  
  #用广播机制得出的布尔数组来做索引
  index= a2 % 2 == 0
  a2[index]
  ```


### 变换数组的形态

- 方法

  | 对象.方法名() | 说明               | 例子                                  |
  | ------------- | ------------------ | ------------------------------------- |
  | a.ravel()     | 展平数组，展成1行  |                                       |
  | a.flatten()   | 按行（列）展平     | 展行a1.flatten()；展列a1.flatten("F") |
  | a.repear()    | 按行（列）重复几次 | a.repeat(3,axis=1)                    |

- 函数

  | np.函数名()         | 说明                                         | 例子                                                         |
  | ------------------- | -------------------------------------------- | ------------------------------------------------------------ |
  | np.ravel()          | 展平数组，展成1行                            | a.ravel()                                                    |
  | np.flatten()        | 按行（列）展平                               | 展行a1.flatten()；展列a1.flatten("F")                        |
  | np.hstack()         | 将两个数组横向组合                           | np.hstack((a2,a3))                                           |
  | np.vstack()         | 将两个数组纵向组合                           | np.vstack((a2,a3))                                           |
  | np.concatenate()    | 横向或纵向合并数组，axis=1横向，0纵向，默认0 | np.concatenate((a2,a3),axis=1)                               |
  | np.hsplit()         | 横向分割                                     | np.hsplit(a,4) #平分四分<br/>np.hsplit(a,[1,3])#第一份1行，第二份2行 |
  | np.vsplit()         | 同上理                                       |                                                              |
  | np.tile(arr，shape) | 按arr重复shape个                             | np.tile(a,(2,3))  #2行3列                                    |
  

### numpy矩阵

> array类型没法直接使用矩阵的运算，但可以用矩阵的函数，传递array
>
> 用matrix函数转换成矩阵类型

```python
a1=np.array([[1,2,3],[4,5,6]])
a2=np.array([[1,3],[5,7],[9,11]])
# a1*a2  目前是数组，没法直接用矩阵的乘法运算
np.dot(a1,a2)

#matrix函数将数组转成矩阵matrix类型
m1=np.matrix(a1)
m1
m2=np.matrix(a2);m2
m1*m2
```

### ufunc类型（函数）

> 是对整个数组进行操作的

```python
#代码2-34：数组的四则运算
#创建两个一维数组x和y
x=np.array([1,2,3])
y=np.array([4,5,6])
#数组相加
x+y
np.add(x,y)  #通用函数
#数组相减
x-y
np.subtract(x,y)
#数组相乘
x*y
np.multiply(x,y)
#数组相除
x/y
np.divide(x,y)
#数组幂运算
x**y
np.power(x,y)


#代码2-35：数组的比较运算
#>,<,==,>=,<=,!=
x=np.array([4,2,3])
y=np.array([1,2,6])
x;y

x<y

x>y

x==y
np.equal(x,y)

x>=y

x!=y
np.not_equal(x,y)

x[x>y]
```

### 读写文件

```python
#代码2-39：二进制存储数据
a=np.arange(100).reshape(10,-1)
#使用save保存数组到文件
np.save("./data/save_a1",a)

#代码2-40：多个数组的存储
a=np.arange(9).reshape(3,3)
a1=np.arange(0,1,0.01)
#使用savez保存多个数组到文件（文件后缀名为npz）
np.savez("./data/save_arrs",x=a,y=a1)  #x,y随便的，相当于命名

#代码2-41：二进制读取文件
#读取单个数组的文件
load_a1=np.load("./data/save_a1.npy")
load_a1
#读取多个数组的文件（npz：多个数组文件）
load_arrs=np.load("./data/save_arrs.npz")
load_arrs.files
x1=load_arrs['x']  #通过类似字典的方式去访问
y1=load_arrs[load_arrs.files[1]]
x1;y1


#代码2-42：文本文件的存储与读取
a=np.arange(0,20,0.5).reshape(5,8)
#存储文本文件savetxt
np.savetxt("./data/save_txt",a,delimiter=",")
#读取文本文件loadtxt
b=np.loadtxt("./data/save_txt",delimiter=",")


#代码2-43：使用genfromtxt函数读取数据
np.genfromtxt("./data/save_txt",delimiter=",",skip_header=1)  #跳过一行
```

### 排序

| 命令                 | 说明                                 | 例子              |
| -------------------- | ------------------------------------ | ----------------- |
| sort()               | 排序函数，可以选择排序算法，有返回值 | np.sort(asix=1)   |
| **a.sort()**         | **排序方法，无返回值，原地操作**     | a.sort(asix=0)    |
| a.argsort()          | argument，排序后的原始下标           | a.argsort(axis=0) |
| np.lexsort(md_array) | 间接排序                             |                   |

```python
#lexsort：间接排序
name=np.array(['jb','lis','wa','liu','wa'])
age=np.array([41,24,53,74,51])
name;age
i1=np.lexsort((name,age))  #两个数组是对应的，因此一个排序另一个也要排序，默认先按后面的排，即按照age排
i2=np.lexsort((age,name))  #先按name排，相等再按age排
i1;i2

#lexsort应用
[(name[i],age[i])for i in i1]   #列表解析式，可以重复
dict(zip(name[i1],age[i1]))  #字典，但不能重复
np.vstack((name[i1],age[i1]))
#name排
[(name[i],age[i])for i in i2]   #列表解析式，可以重复
dict(zip(name[i2],age[i2]))  #字典，但不能重复
```

> **带arg函数的是重点，可以实现索引的高级操作**

### 统计函数

```python
#代码2-47：数组内去重
#创建字符串数组
name=np.array(['jb','lis','wa','liu','wa'])
np.unique(name)
#数组去重
name
set(name)
#不用Numpy的实现

#创建整型数组
a4=np.random.randint(1,5,size=10)
a4
#整型数组去重
np.unique(a4)


#代码2-50：Numpy中常用统计函数
#创建二维数组
a=np.arange(30).reshape(5,6)
a
#数组的和
a.sum()
#沿横轴的和(行的和)
a.sum(axis=1)
#沿纵轴的和（列的和）
a.sum(axis=0)
#数组均值
a.mean()
#沿横轴均值
a.mean(axis=1)
#沿纵轴均值
a.mean(axis=0)
#标准差和方差
a.std()
#最大值和最小值
a.max();a.min()
#最大值和最小值的索引（重点）
a.argmax();a.argmin()



#代码2-51：cumsum和cumprod
#创建数组

#累计和
a
np.cumsum(a,axis=0)
#累计积

```

### 案例

```python
# 1990年全国人口总和
peoples[:,0].sum()
# 2001年全国人口总和
p01=peoples[:,11]
p01.sum()
# 2001年各省市人口的均值和标准差
p01.mean()
p01.std()
# 广东1990年的人口
peoples[province=="广东",0]
# 广东每年人口增长值
np.diff(peoples[province=="广东"])
# 东北三省1990年人口之和
three=peoples[np.any([province=="辽宁",province=="吉林",province=="黑龙江 "],axis=0)]
np.sum(three[:,0])
# 东北三省2001年人口之和
np.sum(three[:,11])
# 东北三省每年人口增长值
np.diff(peoples[np.any([province=="辽宁",province=="吉林",province=="黑龙江 "],axis=0)])
# 各个省历年人口之和
np.sum(peoples,axis=0)
# 1990年人口最多的省份
province[np.argmax(peoples[:,0])]
# 2001年人口最多的省份
province[np.argmax(peoples[:,11])]
# 2001年人口最少的省份
province[np.argmin(peoples[:,11])]
```



## matplotlib

### matplotlib准备工作

```python
#导入
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# 设置中文显示
plt.rcParams["font.sans-serif"] = "SimHei"
plt.rcParams["axes.unicode_minus"] = False
```

- 子图的间距

```python
plt.tight_layout()
<Figure size 432x288 with 0 Axes>
```

```python
import pandas as pd
df = pd.read_csv("data/Euro2012.csv")
df.head()
```

- matplotlib的所有配置参数的字典

  ```python
  plt.rcParams
  # plt.rcdefaults()   #将rc参数恢复默认设置
  
  ## 修改线型
  plt.rcParams["lines.linestyle"]="--"
  ## 修改线宽
  plt.rcParams["lines.linewidth"]=3
  
  
  print(plt.style.available)  #打印所有风格
  plt.style.use("bmh")  #设置风格的函数
  ```

- 支持的图片格式

  ```python
  plt.figure().canvas.get_supported_filetypes()
  ```

  

### 基本语法

![image-20240329193522418](assets/image-20240329193522418.png)

- plt.figure：创建空白画布，在一幅图中可省略
- figure.add_subplot：第一个参数表示行，第二个参数表示列，第三个参数表示选中的子图编号
- plt.title：标题
- plt.xlabel：x轴名称
- plt.ylabel：y轴名称
- plt.xlim：x轴的范围
- plt.ylim：y轴范围
- plt.xticks：第一个参数为范围，数组类型；第二个参数是标签，第三个是控制标签
- plt.yticks：同plt.xticks
- plt.legend：图例
- plt.savafig：保存图形
- plt.show：在本机显示
> **上述都是函数，都要加括号**

```python
# 代码 3-2
## 生成数据
rad=np.arange(0,np.pi*2,0.01)


# 第一幅子图
## 确定画布大小
fig=plt.figure(figsize=(8,6),dpi=80,facecolor="cyan")
## 创建一个两行1列的子图，并开始绘制第一幅，用对象的add_subplot方法
ax1=fig.add_subplot(2,1,1)
## 添加标题
plt.title("子图示例1")
## 添加x轴的名称
plt.xlabel("x")
## 添加y轴的名称
plt.ylabel("y")
## 确定x轴范围
plt.xlim([0,1])
## 确定y轴范围
plt.ylim([0,1])
## 规定x轴刻度
plt.xticks([0,0.5,2])  #可以不均匀，权限大于范围lim
## 确定y轴刻度
plt.yticks(np.arange(0,1.1,0.1))
## 添加y=x^2曲线
plt.plot(rad,rad**2,label="$y=x^2$")  #可以省去x，只剩y
## 添加y=x^4曲线
plt.plot(rad,rad**4,label="$y=x^4$")
## 添加图例
plt.legend()
"""以上代码只针对与第一子图"""



# 第二幅子图
## 开始绘制第2幅
fig.add_subplot(2,1,2)  #一旦开始声明一个子图，那么接下来操作只针对该子图
## 添加标题
plt.title("sin/cos")
## 添加x轴的名称
plt.xlabel("radius")
## 添加y轴的名称
plt.ylabel("value")
## 确定x轴范围
plt.xlim(0,np.pi*2)
## 确定y轴范围
plt.ylim(-1,1)
## 规定x轴刻度
plt.xticks([0,np.pi/2,np.pi,np.pi*1.5,np.pi*2])
## 确定y轴刻度
plt.yticks([-1,-0.5,0,0.5,1])
## 添加sin曲线
plt.plot(rad,np.sin(rad),label="$y=sinx$")
## 添加cos曲线
plt.plot(rad,np.cos(rad),label="$y=cos(x)$")
## 添加图例
plt.legend()
## 保存图形到文件
plt.savefig("./data/")
## 调整图形
plt.subplots_adjust(hspace=0.3,wspace=0)  #调整高度间隔
## 显示图形
plt.show()
```

> 以上方式都必须只能针对当前的子图设置，不能对任意的子图进行设置，下面的方式可以在任意位置设置子图：
>
> 采用 对象.方法（）的方式，直接对某个子图对象进行操作
>
> - plt.xlabel() → ax.set_xlabel()
> - plt.ylabel() → ax.set_ylabel()
> - plt.xlim() → ax.set_xlim()
> - plt.ylim() → ax.set_ylim()
> - plt.title() → ax.set_title()  

#### xticks的特殊用法

```python
plt.xticks(range(0,12,2),range(1990,2002,2)) #第一个参数表示底下有12个刻度，用的是索引表示，取0.2.4...10的刻度；第二个参数表示第一个显示出来的刻度对应的真实的值，表示0索引对应1990,2索引对应1992，这是真实的，从1开始，不是索引表示
```

### 子图的绘制

#### add_subplot方法

```python
fig=plt.figure(figsize=(8,8))

x=np.arange(-10,10)
x
fig.add_subplot(221)#表示两行两列，第一幅图
plt.plot(x,x)
plt.title("$y=x$")

fig.add_subplot(222)
plt.plot(x,x**2)
plt.title("$y=x^2$")

# plt.add_subplot(223)  #报错，因为得按顺序
fig.add_subplot(223)
plt.plot(x,x**3)
plt.title("$y=x^3$")

fig.add_subplot(224)
plt.plot(x,x**4)
plt.title("$y=x^4$")

plt.suptitle("画布的总标题")
plt.subplots_adjust(hspace=0.4,wspace=0.3)



# 面向对象的add_subplot
fig=plt.figure(figsize=(8,8))

ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(212)  #ax3占两个，表示两行，此时变成一列，取第二行整行

ax2.plot(x,x**2)
ax1.plot(x,x)
ax3.plot(x,x)
ax2.set_title("$y=x^2$")
ax2.set_xlabel("x")
plt.show()
```

![image-20240618161842400](assets/image-20240618161842400.png)

#### subplot函数

```python
fig=plt.figure(figsize=(8,8))
x=np.arange(-10,11)
plt.subplot(221)
plt.plot(x,x)
#获取当前子图
ax1=plt.gca()

plt.subplot(222)
plt.plot(x,x**2)
plt.title("$y=x^2$")

plt.subplot(212)
plt.plot(x,x**3)

ax1.set_title("$y=x$")
plt.show()
```

![image-20240618162125479](assets/image-20240618162125479.png)

#### subplots函数（配合pd好用）

```python
plt.style.use("seaborn-whitegrid")
x=np.arange(-10,11)
#subplots返回值两个
fig,ax=plt.subplots(2,2,figsize=(8,8),sharex=True)#即使还没画图，位置也会先加载出来
ax[0,0].plot(x,x)
ax[0,1].plot(x,x**2)
ax[1,0].plot(x,x**3)
ax[1,1].plot(x,x**4)
#面向对象标题label这些都是set_...
ax[1,1].set_title("$y=x^4$")
plt.subplots_adjust(hspace=0.1)
plt.show()


#另一种使用方式
plt.style.use("seaborn-whitegrid")
x=np.arange(-10,11)
fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,figsize=(8,8),sharex=True)
ax1.plot(x,x)
ax2.plot(x,x)
ax3.plot(x,x)
ax4.plot(x,x)
```

![image-20240618162201242](assets/image-20240618162201242.png)

#### subplot2grid函数（推荐）

**plt.subplot2grid((shape),(loc),colspan=,rowspan=)**

```python
#2表两维
x=np.arange(-10,11)
plt.figure(figsize=(8,8))
plt.subplot2grid((2,2),(0,0))#第一个是shape，第二个是loc，现在表示0,0，即第一个
plt.plot(x,x)

plt.subplot2grid((2,2),(0,1))
plt.plot(x,x)

plt.subplot2grid((2,2),(1,0),colspan=2)
plt.plot(x,x)
```

![image-20240618162448984](assets/image-20240618162448984.png)

#### GridSpec函数配合subplot函数

> 也可以考虑

```python
x=np.arange(-10,11)
plt.style.use("seaborn-whitegrid")
plt.figure(figsize=(8,8))

grid=plt.GridSpec(2,2)

plt.subplot(grid[0,0])
plt.plot(x,x)
plt.subplot(grid[0,1])
plt.plot(x,x)
plt.subplot(grid[1,0:2])  #用切片的方式
plt.plot(x,x)

plt.show()
```

![image-20240618162530979](assets/image-20240618162530979.png)

### 曲线图

```python
# 从文本文件读取人口数据
peoples=np.loadtxt("data/人口.csv",skiprows=2,delimiter=",",usecols=(range(1,13)),encoding="utf-8")
province=np.loadtxt("data/人口.csv",skiprows=2,delimiter=",",usecols=(0),encoding="utf-8",dtype=str)
province

# 生成画布并设置大小
fig=plt.figure(figsize=(6,4))

# 绘制北京人口1990-2001年的折线图
beijing_y = peoples[0]
beijing_y
plt.plot(beijing_y,label=province[0],marker='*',color='g')

# 绘制上海人口1990-2001年的折线图
# print(np.where(province=="上海")[0])
plt.plot(peoples[8],label="上海",marker='.',color='b')

# 绘制广东人口1990-2001年的折线图
plt.plot(peoples[18],label="广东",marker='+',color='r')

# 设置各种参数
plt.title("北京、上海、广东人口折线图")
plt.legend(title="省市图例",loc="center left")
plt.xticks(range(0,12,2),range(1990,2002,2))
plt.axis([0,12,500,8000])
plt.show()
```

### 散点图

**plt.scatter(x, y, s, c, marker, cmap, norm, alpha, linewidths, edgecolorsl)**

- 参数说明：
    - x: x轴数据，不能像折线图一样省略
    - y: y轴数据
    - s: 散点大小
    - c: 散点颜色
    - marker: 散点图形状
    - cmap: 指定某个colormap值,该参数一般不用，用默认值
    - alpha: 散点的透明度
    - linewidths: 散点边界线的宽度
    - edgecolors: 设置散点边界线的颜色

```python
# 代码 3-6  第二季度，三大产业 散点图
data=np.load("./data/国民经济核算季度数据.npz",allow_pickle=True)
name=data['columns']
values=data['values']
name
values[0]
## 设置画布
fig=plt.figure(figsize=(6,4))
%matplotlib inline
## 绘制散点1 第二季度 第一产业
plt.scatter(values[1:69:4,0],values[1:69:4,3],marker='o',color="g",label=name[3])  #第一个values的列可以选数字列0，1，然后后面再设置xtick设置value实际的值
## 绘制散点2 第二产业
plt.scatter(values[1:69:4,0],values[1:69:4,4],marker='o',color="r",label=name[4])
## 绘制散点3 第三产业
plt.scatter(values[1:69:4,0],values[1:69:4,5],marker='o',color="b",label=name[5])  #label就是用来设置图例的

## 添加横轴标
plt.xlabel("时间（第二季度）")
## 添加纵轴标签
plt.ylabel("三大产业生产总值")
## 设置x轴刻度
plt.xticks(range(2,70,4),values[1:69:4,1],rotation=30)  #第一个是x真正的取值，第二个是索引，第一个可以对应上面plot.scatter的选取的数字列
## 添加图表标题
plt.title("三大产业第二季度国民生产总值散点图")
## 添加图例
plt.legend()
## 保存图形到文件

## 显示图形
plt.show()
```

### 折线图

plt.plot(x, y, linestyle, linewidth,color,marker, markersize, markeredgecolor, - markerfactcolor, label, alpha)
- x：指定折线图的x轴数据；
- y：指定折线图的y轴数据；
- linestyle：指定折线的类型，可以是实线、虚线、点虚线、点点线等，默认文实线；
- linewidth：指定折线的宽度
- marker：可以为折线图添加点，该参数是设置点的形状；
- markersize：设置点的大小；
- markeredgecolor：设置点的边框色；
- markerfactcolor：设置点的填充色；
- label：为折线图添加标签，类似于图例的作用

```python
# 代码 3-7
# 读入数据
data=np.load("./data/国民经济核算季度数据.npz",allow_pickle=True)
name=data['columns']
values=data['values']
name
values[0]
## 设置画布
fig=plt.figure(figsize=(8,4))
## 绘制折线图
plt.plot(values[0:69,1],values[0:69,3],c="r",ls="--",lw=2,marker="D")
## 添加横轴标签
plt.xlabel("时间）")
## 添加y轴名称
plt.ylabel("生产总值")
## 设置x轴刻度
plt.xticks()
## 添加图表标题
plt.title("三大产业国民生产总值折线图")
## 保存图形到文件

## 显示图形
plt.show()
```

### 条形图

- 调用方法：**plt.bar(x, y, width，,height, color, edgecolor, bottom, linewidth, align, tick_label, align)**

    > 横向：plt.barh

- 参数说明：

    - **x：指定x轴上数值**
    - **y：指定y轴上的数值**
    - width：表示条形图的宽度，取值在0~1之间，默认为0.8。选定**y时，指定width为宽度，而此时height指的是高度0-1**
    - height：当选**x时，指定height为高度，而此时width指的是宽度0-1**
    - color：条形图的填充色
    - edgecolor：条形图的边框颜色
    - bottom：y轴的基准,默认0
    - linewidth：条形图边框宽度
    - tick_label：条形图的刻度标签
    - align：指定x轴上对齐方式，“center”,"lege"边缘

    ```python
    ## 条形图举例（注意：不是直方图）
    label=['一班','二班','三班','四班']
    y=[38,40,42,45]
    plt.bar(x=label,height=y,width=0.7,color='g')   #条形图这里不叫y了叫height，width指每一条占的百分比
    plt.show()
    
    
    
    # 补充：横向条形图
    import numpy as np
    import matplotlib.pyplot as plt
    label=['2016','2017','2018','2019','2020']
    n=[20,30,25,15,40]
    x=range(len(n))
    # plt.barh(y=x,width=n,height=0.6,color='g') 
    plt.barh(y=label,width=n,height=0.6,color='g') 
    plt.title("公司销量条形图")
    plt.ylabel("年份")
    plt.xlabel("销量")
    # plt.yticks(x,label)
    plt.yticks(x,['2016年','2017年','2018年','2019年','2020年'])
    plt.show()
    ```

    ![image-20240427204126376](assets/image-20240427204126376.png)

    ![image-20240427204117711](assets/image-20240427204117711.png)

- 并列条形图

    ```python
    #补充 并列条形图：使x的位置错开
    label=['2016','2017','2018','2019','2020']
    n1=[20,30,25,15,40]
    n2=[40,60,43,10,73]
    x=np.arange(len(n1))
    w=0.4
    plt.figure(figsize=(6,4))
    
    plt.bar(x=x,height=n1,width=w,color='g',label="部门一")  #表示x宽度是w=0.4
    plt.bar(x=x+w,height=n2,width=w,color='r',label="部门二")    #x+w表示右移0.4
    
    plt.xticks(x+w/2,label)
    plt.legend()
    plt.title("并列条形图")
    plt.show()
    ```

    ![image-20240427204100518](assets/image-20240427204100518.png)

- 堆叠条形图

    ```python
    #补充 堆叠条形图：其中一个用bottom
    label=['2016','2017','2018','2019','2020']
    n1=[20,30,25,15,40]
    n2=[40,60,43,10,53]
    x=np.arange(len(n1))
    w=0.7
    plt.bar(x=x,height=n1,width=w,label="部门一",color='r')
    plt.bar(x=x,height=n2,width=w,label="部门二",color='g',bottom=n1)
    
    plt.xticks(x,label)
    plt.legend()
    plt.show()
    ```

    ![image-20240427204154465](assets/image-20240427204154465.png)

### 饼图

- 调用方法：**plt.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None, radius=None, counterclock=True, wedgeprops=None, textprops=None, center=(0, 0), frame=False)**
- 参数说明：
    - **x：指定绘图的数据**
    - explode：指定饼图某些部分的突出显示，即呈现爆炸式
    - **labels：为饼图添加标签说明，类似于图例说明**
    - colors：指定饼图的填充色
    - autopct：自动添加百分比显示，可以采用格式化的方法显示  #auto percent
    - pctdistance：设置百分比标签与圆心的距离
    - shadow：是否添加饼图的阴影效果
    - labeldistance：设置各扇形标签（图例）与圆心的距离；
    - startangle：设置饼图的初始摆放角度；
    - radius：设置饼图的半径大小；
    - counterclock：是否让饼图按逆时针顺序呈现；  #默认
    - wedgeprops：设置饼图内外边界的属性，如边界线的粗细、颜色等；
    - textprops：设置饼图中文本的属性，如字体大小、颜色等； #text proportions
    - center：指定饼图的中心点位置，默认为原点
    - frame：是否要显示饼图背后的图框，如果设置为True的话，需要同时控制图框x轴、y轴的范围和饼图的中心位置；

    ```python
    # 简单的饼图
    #https://echarts.apache.org/examples/zh/index.html各种图形的网站
    plt.figure(figsize=(4,4))
    n=[41,20,42,15]
    labels_list=['一班','二班','三班','四班']
    colors_list=['red','blue','green','purple']
    explodes=[0.4,0.05,0.1,0.2]  #explode是离圆心的距离
    
    plt.pie(n,labels=labels_list,explode=explodes,colors=colors_list,shadow=True,autopct="%.1f%%",startangle=90)
    
    plt.legend()
    plt.show()
    ```

    ![image-20240427204314491](assets/image-20240427204314491.png)

- 极坐标系

    ```python
    #极坐标系，极径和角度
    r=np.random.randint(1,10,5)
    theta=[i*np.pi/2 for i in range(5)]
    print(r)
    ax=plt.subplot(111,projection='polar')  #主要是projection
    ax.plot(theta,r,linewidth=3,color='g')
    ax.set_xticks(theta)
    ax.set_xticklabels(["第一","第二","第三","第四","第五"])
    
    plt.show()
    ```

    ![image-20240427204433623](assets/image-20240427204433623.png)

### 直方图

> 用来描述连续型数据的频数分布的状态，**一般用于正态分布的数据，如升高、成绩这些**

- 调用方法：**plt.hist(x, bins=10, range=None, normed=False, weights=None, cumulative=False, bottom=None, histtype=‘bar’, align=‘mid’, orientation=‘vertical’, rwidth=None, log=False, color=None, label=None, stacked=False)**
- 参数说明：
    - **x：指定要绘制直方图的数据；**
    - **bins：指定直方图条形的个数；**
    - **range：指定直方图数据的上下界，默认包含绘图数据的最大值和最小值；**
    - density：是否将直方图的频数转换成频率；
    - weights：该参数可为每一个数据点设置权重；
    - cumulative：是否需要计算累计频数或频率；
    - bottom：可以为直方图的每个条形添加基准线，默认为0；
    - histtype：指定直方图的类型，默认为bar，除此还有’barstacked’, ‘step’, ‘stepfilled’；
    - align：设置条形边界值的对其方式，默认为mid，除此还有’left’和’right’；
    - orientation：设置直方图的摆放方向，默认为垂直方向；
    - rwidth：设置直方图条形宽度的百分比；
    - log：是否需要对绘图数据进行log变换；
    - color：设置直方图的填充色；
    - label：设置直方图的标签，可通过legend展示其图例；
    - stacked：当有多个数据时，是否需要将直方图呈堆叠摆放，默认水平摆放
    - edgecolor：边界颜色

```python
import numpy as np
import matplotlib.pyplot as plt
## 设置中文显示
plt.rcParams["font.sans-serif"] = "SimHei"
## 设置正常显示符号
plt.rcParams["axes.unicode_minus"] = False

#用来描述连续型数据的频数分布的状态，一般用于正态分布的数据，如升高成绩这些

#升高数据
data=np.random.normal(165,20,1000)  #生成正态分布数据的函数

plt.hist(data,bins=15,rwidth=0.9,color='g',edgecolor='y')
# plt.hist(data,bins=15,rwidth=0.9,color='g',edgecolor='y',range=(150,180))
plt.xlabel("升高(cm)")
plt.ylabel("人数")
plt.title("1000个学生身高分布直方图")

plt.show()
```

![image-20240427204556774](assets/image-20240427204556774.png)

### 箱型图

> 也是用来**表述数据的分布的**
- 调用方法：**plt.boxplot(x, notch=None, sym=None, vert=None, whis=None, positions=None, widths=None, patch_artist=None, meanline=None, showmeans=None, showcaps=None, showbox=None, showfliers=None, boxprops=None, labels=None, flierprops=None, medianprops=None, meanprops=None, capprops=None, whiskerprops=None)**
- 参数说明：
    - x：指定要绘制箱线图的数据；
    - notch：是否是凹口的形式展现箱线图，默认非凹口；
    - sym：指定异常点的形状，默认为+号显示；
    - vert：是否需要将箱线图垂直摆放，默认垂直摆放；
    - whis：指定上下须与上下四分位的距离，默认为1.5倍的四分位差；
    - positions：指定箱线图的位置，默认为[0,1,2…]；
    - widths：指定箱线图的宽度，默认为0.5；
    - patch_artist：是否填充箱体的颜色；
    - meanline：是否用线的形式表示均值，默认用点来表示；
    - showmeans：是否显示均值，默认不显示；
    - showcaps：是否显示箱线图顶端和末端的两条线，默认显示；
    - showbox：是否显示箱线图的箱体，默认显示；
    - showfliers：是否显示异常值，默认显示；
    - boxprops：设置箱体的属性，如边框色，填充色等；
        - boxprops = {‘color’:‘g’, ‘facecolor’:‘yellow’}
        - ‘color’ : ‘g’ 箱子外框的颜色
        - ‘facecolor’ : ‘yellow’ 箱子填充的颜色
    - labels：为箱线图添加标签，类似于图例的作用；
    - flierprops：设置异常值的属性，如异常点的形状、大小、填充色等；
    - medianprops：设置中位数的属性，如线的类型、粗细等；
    - meanprops：设置均值的属性，如点的大小、颜色等；
    - capprops：设置箱线图顶端和末端线条的属性，如颜色、粗细等；
    - whiskerprops：设置须的属性，如颜色、粗细、线的类型等

- 直方图的概念（四分位距）

  ![直方图](assets/直方图.png)

  ![直方图描述](assets/直方图描述.png)

- **四分位距=IQR=Q3-Q1,上限=Q3+1.5*IQR，下限=Q1-1.5*IQR ,MAX， MIN**

  ```python
  # 代码 3-14
  import numpy as np
  import matplotlib.pyplot as plt
  ## 设置中文显示
  plt.rcParams["font.sans-serif"] = "SimHei"
  ## 设置正常显示符号
  plt.rcParams["axes.unicode_minus"] = False
  ## 从文件导入数据
  data=np.load("data/国民经济核算季度数据.npz",allow_pickle=True)
  name=data['columns']
  values=data['values']
  name
  values[0]
  ## 设置画布
  plt.figure(figsize=(6,4))
  ## 绘制箱型图 三大产业
  gpd=values[:,3:6]
  plt.boxplot(gpd,labels=name[3:6],showmeans=True,patch_artist=True)
  ## 添加图表标题
  plt.title("三大产业国民生产总值箱型图")
  ## 保存图形到文件
  
  ## 显示图形
  plt.show()
  ```

  ![image-20240427205037330](assets/image-20240427205037330.png)

- 小提琴图

```python
## 补充：小提琴图violin
import numpy as np
import matplotlib.pyplot as plt
## 设置中文显示
plt.rcParams["font.sans-serif"] = "SimHei"
## 设置正常显示符号
plt.rcParams["axes.unicode_minus"] = False
## 生成数据
data=np.random.normal(165,20,1000)  #生成正态分布数据的函数
data2=np.random.normal(160,15,1000)

plt.figure(figsize=(6,4))
plt.violinplot([data,data2],showmeans=True,widths=[0.4,0.4])
```

![image-20240427205116201](assets/image-20240427205116201.png)

- 1

- 极坐标系

  ```python
  
  ```

- 1

- 极坐标系

  ```python
  
  ```

- 1

### 常用函数

| [flt.]函数名           | 说明                                        | 调用                                                  |
| ---------------------- | ------------------------------------------- | ----------------------------------------------------- |
| figure                 | 设置画布，创建一个实例                      | fig=plt.figure(figsize=(8,6),dpi=80,facecolor="cyan") |
| fig.add_subplot(n,m,x) | 设置子图，前两个是几行几列，x是第几辐画     | ax1=fig.add_subplot(2,1,1)                            |
| title()                | 设置某子图标题                              | plt.title("子图示例1")                                |
| xlabel()               | x轴名称                                     | plt.xlabel("x")                                       |
| ylabel()               |                                             |                                                       |
| xlim()                 | x轴范围                                     | plt.xlim([0,1])                                       |
| ylim()                 |                                             |                                                       |
| xticks()               | x轴刻度                                     | plt.xticks([0,0.5,2])  #可以不均匀，权限大于范围lim   |
| plot(x,y,label="name") | 画图，label里用latex表示                    | plt.plot(rad,rad**2,label="$y=x^2$")                  |
| legend()               | 显示图例，loc="center left"表示位于中间左侧 |                                                       |
| grid()                 | 显示网格                                    |                                                       |
| subplots_adjust()      | 调整各子图的高度间隔                        | plt.subplots_adjust(hspace=0.3,wspace=0)              |
| savefig()              | 保存图形到文件                              | plt.savefig("./data/")                                |
| show()                 | 显示图像，没有也会默认显示                  |                                                       |

## pandas

> **分布的补充**
>
> **均匀：都是均匀的**
>
> **正态分布：中间高两边低**

- **数据类型**

  1. **Series：一维**，带标签数组
  
     Series有索引和数据值组成，有index和values属性
  
  2. **DataFrame：二维**，Series容器，由列和Series组成
  
  > numpy是ndarray和ufunc

### series的使用

> 用法和数组类似，**区别是可以改index，要求数据是同一个类型**

```python
# series索引和切片
 # 不包含结束的索引位置
 # 包含结束索引名
list=[21.2,4.1,54,6.7]
ser1=pd.Series(list,index=['a','e','c','d'])  #只能一种数据类型
ser1
ser1[2]
ser1[1:3]  #数值是开区间
ser1['e':'c']  #可以用新index进行切片，用非数字型的index是闭区间，因为新index不能-1，即使不是顺序的英文字母也行
```

### DataFrame的使用

![image-20240513204858020](assets/image-20240513204858020.png)

#### 创建

**pd.DataFrame(data=None, index=None, columns=None**, dtype=None, copy=False)

##### 正常的方式创建

![image-20240513205254061](assets/image-20240513205254061.png)

##### 字典的方式创建

> **用字典的方式创建其中键就是columns，索引就是默认的数值范围索引**

![image-20240513205325458](assets/image-20240513205325458.png)

![image-20240513210105539](assets/image-20240513210105539.png)

##### 增加列

![image-20240515152721170](assets/image-20240515152721170.png)

##### 设置行索引set_index方法

![image-20240515152908113](assets/image-20240515152908113.png)

![image-20240515152919266](assets/image-20240515152919266.png)

##### 以np数组创建

```python
# np数组生成Dataframe，此时loc和iloc一致
arr=np.arange(20).reshape(4,5)
df=pd.DataFrame(arr)
df
```

|      |    0 |    1 |    2 |    3 |    4 |
| ---: | ---: | ---: | ---: | ---: | ---: |
|    0 |    0 |    1 |    2 |    3 |    4 |
|    1 |    5 |    6 |    7 |    8 |    9 |
|    2 |   10 |   11 |   12 |   13 |   14 |
|    3 |   15 |   16 |   17 |   18 |   19 |



#### 取值操作（重点）

##### 取某列的Series

> **类似字典的方式，一个列就是Series，当多个列时就为DataFrame**

```python
#取列 ，取列用的是指定的方式
df3
# 列的调用方式（中括号和点）
# 每一列是一个Series
df3['Name']
df3.Age
#取多个列,不能[0]，默认是对行进行切片，因为axis=0，即横轴
df3[0:3]
df3[['Gender','Age']]  #分别取两个值
```

![image-20240513210339715](assets/image-20240513210339715.png)

- **按行迭代的方式**

  ```python
  #按行迭代
  df.head()
  for index,row in df.iterrows():
      print(index,end="：")
      print(row['tip'])
      pd.DataFrame()
  ```

  ![image-20240513211342124](assets/image-20240513211342124.png)

##### 取某行的DataFrame

> **类似np数组切片的方式**

```python
#取行,取行用的是切片的方式
dic = {"Name":["张三","李四","王五","赵六","钱七"],
      "Age":[18,25,30,21,19],
      "Gender":["男","女","女","男","女"]}
df3=pd.DataFrame(dic)
df3[0:3]
df3.index=['a','b','c','d','e']
df3
df3['a':'d']
# df3[['a','b','c']] #取列的操作
df3[0:2]
```

![image-20240513210741220](assets/image-20240513210741220.png)

##### 取某列某行（复合使用）

```python
###先筛选列后筛选行
# 闭区间
df["Name"]["li":"zhao"]
 # 开区间
df["Name"][1:4]
df["Name"][4]   #series才可以

df[["Name","Age"]]
df[["Name","Age"]]["li":"zhao"]  #闭区间
df[["Name","Age"]][1:4]  #半开半闭
# df[["Name","Age"]][1]  #dataframe就不能这样了，必须要切片


###先筛选行后筛选列
df["li":"zhao","Name","Age"]
```

![image-20240515153406081](assets/image-20240515153406081.png)![image-20240515153415282](assets/image-20240515153415282.png)

##### query方法

```python
detail.query("order_id==413")[['dishes_name','counts']]
#结果选自index列和['dishes_name','counts']列的order_id=413的数据
```

#### 增删改

```python
# 增加一列“Province”，设为“广东”
df["Province"]="广东"

# 增加一列“City”
df["City"]=["深圳","广州","广州","珠海","肇庆"]

# 删除“钱七”这一行
df.drop(4,axis=0,inplace=False)

# 删除City列，第一个参数是索引名，axis=0是删行，1是删列，inplace表示是否原地修改
df.drop("City",axis=1,inplace=False)#df.drop(4,axis=0,inplace=True)

#pop返回删除后的Series，直接原地修改，没有会报错
df.pop("Province")
```



#### loc的使用（重点）

##### 基本使用

> 有loc和iloc，iloc就是用数字索引来操作，loc就是字符索引
>
> - loc属性是针对DataFrame索引名称的切片方法，**如果传入的不是索引名称，那么切片操作将无法执行**。利用loc属性，能够实现所有单层索引切片操作。loc属性的使用方法如下。
>   **DataFrame.loc[行索引名称或条件, 列索引名称]**
> - iloc和loc区别是iloc接收的必须是行索引和列索引的**位置**。iloc属性的使用方法如下。
>   **DataFrame.iloc[行索引位置, 列索引位置]**

```python
# 索引名称，返回series
df.loc['zhang']
type(df.loc['zhang'])
#索引位置，类似series的方式用，取值，返回series
df.iloc[2]
type(df.iloc[2])		
```

![image-20240515153151558](assets/image-20240515153151558.png)

##### loc的花式索引

```python
# loc方法索引和切片, 推荐的方式，也可以实现多行多列
df
#先行后列，类似ndarray里
df.loc["zhao","Age"]
df.iloc[3,1]

df.loc[['zhao','qian'],'Age']
df.loc[['zhao','zhang'],['Age','Sex']]

```

![image-20240515153945593](assets/image-20240515153945593.png)

![image-20240515154010657](assets/image-20240515154010657.png)

##### loc的条件索引

```python
# 条件切片, 要用条件只能用loc，不用iloc
# 年龄小于20的姓名
df
df.loc[df["Age"]<20,:]  #只有行有条件，列没有
df.loc[df["Age"]<20,["Name","Age"]]
df.loc[df["Age"]<20,:][["Name","Age"]]  #等价于上式

# df.iloc[df[1]<20,:]  #因为iloc不支持，所以会报错
#如果一定要用iloc的方式
df.iloc[(df["Age"]<20).values,]

# # 条件切片，age<20的所有人
df["Age"]<20  #返回一个布尔型的series
```

![image-20240515154145781](assets/image-20240515154145781.png)

##### loc使用多个条件

**条件部分用(条件1)&(条件2)...表示**

```python

#给小费多于6快的数据：再按照性别统计小费均值，多个条件可以用()&()连接
tips.loc[tips['tip']>6,['tip','sex']].loc[tips['sex']=='Male','tip'].mean()
tips.loc[tips['tip']>6,['tip','sex']].loc[tips['sex']=='Female','tip'].mean()
tips.loc[(tips['day']=="Sat")&(tips['time']=="Dinner"),'tip'].mean()
```

![image-20240521203236227](assets/image-20240521203236227.png)

#### DataFrame的数据查看

![image-20240513211446409](assets/image-20240513211446409.png)

#### DataFrame的方法

- .rank()：按数值求出名词
- .sort_index(**axis=0,ascending=True**)
- .sort_values(**column,ascending=True**)

![image-20240521203027880](assets/image-20240521203027880.png)

#### DataFrame的统计计算

![image-20240521202606030](assets/image-20240521202606030.png)

![image-20240521202610687](assets/image-20240521202610687.png)

```python
df
# 按性别统计人数，以下例子都是先取出一个Series
df["Sex"].value_counts()
# 非重复值的数量
df.nunique()
df["Sex"].unique()
---------------------------
# 平均年龄
df['Age'].mean()
np.mean(df["Age"])
df["Age"].min()
```

![image-20240521202722359](assets/image-20240521202722359.png)![image-20240521202805589](assets/image-20240521202805589.png)

```python
#取出DataFrame再用，用两层括号
df[["Sex"]]
# 语文和数学平均分
df[["chn","math"]].mean()  #等价于df['chn'].mean();df['math'].mean()
# 最高最低分
df[["chn","math"]].max()
df[["chn","math"]].min()

# 添加一列平均分Aver
df["Aver"] = (df["chn"] + df["math"]) / 2
df
```

![image-20240521202852652](assets/image-20240521202852652.png)

### 分组聚合

#### 基本使用

**要求df包含column列：df.groupby(by=['column','column2'...])[取需要的列].聚合函数|agg(np.聚合属性|"聚合名")|apply(np.聚合属性|"聚合名")**

**不要求df包含column列：df.groupby(by=df['column'])**

![image-20240528134903567](assets/image-20240528134903567.png)

```python
import pandas as pd
dict = {"Name":["张三","李四","王五","赵六","钱七"],
       "Age":[18,25,30,21,19],
       "Sex":["男","女","女","男","女"],
       "chn":[90,85,62,58,75],
       "math":[96,66,73,60,90]}
df = pd.DataFrame(dict)
df
# 按性别求均值，dataframe，前dataframe，后列或series
df[['Age','Sex']].groupby(by='Sex')
df[['Age','Sex']].groupby(by='Sex').mean()
#另一种方式，series，前series后series
type(df['Age'].groupby(by=df['Sex']))
df['Age'].groupby(by=df['Sex']).mean()
```

![image-20240528135211078](assets/image-20240528135211078.png)

#### 输出组内成员

- **df.get_group('column')**

```python
#分组对象，进行调用和遍历
group1=df.groupby(by='Sex')
group1
group1.get_group('男')  #通过上面定义的对象，访问其内部分类好的组
group1.get_group("女")
#不知道分组里面有啥，通过循环遍历该次分组的所有项（值）
for key,gr in group1:
    print(key)
    print(gr)
    print("**********************************")
```

![image-20240528135502912](assets/image-20240528135502912.png)

#### apply和agg的使用

```python
# apply不支持分组的多个函数聚合
#df.groupby(by="Sex")[["chn","math"]].apply([np.sum,np.mean])

df.groupby(by="Sex")[["chn","math"]].apply("mean")
#分组之后的apply（np）方法却不一样，结果是chn和math加起来的均值
df.groupby(by="Sex")[["chn","math"]].apply(np.mean)

#除了apply的另一种方法：agg，既分组又多个函数聚合
df.groupby(by="Sex")[["chn","math"]].agg("mean")
df.groupby(by="Sex")[["chn","math"]].agg(np.mean)  #这里的agg（np）就相同了，不像apply
```

#### 运用lamda函数

```python
# 将语文和数学分数变为10分制。lambda函数，语法：lambda 形参:返回值
df
df[['chn','math']].apply(lambda x:np.round(x/10,1))
df[['chn','math']].agg(lambda x:np.round(x/10,1))
```

![image-20240528140133011](assets/image-20240528140133011.png)

#### apply和agg的高级用法

```python
# 分组聚合的应用，复杂的用agg就行了，简单随便用

# apply不支持分组的多个函数聚合，分组单个函数就可以
df.groupby(by="Sex")[["chn","math"]].apply("sum")
#df.groupby(by="Sex")[["chn","math"]].apply([np.sum,np.mean])

#但是agg支持，aggregate，所以可以主要使用agg，要用lambda才用apply
df.groupby(by="Sex")[['chn','math']].agg([np.sum,np.mean])
df.groupby(by="Sex")[['chn','math']].agg({'chn':np.sum,'math':np.mean})#apply不行

#agg还支持多个函数
result=df.groupby(by="Sex")[['chn','math']].agg({'chn':[np.sum,np.min],'math':[np.mean,np.max]})
result
result.columns  #两层了，叫Multiindex
```

### 聚合排序

#### 非分组

```python
# 非分组的聚合排序（np的sort函数作为参数），注意，分组后，用sort的话只能用apply
df[['total_bill','tip']].apply(np.sort).head()
df[['total_bill','tip']].agg(np.sort).head()
```

![image-20240528140736877](assets/image-20240528140736877.png)

#### 分组

```python
#按照性别分组，取每个组小费最多的前五名
df.groupby(by='sex')['tip'].apply(np.sort)  #这里没法使用agg方法
#女，取第0组
df.groupby(by='sex')['tip'].apply(np.sort)[0][-5:]
#男
df.groupby(by='sex')['tip'].apply(np.sort)[1][-5:]

#别的方式1
df.sort_values(by=['tip','sex']).groupby(by='sex')[['sex','tip']].tail()
#别的方式2，这里的lambda对于agg不能使用，若有apply或agg用不了的函数或想使用参数的话可以用lambda，复杂的lambda就只能用apply
df.groupby(by='sex').apply(lambda x:x.sort_values(by='tip',ascending=False).head())[['sex','tip']]
```

![image-20240528141052959](assets/image-20240528141052959.png)

### DataFrame的交叉表

**pd.crosstab(index,columns,values=None**,rownames=None,colnames=None,**aggfunc=None..) -> 'DataFrame'**

```python
# 以性别和班级形成交叉表
# crosstab函数的columns、index、values、aggfunc等参数
df.groupby(by=["Class","Sex"]).size()
# pd.crosstab(index,columns,values=None,rownames=None,colnames=None,aggfunc=None,margins: 'bool' = False,
#     margins_name: 'Hashable' = 'All',dropna: 'bool' = True,normalize: 'bool' = False,
# ) -> 'DataFrame'
pd.crosstab(df['Sex'],df['Class'])
pd.crosstab(columns=df['Sex'],index=df['Class'])
pd.crosstab(index=df['Sex'],columns=df['Class'],margins=True)  #自动带个all

# 复杂的交叉表（可以用透视表）
#pd.crosstab(index=df['Class'],columns=df['Sex'],values=df['chn'],aggfunc="mean")#对values进行聚合
pd.crosstab(index=[df['Class'],df['Name']],columns=df['Sex'],values=df['chn'],aggfunc="mean")
```

![image-20240608180124583](assets/image-20240608180124583.png)



### DataFrame的透视表

**pd.pivot_table(data: 'DataFrame',values=None,index=None,columns=None,**

![image-20240608180350647](assets/image-20240608180350647.png)

### 时序数据的操作

#### 时序类型转换

**pd.to_datetime()**

#### 时许数据的读取

**时序数据.dt.year|month|day**

```python
###################读数据
# 选取时间段
apple.loc[apple['Date']=="2014-07-08",:]
#选择2012年的数据，str.contains方法：选取包含某字符串的信息，只能针对字符串使用
apple.loc[apple['Date'].str.contains("2012"),:]

# 将Date列转换为日期时间类型
apple["Date"]=pd.to_datetime(apple["Date"])  #不赋值原本不动
#还可以用原来的方式，但不能用字符串方法
apple.loc[apple['Date']=="2014-07-08",:]


######################取年月日
# 选择年、月和日的字段
apple['Date'].dt
apple['Date'].dt.year
apple['Date'].dt.month
apple['Date'].dt.day
#设置年、月和日的字段
apple['Year']=apple['Date'].dt.year
apple['Month']=apple['Date'].dt.month
apple['Day']=apple['Date'].dt.day
```

#### 其他操作（重采样和生产时间数据）

```python
# 时序数据分组的操作，可以存在列没有by这一列，然后调用时间序列的方法进行分组
apple.groupby(by=apple.index.year)[['Open','Close']].agg("mean")

# 重采样resample（重要），相当于对时序数据的分组
apple.resample("10Y")['Open'].mean()  #10Y：每十年取一次
apple.resample("10M")['Open'].mean()
apple.resample("20W")['Open'].mean()
apple.resample("BM")["Close"].mean()   #月的最后一天

#生成时间类型的数据
pd.date_range(start="20230101",end="20240531",freq="5M")
```

![image-20240608181104925](assets/image-20240608181104925.png)

#### 实例

```python
#扩展例子
df=pd.read_excel("data/PM25.xlsx")
df.head()
df1=df.set_index("月份")
df1.head()
#重采样，这里表示一年一取
df1.resample("Y")["PM2.5","PM10","CO"].mean().plot.line()
```

![image-20240618140057818](assets/image-20240618140057818.png)

### pandas的画图

> **可以随意和pyplot搭配，pandas里仅仅是随意快速的画出图，具体的设置要用plt来实现**
>
> 1. **折线：df.plot(ax=)==df.plot.line(ax=)**
> 2. **散点：plot(kind="scatter",x=,y=,ax=)**
> 3. **条形图：plot.bar(ax=)**
> 4. 直方图：plot.hist(edgecolor,rwidth,**ax=**)
> 5. 箱型图：plot.box(**ax=**)或boxplot(**ax=**)
> 6. 饼图：plot.pie(figsize=(),autopct='%.1f%%',explode=[],labels=,**ax=**)

```python
# 绘制语文和数学关系的散点图
df.plot(kind="scatter",x="chn",y="math",title="语文数学成绩关系散点图")
# 语文数学折线图
df.plot.line(y=["chn","math"])
# 语文成绩条形图
df.plot.bar(x="Name",y=["chn","math"])
# 横向条形图
df.plot.barh(x="Name",y="chn")

# Series绘图
df["chn"].plot.bar()
df['math'].plot.line()

# 语文数学成绩条形图（堆叠）
df.plot.bar(x="Name",y=["chn","math"],stacked=True)

# 选取字段绘图
df[["chn","math"]].plot.bar()

# 数学成绩直方图
df["math"].plot.hist(edgecolor="red",rwidth=0.95)

# 语文数学成绩的箱型图
df[["chn",'math']].plot.box()

## Pandas快速画图绘图的子图，运用每个画图方法里的ax
fig,ax=plt.subplots(2,2,figsize=(6,6))
df.plot.bar(x="Name",y=["chn","math"],title="语文数学成绩条形图",ax=ax[0,0])
df.groupby(by="Sex").size().plot.pie(ax=ax[0,1])
df[["chn","math"]].plot.box(ax=ax[1,0])
df.plot.scatter(x="chn",y="math",ax=ax[1,1])
```

![image-20240618135751577](assets/image-20240618135751577.png)

### pandas的文件读取

#### read_table（适用于所有）

**pd.read_table("file",sep=",",encoding='')**

**head（）和tail（）函数：默认读前后5行**

```python
# 从文本文件创建
import pandas as pd
# 两种方法读取csv文件
#read_table，会把第一行作为columns
df1=pd.read_table("./data/scores.txt")  #read_xx有很多的方法读文件的，自选，还有json
df1.head(3)  #默认返回前5行
type(df1)

#csv也可以用read_table，需要指定sep分隔符
df2=pd.read_table("data/scores.csv",sep=",",encoding='gbk')
df2.head(1)

#read_csv
df3=pd.read_csv("data/scores.csv",encoding='gbk')
df3.head(1)

# read_excel
df4=pd.read_excel("data/users.xlsx",sheet_name="users2")
df4.head(1)
df2["num"] 
```



#### read_(excel,csv,...)

**pd.read_csv("data/scores.csv",encoding='gbk',index_col="num")#设置某一个column作为index**

#### 保存数据集

```python
# 带索引或不带索引，index表示是否保存，false的话DataFrame的index就会去掉，直接保存values和columns
tips.to_csv("data/tips_to_csv.csv",index=True)
tips.to_csv("data/tips_to_csv1.csv",index=False)
```

## pandas数据预处理

### 合并数据

#### concat函数

**pd.concat([df1,df2],axis=,ignore_index=,join="inner|outer")**

![image-20240618180336793](assets/image-20240618180336793.png)

![image-20240618180431362](assets/image-20240618180431362.png)

#### merge函数

**pd.merge(left**: 'DataFrame | Series',**right**: 'DataFrame | Series',
    **how**: 'MergeHow' = 'inner',**on**: 'IndexLabel | None' = None,
    **left_on**: 'IndexLabel | None' = None**,right_on**: 'IndexLabel | None' = None,
    left_index: 'bool' = False,right_index: 'bool' = False,
    sort: 'bool' = False,suffixes: '**Suffixes**' = ('_x', '_y'),  #指明重复名字自动添加，用于区分的，因为不能重名
) -> 'DataFrame'

![image-20240621162541788](assets/image-20240621162541788.png)

```python
pd.merge(df_score,df_class_1,on="班级编号",how="inner")
pd.merge(df_score,df_class_1,on="班级编号",how="outer")
pd.merge(df_score,df_class_1,on="班级编号",how="left")
pd.merge(df_score,df_class_1,on="班级编号",how="right")
```

![image-20240621162625624](assets/image-20240621162625624.png)

#### join方法

> **使用join函数，则需要两个表主键名字相同**

df_score.join(df_class_1,on="班级编号")

![image-20240621162707695](assets/image-20240621162707695.png)

### 数据清洗

#### 去重

**df.drop_duplicates(inplace=True,keep="last")**

#### 缺失值的处理

```python
# 发现缺失值
iris.isnull().sum()
# 非缺失值有
iris.notnull().sum()
# petal_width_cm列缺失值所在行
iris.loc[iris["petal_width_cm"].isnull(),:]

### 缺失值处理
# 1、删除缺失值axis=0
df=iris.dropna(axis=0,how="any",inplace=False)
df.shape
# axis=1，不适合
df1=iris.dropna(axis=1,how="any",inplace=False)
df1.shape
# 2、填充缺失值（前向、后向）
#前向
df3=iris.fillna(method="ffill")
df3.head(15)
#后向
df4=iris.fillna(method="bfill")
df4.head(15)
# 3、填充具体值，只适用于这种已知道只有某一列有空的情况
df5=iris.fillna(0.2)
df5.head(15)
# 列填充具体值，相比于上述，更适应所有情况
iris["petal_width_cm"]=iris["petal_width_cm"].fillna(0.35)
iris.head(15)
# 类别均值, 在这里比较合适。
m=iris.loc[iris["class"]=="Iris-setosa","petal_width_cm"].mean()
m
# 类别均值填充
iris["petal_width_cm"].fillna(m,inplace=True)
iris.head(15)
```

![image-20240621163036181](assets/image-20240621163036181.png)

![image-20240621163054501](assets/image-20240621163054501.png)

![image-20240621163114428](assets/image-20240621163114428.png)

![image-20240621163148447](assets/image-20240621163148447.png)

#### 异常值处理

用describe()或describe(include='all')来查看有无特别偏离的异常

![image-20240621163343808](assets/image-20240621163343808.png)

```python
# 绘图方式发现异常值，散点图
iris.plot.scatter(x="sepal_length_cm",y="sepal_width_cm")
# 直方图发现异常
iris["sepal_length_cm"].plot.hist()
# 箱型图发现异常
iris["sepal_length_cm"].plot.box()
# 定位异常位置
iris.loc[iris['sepal_length_cm']<1,:]
# 具体行
iris.loc[iris['sepal_length_cm']<1,"sepal_length_cm"]*=100
iris.describe()
```

![image-20240621163500998](assets/image-20240621163500998.png)

![image-20240621163541163](assets/image-20240621163541163.png)

### 数据转换

#### 函数转换

```python
# 一般会把文本数据简单数值化，例如性别变为0和1
# 定义转换函数
def transform(gender):
    if gender=="女":
        return 0  #男1女0
    elif gender=="男":
        return 1
scores["gender"]=scores["gender"].agg(transform)
scores.head()
#还可以
#scores["gender"].apply(lambda x:0 if x=="女" else 1)
#scores["gender"].map({"女":0,"男":1})
```

![image-20240624141133111](assets/image-20240624141133111.png)

#### 哑变量

```python
# 性别的哑变量处理
genders=pd.get_dummies(scores["gender"],prefix="gender")
genders
# 哑变量合并到数据
scores=pd.concat([scores,genders],axis=1)
scores.head()
```

![image-20240624141233413](assets/image-20240624141233413.png)

#### 离散化

```python
# 对英语成绩离散化
scores["chn"]=pd.cut(scores["chn"],bins=[0,72,84,96,108,120],labels=["不及格","及格","中等","良好","优秀"])
```

![image-20240624141304567](assets/image-20240624141304567.png)

# 附录

## 各结构方法总结

> 方法都是以“结构.方法名()”来进行操作的

| 结构类型 | 方法                               | 说明                                                         | 例子                                 | 返回值                         |
| -------- | ---------------------------------- | ------------------------------------------------------------ | ------------------------------------ | ------------------------------ |
| **str**  | title()                            | 首字母大写                                                   |                                      |                                |
|          | upper()                            |                                                              |                                      |                                |
|          | lower()                            |                                                              |                                      |                                |
|          | rstrip()                           | 删除右边空格                                                 |                                      |                                |
|          | lstrip()                           | 删左边空格                                                   |                                      |                                |
|          | strip()                            | 同时去除左右的空格，默认为空格或换行，可以特别指定别的：'\0' | str.strip('左右')                    | 返回原字符串的副本             |
|          | `split`(*sep=None*, *maxsplit=-1*) | 返回一个由字符串内单词组成的列表，使用 *sep* 作为分隔字符串。**sep**没给的话是**默认是空格**，几个空格都可以。 如果给出了 **maxsplit**，则**最多**进行 **maxsplit** 次拆分。如果给出了 *sep*，则连续的分隔符不会被组合在一起而是被视为分隔空字符串 | '1<>2'.split('<>',1)                 |                                |
|          | rsplit                             |                                                              |                                      |                                |
|          | lsplit                             |                                                              |                                      |                                |
|          | `join`(*iterable*)                 | 返回一个由 *iterable* （可迭代的对象，如字符串组成的列表）中的字符串拼接而成的字符串。 如果 *iterable* 中存在任何非字符串值包括`bytes`对象则会引发`TypeError`。 调用该方法的字符串将作为元素之间的分隔。 | ':'.join("2020 09 05 13 54".split()) | '2020:09:05:13:54'             |
|          | `replace`(*old*, *new*[, *count*]) | 返回字符串的副本，其中出现的**所有**子字符串 *old* 都将被替换为 *new*。 如果给出了可选参数 *count*，则只替换前 *count* 次出现。 | '111'.replace('1','2',1)             |                                |
|          | `count`(*sub*[, *start*[, *end*]]) | 返回子字符串 *sub* 在 [*start*, *end*] 范围内非重叠出现的次数，默认是整个字符串。 可选参数 *start* 与 *end，* 会被解读为切片表示法。 | 'www.example.com'.count('w',1,7)     | 2                              |
|          | `find`(*sub*[, *start*[, *end*]])  | 返回子字符串 *sub* 在 `s[start:end]` 切片内被找到的最小索引  | 'www.example.com'.find('w',1,7)      | 如果 *sub* 未被找到则返回 `-1` |
|          | `isalpha`()                        | 全是字母                                                     |                                      |                                |
|          | `isdecimal`()                      | 全是数字                                                     |                                      |                                |
|          | `chr`(*i*)                         | 返回 Unicode 码位为整数 *i* 的字符的字符串格式               | chr(97)                              | a                              |
|          | `ord`(*c*)                         | 对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。 | ord('a')                             | 97                             |
|          |                                    |                                                              |                                      |                                |
|          |                                    |                                                              |                                      |                                |
|          |                                    |                                                              |                                      |                                |
| **list** | append()                           | 末尾添加                                                     |                                      | none                           |
|          | extend()                           | 末尾添加列表                                                 |                                      | none                           |
|          | insert(i,x)                        | 在第i个位置插入x                                             |                                      | none                           |
|          | pop(i)                             | 删除下标为i的元素，默认为末尾                                |                                      |                                |
|          | remove(x)                          | 删除第一个值为x的元素，没有valueerror                        |                                      |                                |
|          | clear()                            | 清除所有                                                     |                                      |                                |
|          | 列表内置方法                       |                                                              |                                      |                                |
|          | copy()                             | 等价于list[:]或str[:]。不会对原本数据进行修改                |                                      |                                |
|          | count()                            |                                                              |                                      |                                |
|          | index(x[, i[, j]])                 | *x* 首次出现项的索引号（范围[i,j)），没有找到时ValueError。不确定是否存在时，先使用in进行检查。 |                                      |                                |
|          | len()                              |                                                              |                                      |                                |
|          | 列表专属方法                       |                                                              |                                      |                                |
|          | reverse()                          | 将列表中的元素逆序，就地反转。若不想使列表，那就[::-1]       |                                      | none                           |
|          | sort(*key=None*, *reverse=False*)  | 此方法会对列表进行升序排序，只使用 `<` 来进行各项间比较。*reverse* 值默认为False。 如果设为 `True`，则每个列表元素将按降序进行排序。*key* 指定带有一个参数的函数，用于从每个列表元素中提取比较键，(例如 `key=str.lower`)，此时会先将每个元素转换成小写再比较 | list.sort(reverse=True)              | none                           |
|          | reversed（）函数                   | 反转                                                         |                                      |                                |
|          | sorted()函数                       | 返回一个新的排序列表                                         |                                      |                                |
|          |                                    |                                                              |                                      |                                |
|          |                                    |                                                              |                                      |                                |
|          |                                    |                                                              |                                      |                                |
| dict     | get(*key*[,default])               | 如果 *key* 存在于字典中则返回 *key* 的值，否则返回 *default*。 如果 *default* 未给出则默认为 `None` |                                      |                                |
|          | setdefault(key,default)            | 设置默认值。如果字典存在键 *key* ，返回它的值。如果不存在，插入值为 *default* 的键 *key* ，并返回 *default* 。 *default* 默认为 `None`。就是不更新，只添加 |                                      |                                |
|          | copy()                             |                                                              |                                      |                                |
|          | pop(key，default)                  | 如果 *key* 存在于字典中则将其移除并返回对应value，否则返回 *default*。 如果 *default* 未给出且 *key* 不存在于字典中，则会引发`KeyError` |                                      |                                |
|          | del函数                            |                                                              |                                      |                                |
|          | popitem()                          | 删除键值对。从字典中移除并返回一个 `(键, 值)` 对。 键值对会按 LIFO(Last in,First out 后进先出)的顺序被返回。如果字典为空，则会引发`KeyError`。 | d1.popitem()('lady', 'yu')           |                                |
|          | fromkeys(iterable,[None/value])    | 创建并返回字典。使用来自 *iterable* 的键创建一个新字典，并将键值设为 *value。第二个参数不填，默认为None。* | d1 = d.fromkeys(d.keys(),9)          |                                |
|          | clear()                            |                                                              |                                      |                                |
|          | update()                           | 合并字典，将一个字典的键值对复制到另一个字典中，若键相同则按新的算 |                                      |                                |
|          | copy()                             |                                                              |                                      |                                |
|          |                                    |                                                              |                                      |                                |
|          |                                    |                                                              |                                      |                                |
| **dict** | keys()                             | 键，遍历字典时，默认是用key                                  |                                      |                                |
|          | values()                           | 值                                                           |                                      |                                |
|          | items()                            | 键值对                                                       |                                      |                                |
|          | get('键名','键不存在返回')         | 若键不存在返回第二个参数，若没第二个参数返回None             |                                      |                                |

## 常用库

### math库

math库里要用到的就最多只有：fabs,fmod,**floor,ceil**,trunc

> 注：**oracle里的函数不用导入，且次幂是power（多个er）**
>
> **内置数学函数（不需要导入math）**：**abs,min**,ascii,**pow,sum,round,reversed,sqrt**

- 区分内置函数与math库函数

| 函数名    | 内置函数/需import math | 说明                                                         |
| --------- | ---------------------- | ------------------------------------------------------------ |
| abs       | 内置函数               | 返回数字的绝对值                                             |
| **pow**   | **内置函数**           | 返回 x 的 y 次幂，其中 x 和 y 都是数字，pow(x, y) = x**y     |
| **round** | **内置函数**           | 四舍五入为最接近的整数                                       |
| max       | 内置函数               | 返回最大值                                                   |
| min       | 内置函数               | 返回最小值                                                   |
| sum       | 内置函数               | 返回所有元素的和                                             |
|           |                        |                                                              |
| **trunc** | **需import math**      | 返回 x 的截断整数部分                                        |
| **sqrt**  | **需import math**      | 返回 x 的平方根，x 必须是数字                                |
| exp       | 需import math          | 返回 e 的 x 次方 (e**x)，e 是自然对数的底数                  |
| log       | 需import math          | 返回 x 的自然对数，默认底数为 e，可以通过添加第二个参数来更改底数 |
| sin       | 需import math          | 返回一个角的正弦值，角度是以弧度为单位的                     |
| cos       | 需import math          | 返回一个角的余弦值，角度是以弧度为单位的                     |
| tan       | 需import math          | 返回一个角的正切值，角度是以弧度为单位的                     |
| **ceil**  | **需import math**      | 返回大于等于 x 的最小整数                                    |
| **floor** | **需import math**      | 返回小于等于 x 的最大整数                                    |
| expm1     | 需import math          | 返回 e 的 x次方减1 (e**x - 1)，e 是自然对数的底数            |
| log10     | 需import math          | 返回以10为底的x的对数                                        |
| log2      | 需import math          | 返回以2为底的x的对数                                         |



### random库

程序有时候需要产生随机数，random库提供了一些产生随机数的函数，列举如下：

> 1、生成闭合区间的整数随机数
> **randint(start,stop)**，参数start代表最小值,参数stop代表最大值，产生的整数随机数在[start,stop]**闭区间**

> 2、生成半闭合整数随机数
> randrange(start,stop,step)，参数start代表最小值,参数stop代表最大值，step代表步长，产生的随机数在[start,stop)**半闭半开区间**，不含stop值

> 3、随机选择函数
> choice()函数在列表等集合中随机选择一个元素输出，元素的类型没有限制

> 4、生成半闭合区间浮点数随机数
> random()函数生成[0.0,1.0]之间的任意浮点数

### turtle画图库

导入:

> import turtle | from turtle import *

| 方法                              | 描述                                                         | 例子              |
| --------------------------------- | ------------------------------------------------------------ | ----------------- |
| forward()                         |                                                              | fd()              |
| backward()                        |                                                              | bk()              |
| right()                           |                                                              | rt()              |
| left()                            |                                                              | lt()              |
| seth(a)                           | 改变绝对方向                                                 | seth(60)          |
| home()                            | 回到（0,0）                                                  |                   |
| color(pencolor,[fillcolor])       | pencolor是画笔颜色，fillcolor是填充颜色                      |                   |
| fillcolor()                       | 设置填充色                                                   |                   |
| begin_fill()                      | 开始填充                                                     |                   |
| end_fill()                        | 结束填充色，会对画好的图像进行填充                           |                   |
| setup(width,height,startx,starty) | #setup设置窗体大小，四个参数中后**两个参数非必选参数； #setup()是非必须的；** | setup(300,300)    |
| goto(x,y)                         | 绝对坐标                                                     |                   |
| penup()                           | 抬起笔，此时海龟不会画                                       | pu()              |
| pendown()                         | 放下笔                                                       | pd()              |
| pensize()                         | 笔的宽度                                                     | width()           |
| pencolor()                        | 笔的颜色                                                     |                   |
| **circle(r,angle)**               | **r作为半径画angle角度的弧度**                               | **circle(1,360)** |
| done()                            | 作为turtle停止的方法。如果不停止，在运行一次程序的话会任务无响应 |                   |
| hideturtle()                      | 隐藏海龟头                                                   |                   |

> circle的起点默认在（0，0）但是，圆心不是该点，圆心位于园边上。
>
> 角度若是正表示以0，0为最底下往上画，若画了几个角度，则角度也会相应变化
>
> 如circle(50,270)后circle(50,-90)

### time库

time.sleep()可以让程序暂停n秒

time.time()当前时间

## 优先级

| 运算符说明 |      Python运算符       | 优先级 | 结合性 | 优先级顺序 |
| :--------: | :---------------------: | :----: | :----: | :--------: |
|   小括号   |           ( )           |   19   |   无   |     高     |
| 索引运算符 | x[i] 或 x[i1: i2 [:i3]] |   18   |   左   |     ︿     |
|  属性访问  |       x.attribute       |   17   |   左   |     \|     |
|    乘方    |           **            |   16   |   右   |     \|     |
|  按位取反  |            ~            |   15   |   右   |     \|     |
| 符号运算符 |  +（正号）、-（负号）   |   14   |   右   |     \|     |
|    乘除    |       *、/、//、%       |   13   |   左   |     \|     |
|    加减    |          +、-           |   12   |   左   |     \|     |
|    位移    |         >>、<<          |   11   |   左   |     \|     |
|   按位与   |            &            |   10   |   右   |     \|     |
|  按位异或  |            ^            |   9    |   左   |     \|     |
|   按位或   |           \|            |   8    |   左   |     \|     |
| 比较运算符 |  ==、!=、>、>=、<、<=   |   7    |   左   |     \|     |
| is 运算符  |       is、is not        |   6    |   左   |     \|     |
| in 运算符  |       in、not in        |   5    |   左   |     \|     |
|   逻辑非   |           not           |   4    |   右   |     \|     |
|   逻辑与   |           and           |   3    |   左   |     \|     |
|   逻辑或   |           or            |   2    |   左   |     \|     |
| 逗号运算符 |       exp1, exp2        |   1    |   左   |     低     |

