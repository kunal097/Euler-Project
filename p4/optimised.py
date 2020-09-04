largest_palindrome = 0 

a = 999

while a >= 100:

	if a % 11 == 0:
		b = 999
		db = 1

	else:
		b = 990
		db = 11


	while b >= a:
			

		if a*b < largest_palindrome:
			break

		if str(a*b) == str(a*b)[::-1]:
			largest_palindrome = a*b

		b -= db

	a -= 1


print(largest_palindrome)
