def cube(number):
    return number*number*number
def divisble_by_three(number):
    if number %3==0:
        return cube (number)
    else:
        return False
print(divisble_by_three(9))
print(divisble_by_three(3))