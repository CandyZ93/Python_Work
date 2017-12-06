def func(x):
	return x*x*x-x-1

def dfunc(x):
	return 3*x*x-1
	
def main():
	x0 = eval(input("Please enter x0 to start.\n"))
	epsilon=0.00001
	x_n=x0
	x_n1=x_n-(func(x_n)/dfunc(x_n))
	Err=x_n1-x_n
	counter=1
	while(abs(Err)>epsilon):
		x_n=x_n1
		x_n1=x_n-(func(x_n)/dfunc(x_n))
		Err=x_n1-x_n
		counter+=1
	
	print(x_n)
	print(x_n1)
	print(counter)
    

if __name__ == "__main__":
	main()
