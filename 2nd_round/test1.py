def conver1(alist, card_dic):
    for idx,val in enumerate(alist):
        # if val in card_dic:
        assert (val in card_dic), "wrong card range"
        alist[idx] = card_dic.get(val)
    # alist = list(map(int, alist))
    return alist

def solution1(A, B):
    assert (len(A) == len(B)), "different number of cards"
    assert (1<= len(A)<=1000), "wrong input length" 
    a_list = list(A)
    b_list = list(B)
    card_dic = {'A':14, 'K':13, "Q":12, 'J':11, 'T':10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}
    a_list = conver1(a_list, card_dic)
    b_list = conver1(b_list, card_dic)
    #print(a_list,b_list)
    cnt = 0
    for i in range(len(A)):
        if a_list[i] > b_list[i]:
            cnt +=1
    return cnt

# solution("A586QK","JJ653K")


def solution4(A, D):
    cnt = 0
    t = 0
    for i in reversed(A): # never jump to river
        if i == -1 and cnt <=D:
            if cnt == D:
                t = -1
                break
            else:
                cnt += 1
        else: 
            break 
    return t


#print(solution4([1,2,3,4,-1,6,-1],3))
print(solution4([1,-1,0,2,-1,-1,-1],3))
#print(solution4([3,2,1],1))





import math

def solution3(A):
    x=sum([A[i]*(-2)**(i) for i in range(len(A))])
    x_ceil = math.ceil(x/2)
    x_bits =number2bits(x_ceil)
    return x_bits

def number2bits(n):
    array = []
    while n:
        array.append(n & 1)
        n = -(n >> 1)
    return array


def solution(A):
    ls = []
    for i in range(len(A)):
        ls.append(A[i] * (-2) ** (i))
    x = sum(ls)
    x_ceil = math.ceil(x / 2)
    x_bits = number2bits(x_ceil)
    return x_bits


def number2bits(n):
    array = []
    while n:
        array.append(n & 1)
        n = -(n >> 1)
    return array