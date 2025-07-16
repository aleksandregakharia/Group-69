# 1)
# --ახსენი რისთვის გამოიყენება ინდექსინი, 
# --დაწერე ინდექსინგის  მაგალიათი ანუ შექმენი დიდი სია და გამოიყენე ინდექსინგი და დაპრინე მე 0-ინდექსი 1-ინდექსი 2-ინდექსი 3-ინდექსი 4-ინდექსი და ასევე 5 ჯერ შეუცვალე მნიშვნელობა სიაში არებულ ელემენტებს ინდექსინგის მეშვეობით

# index viyenebt rata gavigot tu meramdene elements vigebt da meramdene elementia tundac listshi romelime elementi


b = [ 1 , 2, 3, 4, 5, 6, 7, 8 , 9 , 10 , 11]

b[5] = 100

print(b[0:6])

# 2) 
# რას ეწოდება ფუნქცია?
# python ში ფუნქციის შექმინის დროს რატომ ვწერთ def-ს?
# def ის შემდეგ რა იწერება?
# რატომ უნდა გამოვიძახოთ ფუქნცია?
# funqcia aris rodesac kodi aketebs konkretul davalebas
# def vwert radgan shevqmnat funqcia phytonshi
# def is shemdeg iwereba funqciis saxeli
# radgan rac gvinda is rom gemochndes ekranze roca da ramdenjerac gvinda


def greet() :
    name = input("enter your name ; ")
    print("gamarjoba" + name)

greet()