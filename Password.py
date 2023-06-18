import random, string
lenth =   int(input("Enter the lenth of pass : ,"))
uperD = string.ascii_lowercase
lowerD = string.ascii_uppercase
digitD = string.digits
symbolD = string.punctuation
dataD = uperD + lowerD + digitD + symbolD
x = random.sample(dataD,lenth)
y = "".join(x)
print(y)
