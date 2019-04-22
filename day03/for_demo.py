
alist = ['哈','楼','wo','de',1,2,3]

def for_demo():
    # for (关键字) i(变量名,代表循环次数)  in(关键字)  range( 迭代器函数 )
    for i in range(5):
        print(i)
        print('hello world')

def for_demo1():
    # 两个参数时:  从第一个参数开始计数,到第二个参数的前一位 停止
    for i in range(3,6):
        print(i)

    for j in range(5,11):
        print(j)

def for_demo2():
    # 三个参数时:  从第一个参数开始计数,到第二个参数的前一位 停止 。 每次循环 递增 参数三
    # for i in range(3,10,2):
    #     print(i)

    for j in range(11,5,-2):
        print(j)

# 遍历 : 就是 对列表中的每个元素 都做一次操作
def for_list():
    for i in alist:
        print(i)

# 第二种遍历方式
def for_list2():
    # 获取list的长度
    a = len(alist)
    # 通过长度设置 循环次数
    # 把 i 当作索引值来遍历元素
    for i in range(a):
        print(alist[i])

if __name__ == '__main__':

    for_list()