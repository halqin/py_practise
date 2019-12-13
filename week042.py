num = int(input())
result = sum([2**(ord(input())-65) for _ in range(num)])
print('Bottle #{} is poisoned.'.format(result))