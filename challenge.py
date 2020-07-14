#get the input
import math

a,b,c = [float(i) for i in input().split()]

# calculate bhaskara's formula
# delta = b**2 - 4ac
delta = b**2 - 4 * a * c

if a == 0 or delta < 0:
    print("Impossivel calcular")
else:

#calculate the roots

    x_1 = (-b + math.sqrt(delta)) / (2*a)

    x_2 = (-b - math.sqrt(delta)) / (2*a)

    print("R1 = {:.5f}".format(x_1))
    print("R2 = {:.5f}".format(x_2))