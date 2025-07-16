# 1. მისალმების ფუნქცია
# შექმენი ფუნქცია, რომელიც არაფერს იღებს და კონსოლში ბეჭდავს ტექსტს: „გამარჯობა!“.

def misalmeba() :
    print("gamarjoba!")


# 2. ორის შეკრება
# შექმენი ფუნქცია, რომელსაც გადაეცემა ორი რიცხვი და აბრუნებს მათ ჯამს.


def shekreba(a, b):
    return a + b


# 3. ლუწი თუ კენტი
# შექმენი ფუნქცია, რომელიც იღებს ერთ რიცხვს და აბრუნებს სტრიქონს: „ლუწია“ თუ რიცხვი ლუწია, ან „კენტია“ თუ კენტია.


def romelia(l):
    return "luwi" if l % 2 == 0 else "kenti"

# სახელი და ასაკი
# შექმენი ფუნქცია, რომელიც იღებს მომხმარებლის სახელსა და ასაკს, და ბეჭდავს ტექსტს, მაგ: „მარიამი არის 25 წლის.“


def shenia_monafemebi(saxeli, wlovaneba):
    saxeli = input("sheni saxeli")
    wlovaneba = input("sheni wlovaneba")
    print(saxeli , "aris" ,  wlovaneba , "wlis")    


# 5.მაქსიმალური მნიშვნელობა
# შექმენი ფუნქცია, რომელიც იღებს სამ რიცხვს და აბრუნებს ყველაზე დიდს მათ შორის.


def ricxvi():
    a = int(input("sheiyvane erti ricxvi: "))
    b = int(input("meore ricxvi: "))
    c = int(input("mesame ricxvi: "))
    print("aqedan yvelaze didi ricxvi:", max(a, b, c))