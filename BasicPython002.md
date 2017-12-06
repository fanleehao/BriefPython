# 自学Python

@[Python, , Markdown]

>说明：根据GitHub开源文档入手，来自：[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000) 。自夏令营结束后的暑假开始想学点能用的东西
 
 --------------------------------
 --------------------------------
### 002部分
>From：实习-滴滴出行  2017.12.1
#### 函数
  - 系统调用 [查看](https://docs.python.org/3/library/functions.html)
	  - max()
	  - int()
	  - abs()等
  - 定义 def
	   ```	
	   def my_abs(x):    **空函数：pass:**
                if x >= 0:
                    return x
                else:
                    return -x
        ```
  - 调用
  - 参数、函数返回值（为tuple）
	  - **函数参数列表顺序：位置（必选）参数 -> 默认参数-> 可变参数（*tuple） -> 命名关键字参数 -> 关键字参数（*\*dict） **
	  - 命名关键字参数（位于分隔符 * 之后，有可变参数（*tuple）后即可省略）**必须传入参数名，可设置缺省**
	  - 任何函数都可以调用：`fun(*agrs, **kw)`
  - 递归函数（尾递归优化 -> **解决递归栈溢出问题（python并未实现）**）
>python : 简单 + 可读性 ->  高级语言效率高？

#### 高级特性
- 切片（list & tuple）：截取子集

    >>> L = ['Mike', 'Bob', 'Cidy', 'Dicy', 'Eno', 'Fred']
    >>> L[0:3]    *0，1，2；0可省略 -> L[:3]*
     ['Mike', 'Bob', 'Cidy']        
		- 负数为倒数：-1索引为倒数第一个 `L[-10:]  #后10个数`
		- 多级索引：`L[:10:2]  #前10个数中每两个取一个，即第0、2、...个`
		- 缺省：`L[:]  #复制  L[::-1] 反转`
		- 字符串：`'ABCDEF[:3]' -> 'ABC'`
		- list & tuple & string 切片后的结果类型不变
- 迭代（Iteration）`for` 循环遍历`list & tuple` 等可迭代对象 
	- `for value in 'asdafdsf'`
	- 判断是否可迭代：`from collections import Iterable -> isinstance('acdd',Iterable)`
	- 类`Java` 的下标循环遍历：`enumerate（） #把list->（索引-元素）对 ` 
		- `for i, value in enumerate(['a','b','c'])`
		- `    print(i, value)`
- 列表生成器
	- `list(range(1,11))  #[1,2,3,...,10]`	
	- `[x * x for x in range(1,11)]  #[1,4,9,...,100]`
	- `[x * x for x in range(1,11)] if x % 2 == 0  #[4,16,...,100]`
	- `嵌套循环-全排列：[m + n for m in 'ABC' for n in 'XYZ']  #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']`
	- 应用：列出当前目录所有文件等
- 生成器
	- 节省空间：generator
	- `[] -> (): g = (x * x for x in range(10))`
	- 通过`next(变量名如g)` 或`for x in g`获取下一个返回值
	- `yield` 关键字在函数中则为generator
- 迭代器（Iterator）
	- 集合类数据：`list` `tuple` `dict` `set` `str`等
	- `generator`：生成器和带`yield`的`generator function`
	- 可迭代对象（Iterable）`↑↑上述两类`  ----> 可用`for`循环遍历
	- 迭代器对象（Iterator）可用`for 及 next()`遍历
	- 判断：`from collections import Iterator  -> isinstance([],Iterator)`
	- 使用`iter()`函数将集合类数据等转换成迭代器

#### 支持函数式编程
 - 高阶函数
	 - 变量可以指向函数`f=abs f(-10)  #10`
	 - 函数名可作变量`abs = 10  #abs函数将失效`
	 - **函数可作为函数的参数** `def add(x, y, f)  # add(-5, 6, abs)`
	 - map/reduce函数
		 - `map(function, Itrator)  #返回Iterator`
		 - `reduce(function, Itrator)  #function(x, y)`
		 - `reduce(f,[a,b,c]) = f(f(a,b),c)`
	 - filter
		 - `filter(function, Iterator)   #保留依据function的True/False`
		 - 筛选
	 - sorted
		 - `sorted([3,2,-1])  # [-1,2,3]`
		 - 高阶函数：根据key指定的函数作用于list的每一个元素，并根据key函数返回的结果进行排序. `sorted(list, key=kw)  # sorted([2,3,-4], key=abs) -> [2,3,-4]`
		 - 字符串排序、反向排序`reverse = True`等
 - 返回函数
	 - 函数作为返回值
		 - 	内部函数可以使用外部定义变量和参数
		 - 	外部函数返回的是函数，不可直接调用  
		 - 	**每次调用的函数返回值为不同的函数**     
     - 闭包
	     - 不可引用循环变量
 - 匿名函数（lambda）
	 - `lambda x: x * x   #def f(x): return x*ｘ`
	 - 可以赋值给函数对象：`f = lambda x : x * x`
	 - 匿名函数做返回值	
```
 def build(x,y):
		 return lambda: x * x + y * y
```
 - 装饰器：通过变量调用函数(**Decorator**)
	 - 函数对象的`__name__`属性
	 - **代码运行期间动态增加功能**
	 - 相当于返回函数的高阶函数
	  
```
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
```
 - 偏函数
	 - functools.partial创建偏函数
	 - e.g. `int2 = functools.partial(int, base=2)`
	 - 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
#### 模块
  - 包（Package）
	  - 必须含有`__init__.py`文件，否则为普通目录
	  - 内置模块（import 导入）
	  - 作用域
		  - 公开（public）：`abc,PI`
		  - 模块内部使用（private）通过前缀`_`实现：`_abc`
		  - 特殊专用：`__xxx__`（一般视为private）
		  - 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public
	  - 安装第三方模块
		  - 包管理工具：`pip`
		  - 第三方库：[点击](https://pypi.python.org/pypi)
	 