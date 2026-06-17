# Task 1
def hello ():
    return "Hello!"

# Task 2
def greet(name):
    return f'Hello, {name}!'

# Task 3
def calc(num1, num2, operator="multiply"):
    try:
        match operator:
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "multiply":
                return num1 * num2
            case "divide":
                return num1 / num2
            case "modulo":
                return num1 % num2
            case "int_divide":
                return num1 // num2
            case "power":
                return num1 ** num2
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
# Task 4
def data_type_conversion(value, type):
    try:
        match type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."
    
# Task 5
def grade(*args):
    try:
        sum_args = sum(args)
    except TypeError:
        return "Invalid data was provided."
    else:
        average = sum_args / len(args)

    match average:
        case num if num >=90:
            return "A"
        case num if 79 < num < 90:
            return "B"
        case num if 69 < num < 80:
            return "C"
        case num if 59 < num < 70:
            return "D"
        case num if num < 60:
            return "F"

# Task 6
def repeat(string, count):
    new_string = ""
    for i in range(count):
        new_string = new_string + string
    return new_string

# Task 7
def student_scores(info_request, **kwargs):
    if info_request == "best":
        top_student = ""
        top_score = 0
        for key, value in kwargs.items():
            if value > top_score:
                top_score = value
                top_student = key
        return top_student
    elif info_request == "mean":
        sum = 0
        for value in kwargs.values():
            sum += value
        mean = sum / len(kwargs.values())
        return mean
    
# Task 8
def titleize(title):
    words = title.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    for i, word in enumerate(words):
        if i == 0 or word not in little_words or i == len(words) - 1:
            words[i] = words[i].capitalize()
    words = " ".join(words)
    return words

# Task 9
def hangman(secret, guess):
    clue = ""
    for i in secret:
        if i in guess:
            clue = clue + i
        else:
            clue = clue + "_"
    return clue

# Task 10
def pig_latin(entry):
    entry = entry.split()
    vowels = "aeiou"
    prefix = ""
    current_word = ""
    for i, word in enumerate(entry):
        cons = True
        for letter in word:
            if cons == True:
                if letter not in vowels:
                    prefix = prefix + letter
                    continue
                elif letter == "u" and "q" in prefix:
                    prefix = prefix + letter
                    continue
                else:
                    cons = False
            current_word = current_word + letter
        current_word = current_word + prefix + "ay"
        entry[i] = current_word
        prefix = ""
        current_word = ""
    phrase = " ". join(entry)
    return phrase
