# 类Class与实例Instance
'''
* python中一切类型皆为对象object
* 用class声明的叫做类，是实例模版。实例是类的执行结果。
* class可以包括属性和方法
* class声明时，第一个参数是只继承的父类，如果不需要继承，可以写object
* class中的方法，第一个参数都可以写self，指向instance
* class中的特殊方法__init__相当于构造函数constructor
'''

class Student(object):

    def __init__(self, name, score): # constructor(可以不写在最前面，但没必要)
        self.name = name # 属性
        self.score = score

    def printInfo(self): # 方法
        print('Name: \033[32m%s\033[0m, Score: \033[32m%s\033[0m' % (self.name, self.score))

    def getLevel(self):
        score = self.score
        if score >= 90:
            return 'A'
        elif score >= 75 and score < 90:
            return 'B'
        elif score >= 60 and score < 75:
            return 'C'
        else:
            return 'D'

    def updateScore(self, score):
        self.score = score

print(Student) # <class '__main__.Student'>

Michael = Student('Michael', 98)
Lucy = Student('Lucy', 82)
print(Michael, Lucy) # <__main__.Student object at 0x1052144e0> <__main__.Student object at 0x105214518> 内存地址不同

Michael.printInfo() # Name: Michael, Score: 98
Lucy.printInfo() # Name: Lucy, Score: 82
print(Michael.getLevel()) # A
print(Lucy.getLevel()) # B

'可以通过方法来修改类的属性值'
Michael.updateScore(65)
print(Michael.getLevel()) # C
'也可以通过instance来直接修改属性值'
Lucy.score = 92
print(Lucy.getLevel()) # A