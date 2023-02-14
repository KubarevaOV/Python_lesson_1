n = int(input('Vvedite kolichestvo juravlikov --> '))

if n%2 != 0:
    print(f"Ne sootvetstvueet usloviyam!")
else:
    jM = n / 3 / 2
    jG = n - (n / 3)

    print(f"Mal'chiki sdelali po {jM}, a devochka {jG} juravley")