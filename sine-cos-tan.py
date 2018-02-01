import math

deg1,deg2 = input("enter two numbers between 0 to 360 and use space to seprate two number: ").split(' ')
print("Sins, Cosine, Tangent values for degrees "+ deg1 + " to " + deg2 + " in steps of 5")

#try # have not done

deg1 = int(deg1)
deg2 = int(deg2)

column =["         "]
sin = ["Sine:    "]
cos = ["Cosine:  "]
tan = ["Tangent: "]

while deg1 <= deg2:

    column.append(deg1)

    #from degrees to radian
    radians = math.radians(deg1)

    sin.append(str(round(math.sin(radians),4)))

    cos.append(str(round(math.cos(radians),4)))

    tan.append(str(round(math.tan(radians),4)))

    deg1 = deg1 +5

# table
table = [column] + [sin] + [cos] + [tan]

for i, d in enumerate(table):
    line = '|'.join(str(x).center(7) for x in d)
    print(line)
    print('-' * len(line))



####################################################
#function to count negative number


del sin[0]
del cos[0]
del tan[0]

def change_to_float(sct):
    for i in range(len(sct)):
        sct[i] = float(sct[i])

change_to_float(sin)
change_to_float(cos)
change_to_float(tan)


print("Number of Negative Sine values: " + str(sum(n <0 for n in sin)))
print("Number of Negative Cosine values: " + str(sum(n <0 for n in cos)))
print("Number of Indeterminate Tangent values: ")
