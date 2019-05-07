
if __name__ == '__main__':

    alist = [2,1,4,3,5,7,6]
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j] <= alist[j+1] :
                continue
            temp = alist[j]
            alist[j] = alist[j+1]
            alist[j + 1] = temp
    print(alist)