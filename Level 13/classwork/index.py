# 1)მომხმარებელს შემოატანინეთ 3 რიცხვი და გამოიტანეთ მაგ სამი რიცხვის ჯამი 


a = int(input("Shemoitane ricxvi"))
b = int(input("Shemoitane 2 ricxvi"))
c = int(input("Shemoitane 3 ricxvi"))


print(a + b + c)


# 2)დაბეჭდეთ რიცხვები 10 - 1 მდე

 
for i in range (112) :
    print(i)


# 3)დაბეჭდეთ 1- 100 რიცხვი მხოლოდ კენტები


for i in range(1 , 101 , 2) :
   print(i)


# 4)დაბეჭდეთ ყველა რიცხვი რომელიც 3 ზე უნაშთოდ იყოფა 1- 100


for i in range(1 , 101, 3) :
    print(i)


# 5)იპოვეთ 1 - 100 რიცხვის ჯამი


ik = 0 
for i in range(1 , 101) :
    ik += i
    print(ik)



