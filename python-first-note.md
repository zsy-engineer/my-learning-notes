# Python零基础入门：一份学习笔记

## 前言

本文记录了我在学习Python过程中的完整笔记，涵盖了从变量到函数的核心概念。适合零基础的Python初学者系统学习。

## 目录

1.变量与数据类型
2.输入输出
3.字符串
4.keyword
5.列表、元组、字典
6.条件判断
7.循环
8.函数定义

## 1、变量与数据类型

```python
#基本的数据类型
a=10                  #整数 int
b=3.14                #浮点数 float
c="Hello"             #字符串 str
d=True                #布尔值 bool

#查看数据类型
print(type(a))        #<class 'int'>
print(type(b))        #<class 'float'>
print(type(c))        #<class 'str'>
print(type(d))        #<class 'bool'>
```

## 2、输入输出

```pyhton
#输入
name=input("请输入你的名字:")
age=int(input("请输入年龄:"))

#输出格式化
print(f"你好 {name}， 你今年{age}岁")
print("你好{}，你今年{}岁".format(name, age))
```

## 3、字符串

### int把字符串转化为整数

```python
a=4
b="15"
#print(a+b)错误,因为b是字符串而a是数
print(a+int(b))
>>19
```

### float把字符串转化为小数

```python
a=4
b="15"
print(a+float(b))
>>19.0
```

### str把x转换成字符串

```python
a="我今年"
b=18
#print(a+b)错误，因为a是字符串而b是数
print(a+str(b))
>>我今年18
```

### eval能把字符串“变成可运行的代码”

```python
print(eval("3+4"))
```

#### 字符串操作

```python
#字符串常用方法
text="hello python"

print(text.upper())  #HELLO PYTHON
print(text.lower())  #hello python
print(text.title())  #Hello Python
print(len(text))     #12(长度)
print(text.split())  #['hello', 'python'](分割)
```

## 4、keyword

| 类别 | 关键字列表 |
| ----- | ---- |
| 基础结构 |False, None, True, and, as, asssert, await, break |
| 控制流 |class, continue, def, del, elif, else, except, finally|
| 逻辑与循环 |for, from, global, if, import, in, lambda, nonlocal|
| 函数与异常 |not, or, pass, raise, return, try, while, with, yield|

## 5、列表、元组、字典

```python
#列表List-可修改
fruits=["apple", "banana", "orange"]
fruits.append("grape") #添加元素
print(fruits[0])       #apple

#元组Tuple-不可修改
colors=("red", "green", "blue")
print(colors[1])       #green

#字典Dictionary-键值对
person={"name":"张三"， "age":18}
print(person["name"])  #张三

#字典：添加元素
person["city"]="北京"

#字典：获取元素(避免KeyError)
print(person.get("name"))  #张三
print(person.get("height","未知"))  #未知

#字典：遍历字典
for key, value in person.items():
    print(f"{key}:{value}")
```

## 6、条件判断

```python
score=85
if score>=90:
    print("优秀")
elif score>=80:
    print("良好")
elif score>=60:
    print("及格")
else:
    print("不及格")
```

## 7、循环

```python
#for循环
for i in range(5):  #0到4
    print(i)
for i in range(2, 6):  #2到5
    print(i)
for i in range(0, 10, 2): #0,2,4,6,8(步长为2)

# while循环
count=0
while count<3:
    print(count)
    count +=1       #count=count+1
```

## 8、函数定义

```python
#定义函数
def greet(name):
    return f"你好，{name}!"

#调用函数
result=greet("李四")
print(result)   
>>你好，李四!
```

## 学习心得
实践比理论更重要
