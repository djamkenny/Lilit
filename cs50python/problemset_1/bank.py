greet = input("Greetings: ").capitalize() #capitalize the first letter

slice = slice(1)
n = greet[slice] # select the first letter
m = tuple(greet)[1:] # select the all the letter first one exclusive

#condition for greetings

if (greet == "Hello" or greet == "hello"):
    print("$0")
elif (n == "H" and m != "ello"):
    print("$20")
else: print("$100")