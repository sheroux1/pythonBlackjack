from unicodedata import digit

def expanded_form(num):
    tens =10
    sep_nums = [str(num) % tens for x in range(len(str(num))) for num -= (num % tens) tens *= 10]
    
    # for x in range(len(str(num))):
    #     sep_nums.append(str(num % tens))
    #     num -= (num % tens)
    #     tens *= 10
    return ' + '.join(sep_nums[::-1])

# def expanded_form(num):
#     zeros = len(str(num)) -1
#     digits = str(num)
#     print(digits[0])
#     return_string = ''
#     for digit in digits:
#         return_string += digit
#         for num in range(zeros):
#             return_string += '0'
#             num -= 1
#         zeros -= 1
#         if zeros >= 0:
#             return_string += ' + '
#     return return_string.strip()

print(expanded_form(1234))
