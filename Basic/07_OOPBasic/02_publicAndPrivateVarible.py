# 公共变量public和私有变量private
'''
* 公共变量public，可以在内部调用修改，也可以在外部通过instance调用修改
* 私有变量private，只能在内部调用修改。外部如果想修改，最好通过使用API来进行调用修改
* 有些python解释器会将私有变量名以_class__property的形式暴露出去，但强烈不建议通过实例访问
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name # public
        self.__score = score # private
    def printInfo(self):
        print('Name: \033[32m%s\033[0m, Score: \033[32m%s\033[0m' % (self.name, self.__score))
    def getScore(self):
        return self.__score
    def setScore(self, score):
        self.__score = score

Michael = Student('Michael', 98)
Michael.printInfo() # Name: Michael, Score: 98

'通过instance获取并修改公共变量'
print(Michael.name) # Michael
Michael.name = 'Lucy'
Michael.printInfo() # Name: Lucy, Score: 98
'无法(正常)访问私有变量，应该通过API来操作'
# print(Michael.__score) # AttributeError: 'Student' object has no attribute '__score
# print(Michael._Student__score) # 98 (不建议，python解释器不一样，这个_Student__score的名字可能不一样)
# Michael._Student__score = 80 # 非常不建议
# Michael.printInfo() # Name: Lucy, Score: 80 # 非常不建议
# Michael.__score = 80 # 这里相当于给instance新创建了一个__score的变量，并不是内部的private __score变量
# Michael.printInfo() # Name: Lucy, Score: 98 # 所以这里依然返回内部的private __score变量
print(Michael.getScore()) # 98 # 通过API访问
Michael.setScore(80) # 通过API修改
Michael.printInfo() # Name: Lucy, Score: 80
