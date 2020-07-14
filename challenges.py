# You must make a program that read a float-point number and print a message
# saying in which of following intervals the number belongs:
# [0,25] (25,50], (50,75], (75,100].
# If the read number is less than zero or greather than 100,
# the program must print the message “Fora de intervalo” that means "Out of Interval".
#
# The symbol '(' represents greather than. For example:
# [0,25] indicates numbers between 0 and 25.0000, including both.
# (25,50] indicates numbers greather than 25 (25.00001) up to 50.0000000.

#read a float number

number = float(input())

#dictionare of possible intervals

intervals = {"0": "0,25",
             "1": "25,50",
             "2": "50,75",
             "3": "75,100"}


for i in range(4):
    if float(intervals.get("{}".format(i)).split(",")[0]) <= number <= float(intervals.get("{}".format(i)).split(",")[1]):
        if (i == 0):
            print("Intervalo [0,25]")
            break
        else:
            print("Intervalo ({},{}]".format(intervals.get("{}".format(i)).split(",")[0], intervals.get("{}".format(i)).split(",")[1]))
            break
else:
    print("Fora de intervalo")


