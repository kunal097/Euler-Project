N = 1000


def sum_divisible_by_num(num):
	p = int((N-1)/num)
	# print(p, '***')
	return num*(p*(p+1))/2


print(sum_divisible_by_num(3) + sum_divisible_by_num(5) - sum_divisible_by_num(15))
