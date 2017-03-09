number = 600851475143
devider = 2

for i in range(number):
    if number % devider == 0:
        number = number/devider
    elif number == 1:
        print(devider)
        break
    else:
        devider += 1
