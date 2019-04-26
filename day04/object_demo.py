
class Animal (object):
    def chifan3(self):
        print('XX吃饭')

    def shuijiao2(self):
        print('XX睡觉')

class Human (object):

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def chifan(self):
        print('%s吃饭'%self.name)



    def shuijiao(self):
        print('%s睡觉'%self.name)




class Tester (Human,Animal):

    def work(self):
        self.chifan()
        print('%s在测试'%self.name)
        self.shuijiao()



if __name__ == '__main__':

    # animal = Animal()
    # animal.chifan()

    # human = Human('闫智楠',25,'男')
    # human.chifan()
    # human.shuijiao()
    # human.chifan()
    # print(human.sex)
    tester = Tester('闫智楠', 25, '男')
    tester.work()
    print(tester.sex)
