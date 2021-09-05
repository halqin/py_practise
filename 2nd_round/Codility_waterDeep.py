# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    max_array = []
    deep = []
    for i in range(len(A)-1):
        if A[i+1] <= A[i]:
            max_array.append(A[i]) #find the first top 
            for j in range(i,len(A)-1):
                if A[j] < max_array[-1]:
                
                    



    return print(max_array)       

solution([1,3,2,1,2,1,5,3,3,4,2])









