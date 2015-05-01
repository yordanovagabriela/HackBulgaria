def prepare_meal(number):
    if number < 1:
        return "\"\""
    elif number % 3 == 0:
        counter = 1
        while number % 3**counter == 0:
            counter += 1
        meal = "spam " * (counter-1)
        if number % 5 == 0:
            meal += "and eggs"
        return "\"%s\"" % meal
    elif number % 5 == 0:
        return "eggs"
    else:
        return "\"\""
print(prepare_meal(45))
