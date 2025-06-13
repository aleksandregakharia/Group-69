# 1)მომხმარებელს შეიყვანს თვის ნომერს (1-12) და პროგრამა ამოიცნობს სეზონს (ზამთარი, გაზაფხული, ზაფხული, შემოდგომა) 


season = int(input("Shemoiyvane sheni dabadebis tve 1-12 :"))

if season >= 3 and season <= 3 :
    print("zamtari")
elif season >= 4 and season <= 6:
    print("gazafxuli")
elif season >= 7 and season <= 9:
    print("zafxuli")
else :
    print("shemodgoma")


# 2)მომხარებელს შემოაყვანინეთ რიცხვი და დაადგინეთ უარყოფითია თუ დადებითი

ricxvi = int(input("sheiyvane nebismieri ricxvi"))

if ricxvi < 0:
    print("uaryofitia")
elif ricxvi > 0 :
    print("dadebitia")

# 3)ახსენი რა არის if else elife
# if aris Tu igive condetional statemant xolo elifi igive funqciit magram ifis magivrad unda gavaketot


# 4)მომხმარებლის ასაკი და შემოსავალი თუ ასაკი < 18 ან შემოსავალი < 10000 გათავისუფლებული ხარ სხვა შემთხვევაში გადასახადი გადასახდელია


age =int(input("sheiyvane asaki"))
salary = int(input("sheiyvane shemosavali"))

if age < 18 :
    print("araa gadasaxdeli")
elif salary > 1000 :
    print("gatavisuflebuli xar")
else :
    print("gadasaxdeli gadasaxdelia")


n =int(input("sheiyvane nbs ricxvi"))

if n > 10 :
    print ("metia")
elif n < 10 :
    print("naklebia") 

