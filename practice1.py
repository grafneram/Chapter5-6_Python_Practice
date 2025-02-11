#check if each num is prime in list
# return True if all numbers are prime, otherwise False


def test(nums):
    return all(is_prime(i) for i in nums)

# Define a function named 'is_prime' that checks if a number 'n' is prime
def is_prime(n):
    if (n == 1): # if n is 1 then it is NOT prime
        return False
    elif (n == 2): # if n is 2 then it IS prime
        return True
    else:
        for x in range(2, n):  # go through numbers from 2 to 'n' - 1
            if (n % x == 0):  #'n' is divisible by 'x', it's NOT prime
                return False
        return True


nums = [0, 3, 4, 7, 9]
print(nums)
print(test(nums))

nums = [3, 5, 7, 13]
print(nums)
print(test(nums))
