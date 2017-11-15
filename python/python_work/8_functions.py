# Exercise 1. Creating a simple function
def double_it(number):
    return number * 2
print double_it(4)
print double_it(4.0)

# Exercise 2. Simple functions cont.
def calc_hypo(a, b):
    hypo = (a**2 + b**2)**0.5
    return hypo
print calc_hypo(3, 4)

# Exercise 3. Add checks into code
def calc_hypo(a, b):
    if type(a) not in (int, float) or type(b) not in (int, float):
        print "Bad argument"
        return False
    if a <= 0 or b <=0:
        print "Bad argument"
        return False

calc_hypo(0, -2)
calc_hypo("hi", "bye")

