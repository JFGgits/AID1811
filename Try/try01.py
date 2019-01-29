# 1.	写一个程序，让用户输入两个以上的正整数，当输入负数时结束输入
#      （要求：限制用户，不允许输入重复的数）
# 1）	打印这些数字的和
# 2）	打印这些数中最大的一个数
# 3）	打印这些数中第二大的一个数
# 4）   删除最小的一个数
L = []	
def mysum(L):
    m1 = 0
    for i1 in L:
        m1 += i1
    return m1
def mymax(L):
    m2 = 0
    for i2 in L:
        if i2 > m2:
            m2 = i2
    return m2
def mymax2(L):
    L1 = L.copy()
    m3 = 0
    L1.remove(mymax(L1))
    for i3 in L1:
        if i3 > m3:
            m3 = i3
    return m3
def del_min(L):
    L2 = L.copy()
    m4 = min(L2)
    # for i4 in L:
    #     if i4 < m4:
    #         m4 = i4
    L2.remove(m4)
    return L2
def jisuan():
    global L
    while True:
        a = int(input('请输入一个正整数：'))
        if a < 0:
            if len(L) <= 2:
                continue
            else:
                break
        if a in L:
            print('已经输入过这个数！')
            continue
        L += [a]
    print('这些数字的和＝',mysum(L))
    print('这些数字中最大的数＝',mymax(L))
    print('这些数字中第二大的数＝',mymax2(L))
    print('删除最小的一个数后还有：',del_min(L))
    print(L)

jisuan()