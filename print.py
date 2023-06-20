# a = int(input("Enter a number :"))
# for i in range (1,(a+1)):
#     print(i,end=" ")


# a = []
# for j in range(1,21):
#     a.append(j)

# ev = []

# odd = []

# for i in a:
#     if i%2 == 0:
#         ev.append(i)
   
#     else:
#         odd.append(i)
        
# print(ev)  

# print(odd)


# email = input("Ente a email add : \n")
# user = email[:email.index("@")]
# domain = email[email.index("@")+1:]
# print(user)
# print(domain)


# import qrcode                                           # This is use to generate qr code
# img = qrcode.make("hello Akshita, Navya & Jyoti")
# img.save("familys.jpeg")

# eml = "anandmgs@gmail.com"
# c = eml.index("@")
# i = 0
# while (i < c):
    
#     print(eml[i],end="")
#     i += 1
# z = eml[c+1::]
# print(z)


# a = "anand"                   # This code is reverse the string
# b = []

# for i in range(len(a)-1,-1,-1):
#      b.append(a[i])
# print(b)
    

# a = "anand"           # This code is reverse the string
# b = []

# for i in reversed(a):
#      b.append(i)
# print(b)
        

# a = "anandmgs@gmail.com"

# c = []
# for k in range(a.index("@")):
#     c.append(a[k])
# print(c)    

# b = []
# for i in range(a.index("@")+1,len(a)):
#     b.append(a[i])
# print(b)
    

# fruit = ["apple","Bannana","mango","kiwi","lichi"]
# f = []

# for i in fruit:
#     i=i.upper()
#     f.append(i)
           
# print(f)    
    
    
# def dis(item):
#     k = []
#     for i in item:
#         i = i.upper()
#         k.append(i)
        
#     return k  
     
# fruit = ["apple","Bannana","mango","kiwi","lichi"]
# print(dis(fruit)) 


# def cell_Fer(C):
#     F = C*9/5 + 32 
#     return F

# def Fer_Cell(F):
#     C = (F-32)*5/9
#     return C

# Fer = int(input("Enter the Ferenhite value : "))
# cel = int(input("Enter the celcious vallue : "))
# print("The Ferenhite value of given cellcious is ",round(cell_Fer(cel),2))
# print("he Cellcious value of given Ferenhite  is ",round(Fer_Cell(Fer),2))

# from currency_converter import CurrencyConverter
# c = CurrencyConverter()
# print((c.convert(100,"USD","INR")))


# from tkinter import *
# win = Tk()
# win.title("welcome")
# win.geometry("500x300")
# l1 = Label(win,text="calculator",font=("Arial bold",30),bg="red", fg="white")
# l1.pack(TOP)


# win.mainloop()


# from tkinter import *

# window = Tk()
# window.minsize(600,400)
# window.maxsize(600,400)
# window.title('Calculator')


# # This is a main function of this program and all the code 
# def main_function():
#     op= str(operation.get())
#     number_1 = int(num_1.get())
#     number_2 = int(num_2.get())

#     if op=='+':
#         answer.config(text=f'{number_1} {op} {number_2} = {number_1+number_2}')

#     elif op=='-':
#         answer.config(text=f'{number_1} {op} {number_2} = {number_1 - number_2}')

#     elif op=='*':
#         answer.config(text=f'{number_1} {op} {number_2} = {number_1 * number_2}')

#     elif op=='/':
#         answer.config(text=f'{number_1} {op} {number_2} = {number_1 / number_2}')

#     else:
#         answer.config(text=f'Please enter a valid number')



# heading = Label(window,text='Calculator',font=('bold',50),bg='cyan')
# heading.pack(fill=X)

# num_1 = Entry(window,bg='light cyan',font=('normal',30),width=5)
# num_1.place(x=140,y=100)

# operation = Entry(window,bg='light cyan',font=('normal',30),width=1)
# operation.place(x=290,y=100)

# num_2 = Entry(window,bg='light cyan',font=('normal',30),width=5)
# num_2.place(x=360,y=100)

# button = Button(window,text='Enter',font=('bold',30),command=lambda:main_function())
# button.place(x=270,y=200)

# answer = Message(window,text=' ',font=('bold',30),width=600)
# answer.place(x=100,y=300)

# window.mainloop()


# import random, string
# lenth =   int(input("Enter the lenth of pass : ,"))
# uperD = string.ascii_lowercase
# lowerD = string.ascii_uppercase
# digitD = string.digits
# symbolD = string.punctuation
# dataD = uperD + lowerD + digitD + symbolD
# x = random.sample(dataD,lenth)
# y = "".join(x)
# print(y)


# # This code is use to count vowel from sentence
# sen = input("Enter a sentence to count the vowel : ").lower()
# vow = ["a","e","i","o","u"]
# count = 0
# for car in sen:
#     if car in vow:
#         count = count + 1
# print(count)        


# # This code is use to generate random password
# import random
# no = int(input("Enter the length of password :  "))
# a = ["a","b","c","d","e","f","g","h","i","j","k"]
# b = ["1","2","3","4","5","6","7","8","9","0"]
# c = ["!","@","#","$","&"]
# d = a+b+c
# e = random.sample(d,no)
# f = "".join(e).upper()
# print(f)



# class Mobile:
#     def __init__(self,m):
#         self.module = m
        
#     def Show_module(self,p):
#         self.price = p
#         print(f"module {self.module} price {self.price}") 

# redme = Mobile("Nokia")
# redme.Show_module(2000) 
# print()
# print(id(redme))          

