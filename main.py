def absent_person_shamer(student_name='Ammar Yaser'):
    print(f'Shame on you {student_name} for being abscent')


absent_person_shamer('Ali Ghalib')
absent_person_shamer('Ahmed Mohammad')
absent_person_shamer()


def combine_two_numbers(num1, num2):
    print(num1 + num2)
    return num1 + num2

combine_two_numbers(num2 = 4, num1 = 10)



def take_order(order_number, person_name, *args):
    print(f'{person_name} has ordered drink #{order_number} Extra Instructions: ')
    for instruction in args:
        print(instruction)



take_order(5, 'Omar','extra milk','no sugar')
take_order(3, 'Sayed Hamed','extra sugar')
take_order(3, 'Ammar')


print(max(4,3,22,100,66,1000))


def search(model,**kwargs):
    print(model)
    print(kwargs)


search('Submarines', region='Bahrain', is_active=True)

search('Submarines')


# Exercise 1
# 1. Wrte a function that calculates area of triangle. It should take in base and height. formula: (base * height)/2


# Exercise 2:
# Write  a function that takes many or 1 argument and adds all the numbers together

def sum_of_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

print(sum_of_numbers(1,8))


def double_number(number):
    return number * number

print(double_number(5))

# SAME as Function above
square_number_again = lambda number : number * number

my_nums = [1,7,19,25,3,2]

squared_nums = list(map(lambda number : number * number,my_nums))

print(squared_nums)
