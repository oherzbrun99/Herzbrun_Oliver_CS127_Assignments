def collatz(number):
    while number != 1:
        if number % 2 == 0:
            print(number // 2)
            return number // 2
        
        elif number % 2 == 1:
            print(3*number + 1)
            return 3*number+1
        
n = input("Enter number:")
while n != 1:
    n=collatz(int(n))