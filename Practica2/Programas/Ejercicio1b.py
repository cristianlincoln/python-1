for num in range(1, 111):
    if num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
        print (num, end = " ")
    if num%11 == 0:
        print()
    else:
        if num%3 == 0:
            print("Cosa" , end = "")
        if num%5 == 0:
            print("Losa", end = "")
        if num%7 == 0:
            print("Wosa", end = "")
    
        print(" ", end = "")
        
        
        
        
            
