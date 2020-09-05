def is_prime(n):

	if n == 1:
		return False

	elif n < 4:
		return True

	elif n % 2 == 0:
		return True
	elif n < 9:
		return True
	elif n % 3 == 0:
		return False
	else:
		r = int(n**0.5)
		f = 5
		while f<= r:
			if n % f == 0:
				return False

			if n % (f+2) == 0:
				return False

			f += 6

	return True


limit = 10001
count = 1
candidate = 1

while 1:
	candidate += 2
	if is_prime(candidate):
		count += 1

	if count == 10001:
		break

print(candidate)