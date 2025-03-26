'''def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i 
    return result

print(iterative_factorial(4))'''






'''def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * (factorial(n - 1))
print(factorial(4))'''



'''def factorial(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1))
num = int(input())
print(factorial)'''


'''list_of_nums = [int(n) for n in input().split()]

def add_list(my_list):
    if len(my_list) == 1:
        return my_list[0]
    else:
        return my_list[0] + add_list(my_list[1:])
print(add_list(list_of_nums))'''

'''final = []
def Fibonacci(num):
    if num <= 1:
        return num
    else:
        return(Fibonacci(num-1) + Fibonacci(num-2))
length = int(input("Enter numbers"))

for i in range(length):
    final.append(Fibonacci(i))
print(final)'''