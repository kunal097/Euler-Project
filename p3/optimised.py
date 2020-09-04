N = 600851475143

last_factor = 1
if N % 2 == 0:
	last_factor = 2

	while N %2 == 0:
		N /= 2

factor = 3
max_factor = N**0.5

while N > 1 and factor <= max_factor :

	if N % factor == 0:
		N /= factor
		last_factor = factor
		while N % factor == 0:
			N /= factor

		max_factor = N**0.5

	factor += 2


if N == 1:
	print(last_factor)

else:
	print(N)