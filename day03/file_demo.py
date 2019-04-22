
if __name__ == '__main__':
    # w+ : 覆盖内容
    # text_io = open('test.text', 'w+')
    # text_io.write('呵呵呵呵呵呵')

    # a+ : 追加内容
    text_io = open('test.text', 'a+')
    text_io.write('呵呵呵呵呵呵')

    # r  : 只可以读取 不能写入
    text_io = open('test.text', 'r')
    # readline() 读取一行
    # readline = text_io.readline()
    # print(readline)
    # 读取所有行 ,返回一个list
    readlines = text_io.readlines()
    print(readlines[2])
