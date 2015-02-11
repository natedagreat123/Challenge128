def is_prime(n): 
    n = abs(int(n))

    if n > 1:   
       for i in range(2,n):
           if (n % i) == 0:
               return False
               break    
       return True
    elif n == 1 or n == 0:
        print("That number has no factors!")
        factorizer()
  
def factorizer():
    num = input("Give me a number to factor ", )
    num = abs(int(num))
    factor = []
    
    if is_prime(num) is True:
        print("The factors of ",num,"are 1 and ", num)
        
    else:
        factor += "1"
        for i in range(2,num):
            if (num % i) == 0:
                factor.append(str(i))
        factor.append(str(num))
        if num > 1:
            print("The factors of ",num,"are ",factor)

factorizer()
