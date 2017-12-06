#这是第一个Python程序
# -*- coding:utf-8 -*-
a = 100
#print('i\'m ok!\ni\'m learning Python')
#print(r'\\\\\\\t\n\\')
print('输出中文测试')
height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi < 18.5:
    print('A')
elif bmi < 25:
    print('B')
elif bmi < 28:
    print('C')
elif bmi < 32:
    print('D')
else:
    print('E')