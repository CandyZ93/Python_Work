def nfunc(x):
	return (x+1)**(1/3) #Noted x=x^3+1 will not converge
	
def main():
	x0 = eval(input("Please enter x0 to start.\n"))
	epsilon=0.0001
	x_n=x0
	#x_n1 = nfunc(x_n)
	#Err=x_n1-x_n
	counter=0
	Flag=True
	while(Flag):
		x_n1 = nfunc(x_n)
		Err=x_n1-x_n
		
		if abs(Err)>epsilon:
			x_n=x_n1
			counter+=1
			print("times", counter)
			print("\t", x_n)
			print("\t", x_n1)
		else:
			Flag = False
		
		
		
	print("Converged root:")
	print("\t",x_n)
	print("\t",x_n1)
	print("\t Total iterate times:",counter)
    

if __name__ == "__main__":
	main()

