nums = range(1,21)

min_num = 2*3*5*7*11*13*17*19

final_num = None

drop = False

while True:
	
	for i in nums:
		if min_num % i != 0:
			drop = True
			break 

	if not drop:
		final_num = min_num
		break
	drop = False
	min_num += 1

print(final_num)