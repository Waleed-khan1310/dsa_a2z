def sum_of_divisors_upto_n(N):
    # Step 1: Create an array to store sum of divisors for each number
    sum_divisors = [0] * (N + 1)

    # Step 2: Use a modified sieve approach to calculate sum of divisors
    for d in range(1, N + 1):
        for multiple in range(d, N + 1, d):
            sum_divisors[multiple] += d

    # Step 3: Sum up all the divisor sums to get the final result
    result = sum(sum_divisors[1:])  # sum from index 1 to N
    return result

# Example usage
N = 3
print(sum_of_divisors_upto_n(N))


def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)
 
a = 60
b = 48
 
# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (computeGCD(60, 48))
    