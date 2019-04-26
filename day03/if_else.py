
def if_demo():
    # 3大于2 所以 a 是 True
    a = 3 > 2
    # a是 True ,所以条件成立 打印 zhen ,
    # 如果a是 false  条件不成立 走else 分支 ,打印 jia
    if a:
        print('zhen')
    else:
        print('jia')

def ifel_demo():
    # 赋值 a 为6
    a = 1

    if a == 1:  # 判断 a是否等与1
        print('a是1')
    elif a == 2:    # 判断 a是否等与2
        print('a是2')
    elif a == 3:    # 判断 a是否等与3
        print('a是3')
    elif a == 4:    # 判断 a是否等与4
        print('a是4')
    elif a == 5:    # 判断 a是否等与5
        print('a是5')
    else:           # 如果 a 都不满足上面的条件 ,则 走else
        print('a是%s'%a)
    print('if结束')

def if_demo3():
    a =5
    if a<8 and a>3 :
        print('嘎嘎嘎嘎嘎')


def if_demo4():
    a =5
    if a<8 or a>3 :
        print('嘎嘎嘎嘎嘎')

def if_demo5():
    a =5
    if not a<8 :
        print('嘎嘎嘎嘎嘎')

if __name__ == '__main__':
    if_demo5()