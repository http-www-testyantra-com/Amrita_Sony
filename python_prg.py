# WAP to filter all the perfect square between he given nos.
def perfectSquare(n):
    return round(n ** 0.5) **2 ==n

print(list(filter(perfectSquare, [2,4,5,6,9,16,4.5])))

#WAP to convert the list of string to Uppercase using map
print("".join(list((map(lambda x:x.upper(),"heelo")))))

#WAP to filter the special symbol present in a string
print(list(filter(lambda ch: ch in "@#$!?*;", 'hello@#')))
