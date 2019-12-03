
def showMaxFactor(num):
    count   = round(num/2,0)
    while count > 1:
        if num % count == 0:
            print("Largest factor of %i is %i" % (num, count))
            break
        count -= 1
    else:
        print(num, "is a prime number")

for eachN in range(100,110):
    showMaxFactor(eachN)