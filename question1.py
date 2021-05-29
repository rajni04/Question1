#Use python lists and make an list of numbers.
#Write a function which returns sum of the list of numbers

def sum_list(items):
    sum=0
    for x in items:
        sum += x
    return sum   
my_list = [10, 20, 14]
print("sum_list", sum_list(my_list))
