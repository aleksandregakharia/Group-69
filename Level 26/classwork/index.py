# 1)შექმენი ფუნქცია is_positive, რომელიც იღებს ერთ რიცხვს არგუმენტად. თუ ეს რიცხვი დადებითია, დააბრუნოს True, სხვა შემთხვევაში კი False.
# 👉 გამოიყენე პირობითი ოპერატორები (if, else). 


is_positive = int(input("sheiyvane ricxvi"))

def is_number_positive(input_number):
    if input_number > 0:
        return True
    else:
        return False
    
# 2)დაწერე ფუნქცია max_of_two, რომელიც იღებს ორ რიცხვს და აბრუნებს მათგან დიდს. გამოიყენე მხოლოდ if,else

def get_max_value(first_value, second_value):
    if first_value > second_value:
        return first_value
    else:
        return second_value


# 3)დაწერე ფუნქცია max_of_three, რომელიც იღებს სამ მთელ რიცხვს და აბრუნებს მათგან უდიდესს.
# 👉 გამოიყენე if-elif-else პირობები და შედარებები.

def maximum_of_three_numbers(num_one, num_two, num_three):
    if num_one >= num_two and num_one >= num_three:
        return num_one
    elif num_two >= num_one and num_two >= num_three:
        return num_two
    else:
        return num_three


# 4)დაწერე ფუნქცია is_hot, რომელიც იღებს ერთ რიცხვს (ტემპერატურა გრადუსებში) და აბრუნებს True, თუ ტემპერატურა 30 ან მეტია, ხოლო False — სხვა შემთხვევაში


def is_hot(temperature_celsius):
    if temperature_celsius >= 30:
        return True
    else:
        return False
