# # Iteration

# n_terms = int(input("How many terms the user wants to print? "))

# #First 2 terms
# n_1 = 0
# n_2 = 1
# count = 0

# #Now we will check if the number of terms is valid or not
# if n_terms <= 0:
# 	print("\nPlease enter a positive integer, the given number is not valid")
# elif n_terms == 1:
# 	print("\nThe fibonacci seq of the numbers up to", n_terms,":")
# 	print(n_1)
# else:
# 	print("\nThe fibonacci sequence of the numbers is:")
	
# 	while count < n_terms:
# 		print(n_1)
# 		nth = n_1 + n_2
# 		#At last, we will update values
# 		n_1= n_2
# 		n_2 = nth
# 		count += 1
		
#Fib sequence

def fibonacci_of(n):
	if n in {0,1}: # 2 base cases
		return n
	return fibonacci_of(n - 1) + fibonacci_of(n - 2) # 2 recursive calls
	
print([fibonacci_of(n) for n in range(15)])