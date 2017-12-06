nums=list(range(1,10))

def myPrint(n):
	if n == 1:
		print(str(n)+'st')
	elif n == 2:
		print(str(n)+'nd')
	elif n == 3:
		print(str(n)+'rd')
	else:
		print(str(n)+'th')
		
for num in nums:
	myPrint(num)
