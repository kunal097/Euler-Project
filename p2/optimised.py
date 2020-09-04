# This eq. follow E(n) = 4*E(n-1) + E(n-2)

limit = 4000000

a= 2
b = 8

sum = 10

while  sum < limit:

	
	c = 4*b + a
	# print(c)
	# input()
	sum += c
	a=b
	b=c

print(sum)