
if __name__ == '__main__':

    # 断言 字符串
    # print('成功' in '操作成功')
    # print('成功' not in '操作成功')
    #
    # # 断言 数字
    # a = 200
    # b = 200
    # print(a==b )
    # assert a ==b
    # print(a!=b )
    # assert a!=b

    # 处理异常
    try:
        5/0
        assert '成功1'  in '操作成功'
        print('XXXX')
    except:
        print('上面那个断言没通过')