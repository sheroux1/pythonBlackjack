def diamond(n):
    diamond_string = ''
    x =0
    # n is also the number of rows
    if n % 2 == 0 or n < 0:
        return None
    else:
        for x in range(n):
            diamond_string += '*'
            x += 1
        return diamond_string

print(diamond(5))