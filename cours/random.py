import random 

a = random.randint(0,21)
b = random.randint(0,21)
print(a)
print(b)
if a > b: 
    print("Le nombre b est plus grand que le nombre a.")
elif a < b: 
    print("Le nombre a est plus grand que le nombre b")
elif a == b:
    print("Le nombre a et le nombre b sont égaux.")
