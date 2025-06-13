# 1)მომხმარებელს შემოაყვანინე რიცხვი და დაბეჭდე, დადებითია თუ უარყოფითი.


ricxvi = int(input("sheiyvane nebismieri ricxvi"))

if ricxvi < 0:
    print("uaryofitia")
elif ricxvi > 0 :
    print("dadebitia")


# 2)მომხმარებელს შემოაყვანინე რიცხვი და დაბეჭდე კენტის შემთხვევაში კენტი ლეწის შემთხვევაში ლუწი


cifri = int(input("sheiyvane raime ricxvi ; "))

if cifri % 2 == 0 :
    print("luwi")
else : 
    print("kenti")








# 4)მომხმარებელს შემოაყვანინე გამოცდის ქულა თუ მიიღო 100 დაბეჭდოს მალადეც თუ მიიღო 50 ნაკლები ვერ ჩააბარე 


score = int(input("dawere sheni migebuli qula"))

if score > 50 and score <100 :
    print("maladec")
elif score < 50 :
    print("ver chaabare")
