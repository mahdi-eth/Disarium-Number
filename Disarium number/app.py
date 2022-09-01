from operator import indexOf


def disarium_checker(n):
    str_n = str(n)
    result = 0
    for i in str_n:
        power = indexOf(str_n, str(i))
        result += pow(int(i),power + 1 )
    if result == n: print("Yes, this is disarium number.") 
    else: print(f"No, this is not a disarium number (answer is : {result} ).") 

n = abs(int(input("Enter a number to see if it is a disarium number : ")))
disarium_checker(n)