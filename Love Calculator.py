user=input("Enter your name: ")
crush=input("Enter your crush's name: ")
name=(user+crush).lower()


first_half=0
second_half=0


for i in range(0, len(name) - 1):
    if (name[i] == "t" or name[i] == "r" or name[i] == "u" or name[i] == "e"):
        first_half += 1

    if (name[i] == "l" or name[i] == "o" or name[i] == "v" or name[i] == "e"):
        second_half += 1

print(f"Compatability = {str(first_half)+str(second_half)}%")            
        
        


user=input("Enter your name: ")
crush=input("Enter your crush's name: ")
name=(user+crush).lower()


first_half=0
second_half=0


for i in range(0, len(name) - 1):
    if (name[i] == "t" or name[i] == "r" or name[i] == "u" or name[i] == "e"):
        first_half += 1

    if (name[i] == "l" or name[i] == "o" or name[i] == "v" or name[i] == "e"):
        second_half += 1

print(f"Compatability = {str(first_half)+str(second_half)}%")            
        
        

