
if __name__ == '__main__':

    alist = [2,1,4,3,5,7,6]
    for i in range(len(alist)):
        for j in range(i):
            n = alist[j]
            m = alist[j+1]
            if n <= m :
                continue
            temp = alist[j]
            alist[j] = alist[j+1]
            alist[j + 1] = temp

    print(alist)