def isPrime(n):	
	if n == 2 or n == 3:
		return True
	elif n%2 == 0 or n<2:
		return True
	elif:	
	
		for i in range(3, int(n**0.5)+1,2):
		if n%i == 0:
			return False

	return True

print(isPrime(25))
def prime_numbers(n):
	primes = [x for x in range(x) if isPrime(x)]
	return primes
print(prime_numbers(50))						