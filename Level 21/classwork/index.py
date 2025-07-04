# 1)შემოატანინე მომხმარებელს რიცხვი და თუ უარყოფითი იყო ეგ რიცხვი დაბეჭდე შენ ტოლმისთვის მზად არ ხარ თუ დადებითია დაბეჭდე ოხ რამხელა ბიჭი ხარ ცოლის მოყვანას როდის აპირებ 

a = int(input("sheni asaki"))

if a < 0 :
    print("shen tolmistvis mzad ar xar")
elif a > 0 :
    print("ox ramxela biwi xar coli rodis mogyavs")


# 2)შემოატანინე მომხმარებელს რიცხვი და მაგ 10 და დაითვალოს უკუღმა  

r = int(input("sheiyvane ricxvi"))

for i in range(r, 0, -1):
    print(i)


# 3)გამოატანინე მომხმარებელს ნადირი ვარ ნადირი 6 ჯერ


n = 0
while n < 6:
    print("nadiri var nadirii")
    n = n + 1


# 4)შექმენი list სადაც ეწერება georgia და გამოიტანე მხოლოდ gia

l = [ "Georgia"]

print( l[4 : ])


# 5)შექმენით list სადაც იქნება თქვენი საყვარელი მენტორები და დაპრინტეთ საუკეთესო მენტორები4

m = ["batoni ioane" , "batoni gurami" , "batoni aleksandre"]

print(m[0 ],m[1],  m[2]  )