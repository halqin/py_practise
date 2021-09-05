# def isbn():
#     #x=[]
#     #x.append(input('ISNB #'))
#     acc = 0
#     x1 = input()
#     cnt = 1
#     while x1 != 'stop':
#         if cnt != 10:
#             acc += int(x1)*cnt 
#             cnt +=1
#         else:
#             if x1 == cnt % 11:
#                 print("OK")
#             else:
#                 print("WRONG")
#             cnt = 0
#         x1 = input()
       
# if __name__=="__main__":
#     # import doctest
#     # doctest.testmod()
#     isbn()

acc = 0
x1 = input()
cnt = 1
while x1 != 'stop':
    if cnt != 10:
        acc += int(x1)*cnt 
        cnt +=1
    else:
        if x1 == acc % 11:
            print("OK")
        else:
            print("WRONG") 
        cnt = 19
        
        acc = 0
    x1 = input()

