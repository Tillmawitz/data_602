import random

global global_count
global_count = 0

def rectangle_measures(length, width):
    return (2 * length) + (2 * width), length * width

def is_even(num):
    if ((num % 2) == 0):
        return "even"
    else:
        return "odd"

def count_case(string):
    if (type(string) != str):
        raise ValueError("Input was not a string")
    upper = 0
    lower = 0
    for letter in string:
        if(letter.isupper()):
            upper += 1
        elif(letter.islower()):
            lower += 1

    return upper, lower

def sum_list(num_list):
    sum = 0
    for num in num_list:
        if (type(num) is int):
            sum += num
    
    return sum

def local_vs_global(input_num):
    global global_count
    this_is_local = 0
    this_is_local += input_num
    global_count = global_count + input_num
    print(f"The local count is: {this_is_local} while the global count is: {global_count}")

def random_product(arg):
    return arg * random.random()

def main():
    rec_mes = rectangle_measures(4, 5)
    print(f"The perimeter is {rec_mes[0]} and the area is {rec_mes[1]}")
    
    print(f"5 is {is_even(5)} and 4 is {is_even(4)}")

    input_string = "CUNY sps"
    num_letters = count_case(input_string)
    print(f"There are {num_letters[0]} upper case and {num_letters[1]} lower case letters in {input_string}")
    input_string = "RaNdOm LeTtErS"
    num_letters = count_case(input_string)
    print(f"There are {num_letters[0]} upper case and {num_letters[1]} lower case letters in {input_string}")

    list_nums = [1,2,3,4,5]
    print(f"The sum of {list_nums} is {sum_list(list_nums)}")

    local_vs_global(1)
    local_vs_global(1)
    local_vs_global(1)

    print(random_product(2))
    print(random_product(2))
    print(random_product(2))

if __name__=="__main__":
    main()