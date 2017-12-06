# 自学Python

@[Python, , Markdown]

>说明：根据GitHub开源文档入手，来自：[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000) 。自夏令营结束后的暑假开始想学点能用的东西
 
 --------------------------------
### 002部分
####  函数
#####    调用
	
    #Python
    abs(-100)  #100
    int('12.3')  #12.3
    bool(1)   #True
    hex(25)   #0x19
    
#####     定义
函数可以返回多个值（实际是返回一个tuple），可以使用`import math`类似语句导包。默认参数必须指定为不变对象：

    #函数,若在文件中，需要'from filename import my_abs'
    def my_abs(x):
	    #参数检查
	    if not isinstance(x, (int, float)):
	        raise TypeError('bad operand type')
	    if(x > 0):
		    return x
		else :
			return -x   #return None 即return .
	#空函数
	def fun1():
		pass #pass 相对于占位符	
		
	#返回
	import math
	def move(x, y, step, angle=0):
	    nx = x + step * math.cos(angle)
	    ny = y - step * math.sin(angle)
    return nx, ny
    x, y = move(100, 100, 60, math.pi / 6)   #调用
   
#####   可变参数与不变参数
函数的参数可以采用两种参数形式，不变参数传递时需要先将参数定义为 list 或 tuple；可变参数调用更加灵活，在参数前加`*`，接收的是一个tuple：

    def calc(numbers):   #不变参数，可变参数为def calc(* numbers)
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
    #调用
    calc([1, 2, 3])
    calc((1, 2, 3))
    calc(1, 2, 3)    #可变
    calc()
    calc(*num)   #num = [1, 2, 3]

##### 	关键字参数
关键字参数多用于拓展函数参数，`**kw`接收的是一个dict：

    def person(name, age, **kw):
	    print('name:', name, 'age:', age, 'other:', kw)
	#调用
	>>> person('Michael', 30)
	name: Michael age: 30 other: {}
	>>> person('Adam', 45, gender='M', job='Engineer')
	name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
	>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
	>>> person('Jack', 24, **extra)  #这里是值传递
	name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
命名关键字参数：

    def person(name, age, **kw):
	    if 'city' in kw: # 有city参数
	        pass
	    if 'job' in kw:  # 有job参数
	        pass
		print('name:', name, 'age:', age, 'other:', kw)
	#调用时不受参数个数限制
	person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
    
    #加限制的命名
    def person(name, age, *, city, job):
	    print(name, age, city, job)
	person('Jack', 24, city='Beijing', job='Engineer')
	