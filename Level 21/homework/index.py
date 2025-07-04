# 1)შემოაყვანინეთ მომხმარებელს n რიცხვი და დაპრინტეთ ყველა რიცხვი ნოლიდან n+1-მდე

n = int(input("sheiyvane ricxvi"))

m  = 0
while m <= n + 1:
    print(m)
    m =m + 1


# 2)მომხმარებელს შემოაყვანინე რიცხვი და დაბეჭდე კენტის შემთხვევაში კენტი ლეწის შემთხვევაში ლუწი


g = int(input("Nebismieri ricxvi: "))

if g % 2 == 0:
    print("luwi")
else:
    print("kenti")
    


# 3)შექმენი for loop- რომელიც გამოიტანს 1-100 ჩატვლით რიცხვებს და ასევე კენტია თუ ლუწი ეს რიცხვი.


for i in range(1, 101):
    print(i, ";- luwi" if i % 2 == 0 else "; kenti")



# 4)მომხმარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ უფრო მაღალი რიცხვი 


ricxvi1 = int(input("sheiyvane ricxvi"))
ricxvi2 = int(input("sheiyvane meore ricxvi"))

if ricxvi1 > ricxvi2 :
    print(ricxvi1)
elif ricxvi1 < ricxvi2 :
    print(ricxvi2)



# 5)გამოიტანეთ მომხმარებლის შემოყვანილი სახელი 10-ჯერ იტერაციის მეშვეობით


saxeli = str(input("tqveni saxeli"))

for i in range (10) :
    print(saxeli)