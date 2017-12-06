# 自学Python

@[Python, , Markdown]

>说明：根据GitHub开源文档入手，来自：[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000) 。自夏令营结束后的暑假开始想学点能用的东西
 
 --------------------------------
### 001部分
**Python** ：Guido van Rossum，1898，Advanced
Python的设计哲学是“优雅”、“明确”、“简单”。
#### 安装
- OS：win10/Linux/Mac OS( 后者更好 )
- Python： Python-3.6.0 x64
- Python解释器： CPython
- 编辑器： Sublime / Notepad++
#### 运行
- 命令行式： cmd    `python xxx.py`    
- Python交互式： >>>   `print(100 + 200)`
- 后者打印每一行结果，相当于执行单行语句
 
####  输入输出
- print()
	- `print('Hello, world!')` 
	- `print('100 + 200 = ', 100 + 200)`
	- `print('Hello','world')`
- input()
	- `name = input(); aaa/; name = 'aaa'`
	- `name = input('Enter your name:'); print(name)`
#### 语法基础
 - 数据类型：整型、浮点型、字符型、布尔型，空值
	 1. `"I'm OK!"` 和`" I \'m \"OK!\" "`
	 2. `print('\\\t\n\\')` 和 `print(r'\\\\\\\n\\t\\')`
 - 变量：可反复赋值 **这里在内存中生成对应的变量，然后将变量名指向**
	 - `a = 5 #整型`
	 - `a = 'abc' #字符串`
 - 整除：`//`   取模：`%`
 - 编码：`Unicode形式`
	 - `ord('A') #获取字符的整数形式`
	 - `chr('65') #将编码转化为字符`
	 - Pyhon中的字符串类型为`str`，在内存中为Unicode，一个字符对应1或多个字节。转化为`bytes`：
		 - `'abc.encode('utf-8')' -> b'abc'`：`bytes`型中每个字符占一字节
		 - `'学习'.endcode('utf-8')`
		 - `b'\xe5\xad\xa6\xe4\xb9\xa0'.decode('utf-8')`
     - 其他：
	     - `len('abc') #3`
	     - `len('学习'.encode('utf-8')) #6`
 - 占位符（类同 C/C++）：
	 - `%s` `'hello, %s' % 'XXXXX'`
	 - `%d 或 %f 或 %x` `'%d + %d = %d' % (3, 4, 7)`
	 - `%% #转义` 
#### lsit & tuple
   - list：有序列表，类型不唯一
   ```>>> name = ['Mike','Job','Neo']
>>> name
['Mike', 'Job', 'Neo']```
	  - 常用函数：
		  - `len(name)  #3`
		  - `list.append('Key')`
		  - `list.insert(1, 'Lay')`
		  - `list.pop(1) #默认为空，末位`
  - tuple：元组，对象不能更改
	  - `name = ('a', 'b', 'c')`
	  - `t = (1,)  #定义一个元素时注意`
#### 选择和循环
 - `for... in ...` 
 - `while`
####  dict和set
 - dict：相当于map，键值对；dict消耗空间，节省时间，与list相对
	 - `d = {'Mike': 80, 'Job':60}`
	 - `d['Mike']  #80`
	 - `d.get()`
	 - `d.pop()`
 - set：不可重复元素集合
	 - `s = set([1,2,3])`
	 - `s.add()`
	 - `s.remove()`