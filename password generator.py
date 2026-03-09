import random
import string
length=int(input("enter the password length:"))
password=""

characters=string.ascii_letters+string.digits+string.punctuation
for i in range(length):
    password+=random.choice(characters)
print("generate password:",password)

    
