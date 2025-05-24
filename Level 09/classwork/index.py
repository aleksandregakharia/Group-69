# 1)დაწერეთ while loop-ით კოდი რომელიც დაითვლის 1 დან 10 მდე


i = 0
while i < 10 :
    print(i + 1)
    i = i + 1


# 2) დაწერეთ while loop-თ კოდი რომელიც დაითვლის 10-1 მდე

a = 10
while a > 0  :
   print(a - 1)
   a = a - 1


#    3) დაწერეთ უსასრულო while loop


   while True :
       print("aleqs")


# 4) ახსენით კომენტარით რას შვება while loop 
# while loop aris programistvis igive gameorebis brdzaneba raime rom gaimeoros


# 5)მომხმარებელს სთხოვე შეიყვანოს პაროლი. სწორი პაროლია "1234". სანამ სწორად არ შეიყვანს, კოდი მუდმივად სთხოვს ახლიდან შეყვანას while loop-ის საშუალებით.


paswword = 1234
user_password = input("please enter your password")
while user_password != paswword :
      user_password = input("try your password again")
print("ACCEES GRANTED")


