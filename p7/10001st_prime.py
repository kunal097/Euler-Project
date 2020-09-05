def is_prime(n):

	for i in range(2, n/2 +1):
		if n % i == 0:
			return False

	return True



# print(is_prime(8))

index = 1
num = 1

while True:

	num += 2

	if is_prime(num):
		index += 1

	if index == 10001:
		break

print(num)


