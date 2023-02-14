n = int(input('vvedite 3h znachnoe chislo --> '))

sum = 0

while n > 0:
    s = n % 10
    sum = sum + s
    n = int(n / 10)

print(f"Sum is {sum}!")
