creature = input()
a = int(input())
b = int(input())

min_tot = 60*24*365
heartbeats = a*b*min_tot

tem = '{} have {:.2f} billion heartbeats'
print(tem.format(creature, heartbeats/1e9))