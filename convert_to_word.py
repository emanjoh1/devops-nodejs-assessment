## Python script for convert_to_word 
def convert_to_word(num):
    if num == 10:
        return 'ten'
    elif num == 20:
        return 'twenty'
    elif num == 30:
        return 'thirty'
    elif num == 40:
        return 'forty'
    elif num == 50:
        return 'fifty'
    elif num == 60:
        return 'sixty'
    elif num == 70:
        return 'seventy'
    elif num == 80:
        return 'eighty'
    elif num == 90:
        return 'ninety'
    else:
        return str(num)

for i in range(101):
    if i % 10 == 0 and i != 0:
        print(convert_to_word(i))
    else:
        print(i)
