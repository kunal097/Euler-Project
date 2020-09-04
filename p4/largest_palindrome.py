# n1 = 999
# n2 = 999

# while n1 >= 100:
# 	while n2 >= 100:

res = (i*j for i in range(100,1000) for j in range(100,1000) if str(i*j) == str(i*j)[::-1])

print(max(res))