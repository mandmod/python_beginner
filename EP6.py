# todo: type Conversion การแปลงค่าตัวแปล
'''
Data Type
https://www.youtube.com/watch?v=zGOMrqsGi2k&list=PLltVQYLz1BMBwqJysYnoEKWXUvqusJpgN&index=10

'''
x = 10
y = 3.14
z = '20'

result = x + y
# result = x + z #todo: ตัวแปล z เป็นข้อความ ไม่สามารถนำมาคำนวนได้
result1 = x + int(z)
result2 = int(z) + x
print(str(y))
print()
print(type(x))
print(type(y))
print(type(z))
print()
print(type(result))
print(result)
print()
print(type(result1))
print(result1)
print()
print(type(result2))
print(result2)
