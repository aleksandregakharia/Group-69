# 1) კომენტარებით ახსენით რაში გამოიყენება join და split ფუნქცია, და დაწერე join ზე და split ზე 1 მაგალითი მინიმუმ
#  joinit shegvidzlia listi gadavaqciot stringat ert did winadadebat xolo splitis dros piriqit stringi listad


sentence = "The quick brown fox jumps over the lazy dog."
words_list = sentence.split(" ")
print(words_list)


words = ["apple" , "banana" , "cherry"]
words1 = ", ".join(words)
print(words1)


# 2) შექმენი ფუნქცია sum_two_number რომელიც იღებს 2 არგუმენტს a და b ს და აბრუნებს მათ ჯამს


def sum_two_number(a , b) :
    return a + b 

print(sum_two_number(10 , 47))