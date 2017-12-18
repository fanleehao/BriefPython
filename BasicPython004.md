# BasicPython004

标签（空格分隔）： Python Markdown

---
### 004部分
>From：实习-滴滴出行  2017.12.11
####   **IO编程（同步io）**
1. 文件读写
  - 读文件（文本文件，utf-8）
      - `f = open('url','r')`    #文件不存在时抛出IOError错误
      - `f.read()`   #一次读取文件的全部内容，在内存中是一个str对象
      - `f.close()`   #文件使用后必须关闭
      - `read(size)：读取size字节内容；readline()读取一行；readlines()一次读取所有返回行list`
      - with语句
  - 二进制文件
     - `f = open('url','rb')`
  - 字符编码
     - 读取非utf-8编码文件：`f = open('url','r',encoding='gbk')  #读取gbk文件`
     - 文本文件中可能夹杂了一些非法编码的字符：`f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')  #直接忽略`
  - 写文件
    ```python
    f = open('url', 'w')
    f.write('hello')
    f.close()
    
    ```
      - with 语句
2. StringIO 和BytesIO
 - StringIO
     - 创建一个StringIO对象，内存中读写str
     - getvalue()获取写入后的str
     - 读取之前，可以用str初始化
 - BytesIO
     - 操作二进制数据
     - 创建BytesIO对象，然后写入
     ```python
     form io import BytesIO
     f = BytesIO()
     f.write('中文'.encode('utf-8'))
     print(f.getvalue())
     
     ```

3. 操作文件和目录
  - 导入模块：`import os`
  - 获取环境变量：`>>>os.environ  #so.environ.get('key')`
  - 操作文件和目录的函数：`os 与 os.path 两个模块中`
     - `os.path.join('url1', 'url2')  #合并`
     - `os.path.split('/home/test/a.txt')   #('/home/test', 'a.txt')`
     - `os.path.splitext(/home/test/a.txt')  #('/home/test', '.txt')  获取文件类型`
     - `os.rename('a.txt','a.py')  os.remove('a.py')`
  - shutil模块
  - 文件过滤：
    ```python
    >>>[x for x in os.listdir('.') if os.path.isdir(x)]
    ['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
    #列出所有.py文件
    >>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
    
    ```
4. 序列化
 - 变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
 - pickle模块来实现序列化：`pickle.dumps(dict)` 把对象序列化成bytes
 - 反序列化：`pickle.loads(f)`
 - 类对象，需先转化后再进行序列化

---

#### **正则表达式**
 1. 匹配字符串的规则，基本
     - 完全匹配：\d，一个数字；\w，一个字母或数字；.，匹配任意字符；
     - *，匹配任意多个字符，用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符：
        - `\d{3}\s+\d{3,8}：`匹配以任意个空格隔开的带区号的电话号码
 2. 高级
    - []:表示范围，`[0-9a-zA-Z\_]:一个字母数字或下划线`
    - [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}：变量的长度是1-20个字符（前面1个字符+后面最多19个字符）
    - A|B：或
    - ^\d：行的开头为数字
    - \d$：行的结尾为数字
3. python中的正则表达式模块：`re`
   - 字符串r前缀，避免转义问题：`s = r'ABC\-001'`
   - 匹配：`re.match()：匹配成功返回match对象，否则返回None`
   - 预编译，groups

---
#### **常用内置模块**
1. datetime
    - 获取当前日期和时间：`datetime.datetime.now()`
    - 获取制定日期和时间：`datetime(2015,12,11,12,20)  #年月日时分秒`
    - datetime和timestamp转化
         - 相对于1970年1月1日 00:00:00的秒数
         - datetime(2015,11,12,12,10).stamp()
         - datetime.fromtimestamp(1200000) ： 转化为datetime类型
    
    - str与datetime转化 [*详细链接*][1]
        - datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S') 
        - datetime.now().strftime('%a, %b %d %H:%M')
    - 日期加减
         
2. collections
3. base64

   


  [1]: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior