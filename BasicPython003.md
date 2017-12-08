# BasicPython003

标签（空格分隔）： Python Markdown

---
### 003部分
>From：实习-滴滴出行  2017.12.6
####  **面向对象编程**
1. 类和实例 `class & instance`
  - 定义：`class Student(object):pass`
  - 实例化：`stu = Student()`
  - 实例对象可任意绑定属性`stu.name = 'Bob'`
2. 初始化
  - 函数`def __init__(self, arg1, arg2,...)`
  - 类的**所有**函数的第一个参数**必须为：**`self`
  - 创建实例时，参数`self`不用传递
3. 访问限制
  - 内部成员（private）,加2个下划线 : `self.__name`
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


#### **面向对象高级属性**
*多继承、定制类、元类等*

1. 使用\__slots\__
   - 给**实例**绑定属性与函数
   - **\__slots__只对当前实例起作用，在继承中无效**
   ```python
    class Student(object):
        pass
    #绑定属性
    s1 = Student()
    s2 = Student()
    s1.name = 'Mike'
    print(s1.name)   
    #绑定函数
    def set_age(self, age):
        self.age = age
    from types import MethodType
    s1.set_age = MethodType(set_age, s)
    s1.set_age(25)    #s1.age = 25
    s2.set_age(35)    #error!!  方法只能单独绑定实例
    #给类绑定方法，所有实例均可使用
    Student.set_age = set_age 
    
    class Student(object):
        __slots__ = ('name', 'age')  #限制实例属性
    ```
2. 使用@property
  - @property属于装饰器，把一个方法变成属性调用
  - setter & getter
3. 多重继承
4. 定制类  [---官方链接---][1]
  - `__str__`：返回字符串，面向用户
  - `__repr__`：返回字符串，面向开发者
  - `__iter__`：类实现for...in循环，调用`__next__()`拿到循环的下一个迭代对象
  - `__getitem__ & __setitem__ & __delitem__`：
  - `__getattr__`：处理调用某些不存在的属性或函数；方便api的调用
  - `__call__`：直接用实例本身调用
  **callable()函数判断一个对象是否是可调用的**
5. 枚举类
  - value属性则是自动赋给成员的int常量，默认从1开始计数
    ```python
  from enum import Enum
  Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
  for name, member in Month.__members__.items():
      print(name, '=>', member, ',', member.value)
  ```

  - 可使用`unique`从`Enum`派生出自定义类
  - `@unique`装饰器可以帮助我们检查保证没有重复值
6. 元类(metaclass)
  - `type()`：查看一个类型或变量的类型（相对于类型和类类型）
  - `type()`：创建新类型
  - 元类：`metaclass`
    - 创建(修改)类类型
    - 先定义metaclass，就可以创建类，最后创建实例
    - 继承自`type`类
  - **元类主要作用于orm：[对象-关系映射][2]**


  [1]: https://docs.python.org/3/reference/datamodel.html#special-method-names
  [2]: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000#0