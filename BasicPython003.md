# BasicPython003

标签（空格分隔）： Python Markdown

---
### 003部分
>From：实习-滴滴出行  2017.12.6
####  1. 面向对象编程
1. 类和实例 `class & instance`
  - 定义：`class Student(Object):pass`
  - 实例化：`stu = Student()`
  - 实例对象可任意绑定属性`stu.name = 'Bob'`
2. 初始化
  - 函数`def __init__(self, arg1, arg2,...)`
  - 类的**所有**函数的第一个参数**必须为：**`self`
  - 创建实例时，参数`self`不用传递
3. 访问限制
  - 内部成员（private）,加2下划线 : `self.__name`
  - 特殊变量：`__xxx__`可以直接访问
  - 单个下划线开头变量：默认为private,可以直接访问
  - 内部成员加类名前缀可以强制访问：`stu._Student__name`
4. 继承和多态
  - 类似Java
  - 判断一个变量的类型：`isinstance(stu, Student)`
  - Python属于动态语言（**鸭子类型**）
5. 获取对象属性
  - 使用`type()`判断对象类型
  - 函数`type()`返回值为**Class**类型
  - 对象类型：`str、int`等或`import types`中的常量：`types.FunctionType;types.LambdaType;types.GeneratorType`等
  - `isinstance([1, 2, 3], (list, tuple))`
  - 使用**dir()**:获取对象属性和方法
       - getattr(obj, 'args',default):异常则返回default，下同
       - setattr(obj, 'args')
       - hasattr(obj, 'args')
6. 类属性（类static）
```python
class Student(object):
    name = 'Student'
```
**忌对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性**

