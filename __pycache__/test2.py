def to_weird_case(string):
    string = string.split()
    return_string = []
    for word in string:
        weird_word = ''
        for index, letter in enumerate(word):
            if index % 2 == 0:
                weird_word += letter.upper()
            else:
                weird_word += letter.lower()
        return_string.append(weird_word)
    return " ".join(return_string)

print(to_weird_case("This is a String"))

#Other winners:
# def to_weird_case_word(string):
    #return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))

    # return_string = list(map(lambda x: x.upper() if indexEven(x) else x.lower(), string.split()))



    # for word in string:
    #     weird_word = []
    #     # print(word)
    #     x = 0
    #     for letter in word:
    #         # print(letter)
    #         if x % 2 == 0:
    #             weird_word.append(letter.upper())
    #         else:
    #             weird_word.append(letter.lower())
    #         x += 1
    #         return_string.append(weird_word)