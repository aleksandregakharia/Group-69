# 1)მომხმარებელს შემოაყვანინეთ რიცხვი x   დაბეჭდეთ 1 დან x 

x = int(input("ricxvi"))

i = 1
while i <= x :
    print(i) 
    i += 1


# 2)მომხმარებელს შემოაყვანინეთ რიცხვიზ   x და 1 დან x დე დაპრინტეთ


L = int(input("sheiyvane ucnobi ricxvi"))


for i in range(1 , L + 1 ) :
    print(i)


# 3)დაბეჭდეთ 2 რის ჯერადი რიცხვები    რომლებიც ნაკლებია 100 '


for j in range(0, 101 , 2):
    print(j)


# 4)დაითვალე რამდენი ლუწი რიცხვიან 1   - 50 

k = 2
f = 0
while k < 50 :
    f += 1
    k += 2
    print(k , f)


# 5)გამოიტანეთ 10 გოა ტოპ 


A = 0
while A < 10 :
    print("GOA TOP")
    A = A + 1
    