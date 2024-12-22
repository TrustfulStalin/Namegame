import random

firstname = {"Chad", "Bookie", "Terry", "Marri", "Jude", "Tevon", "Chloe", "Taliah"}
lastname = {"Musgrow", "Gaddy", "Ewing", "Talbert", "Lucus"}


fname = random.choice(list(firstname))
Nname = random.choice(list(lastname))


print("Your first name is: " + fname)
print("Your last name is: " + Nname)
print("Your whole name is: " + fname + "-" + Nname)