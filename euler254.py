#gets the sum of the factorials of the characters of an integer.
def f(num):
    a = str(num)
    digit_map = map(int, a)
    num_list = list(digit_map)
    list_sum = 0
    for i in range(0, len(num_list)):
        list_sum = list_sum + factorial(num_list[i])
    return list_sum
#gets the sum of the characters of the output of f().
def sf(num):
 
    b = str(f(num))
    digit_map_1 = map(int, b)
    num_list_1 = list(digit_map_1)
    
    the_sum = 0
    for i in range(0, len(num_list_1)):
        the_sum = the_sum + num_list_1[i]
    return the_sum
    
#to get the factorial of a number.
def factorial(b):
    if b == 0:
        fact = 1
    else:
        if b-1 > 0:
            n = b-1
        else: 
            n = b
        fact = b * n
        while n > 0:
            if n != b-1:
                fact = fact * n
            n = n-1      
    return fact

def g(c):
    guess = 0
    while sf(guess) != c or guess == 0:
        guess = guess + 1
    return guess

def sg(c):

    b = str(g(c))
    digit_map_2 = map(int, b)
    num_list_2 = list(digit_map_2)
    
    total = 0
    for i in range(0, len(num_list_2)):
        total = total + num_list_2[i]
    return total

def summation(n, m):
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + sg(i)
    return the_sum % m

print (summation(20, 1000000))

print(g(3))
