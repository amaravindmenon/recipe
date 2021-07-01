def get_recipe(a):
    if (a == 1):
        print("Tea")
        print("Coffee")
        print("Sweet Lemon")
    elif (a == 2):
        print("Salty Lemon")
    elif (a == 3):
        print("Milk Shake")
        print("Tea")
        print("coffee")
        
print("SELECT YOUR Ingredient")
print("1 for Sugar")
print("2 for Salt")
print("3 for Milk")
x = int(input("Enter Number: "))
get_recipe(x)
 

rec = input("Enter Product: ")
get_recipe(rec)
if rec == "Tea":
    print("Add sugar + Water + Milk + Tea Powder")
elif rec == "Coffee":
    print("Add sugar + Water + Milk + Coffee Powder")
elif rec == "Sweet Lemon":
    print("Add sugar + Water + Lemon crushed or powder")
elif rec == "Salty Lemon":
    print("Add Salt + Water + Lemon crushed or powder")
elif rec == "Milk Shake":
    print("Add Milk + Flavour like chocolate or strawberry")
    
