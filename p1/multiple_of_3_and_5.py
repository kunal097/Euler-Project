N = 1000
result = sum((i for i in range(N) if i%3==0 or i%5==0))
print(result)
