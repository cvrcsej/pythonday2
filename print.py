print((1.1+2.2) == 3.3)
a = 90
if (a >= 90):
    print('die')
print('no')
''''''
match value:
    case pattern1:
        # code block
    case pattern2:
        # code block
    case _:
        # default code block
def get_day_name(day_number):
    match day_number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number"

print(get_day_name(3))  # Output: Wednesday

def get_grade(score):
    match score // 10:
        case 10 | 9:
            return 'A'
        case 8:
            return 'B'
        case 7:
            return 'C'
        case 6:
            return 'D'
        case _:
            return 'F'

print(get_grade(85))  # Output: B
