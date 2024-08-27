str = str(input("Enter a letter: "))
def not_string(str):
    if "not" in str == True:
        return str
    else:
        return "not" + str
    
print(not_string(str))
