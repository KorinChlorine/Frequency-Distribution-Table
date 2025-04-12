data, sample, total, lowest, highFreq = 0, 0, 0, 0, 0
frequency, key, dataList, mode = int(0), "", [], []
classLimit_upper, classLimit_lower, midpoint, commutative_freq, classes = 0, 0, 0, 0, 0

while True:
    # This block asks inputs for the data table
    try:
        data = int(input("---\nEnter Data (-1 to stop): "))
    except:
        print("ERROR: Input integers only")
        continue
    # Checks for a '-1' input to stop the loop for asking an input for the data table
    if data == -1:
        break
    # Checks for an input of any negative number other than one and outputs an error message
    # and continues asking for user input
    if data <= -2:
        print("ERROR: Input -1 to stop")
        continue
    # for every iteration, +1 is added to the value for sample which serves as the size of the sample table
    sample += 1
    dataList.append(data)
    print(dataList)

upper, lower = dataList[0], dataList[0]

# Asks for the user input on how many classes to split the data into.
while True:
    try:
        classes = int(input("---\nEnter how many classes: "))
        if classes == 0:
            raise Exception
        break
    # An invalid input will show an error message and ask for input again
    except:
        if classes == 0:
            print("---\nERROR: Classes cannot be 0")
        else:
            print("---\nERROR: Input integers only")
        continue

# The programmers couldn't use .min and .max functions as they hadn't been taught yet,
# so they used a manual for loop instead.
for num in dataList:
    if num > upper:
        upper = num
    if num < lower:
        lower = num

# Computing ranges and other necessary data was easy and didn't require any special methods.
ranges = upper - lower
class_width = -((-ranges / classes) // 1)
class_mark = (upper + lower) / 2
classLimit_lower = lower
classLimit_upper = classLimit_lower - 1

# \n denotes a new line, this is to have the output be nicer to look at
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nData:", dataList)

arranged = dataList
arranged.sort()
print("Arranged Data:", arranged)

mode, highFreq = [], 0
for num in set(dataList):
    freq = dataList.count(num)
    if freq > highFreq:
        highFreq = freq
        mode = [num]
    elif freq == highFreq:
        mode.append(num)

for f in range(classes):

    frequency = 0
    classLimit_upper += class_width
    cBoundary_lower, cBoundary_upper = float(classLimit_lower - 0.5), float(classLimit_upper + 0.5)
    classLimit = str(int(classLimit_lower)) + "-" + str(int(classLimit_upper))

    for index in dataList:
        if classLimit_lower <= index <= classLimit_upper:
            frequency += 1

    midpoint = (classLimit_upper + classLimit_lower) / 2
    relative_freq = round((float(frequency) / len(dataList)), 3)
    commutative_freq += frequency

    # The programmers found that using "\t" serves a similar function to space bars, but they discovered that using " " was messier.
    # Thus, this was used to print the Frequency table.
    table = ("+===========================================----- FREQUENCY TABLE -----=============================================+"
             "\nCLASS LIMIT \t\tFREQUENCY \t\tCLASS BOUNDARY \t\tMID POINT \t\tRELATIVE FREQUENCY \t\tCOMMUTATIVE FREQUENCY")
    info = (classLimit + "\t\t\t\t\t" + str(frequency) + "\t\t\t\t" + str(cBoundary_lower) + "-" + str(cBoundary_upper) +
            "\t\t\t" + str(midpoint) + "\t\t\t" + str(relative_freq) + "\t\t\t\t\t\t " + str(commutative_freq) + "\t\t\t\t")
    # Code below is used to create the borders of the table
    if key != "stopped":
        print(
            "\n\n+===================================================================================================================+\n"
            + table +
            "\n+-------------------------------------------------------------------------------------------------------------------+")
        key = "stopped"
    print(info)
    # Code to increment the lower class limit with the class width
    classLimit_lower += class_width
else:
    print(
        "+===================================================================================================================+")
    print("\n Range:", ranges, "\n", "Lower Limit:", lower, "\n", "Upper Limit:", upper)
    print(" Population/Sample Size:", sample, "\n", "Class Width:", int(class_width), "\n NO of Classes:", classes)
    for num1 in dataList:
        total += num1
    else:
        mean = total / len(dataList)
        # Getting median by extracting the middle of the arranged data list
        middle = sample // 2
        if sample % 2 == 0:
            median = (arranged[middle] + arranged[~middle]) / 2
        else:
            median = arranged[middle]
        print(" Mean:", round(mean, 3), "\n Median:", median)
        # If all frequencies are the same then it will return "No mode"
        if len(mode) == sample:
            print(" Mode: No mode")
        else:
            print(" Mode:", *mode)
        if classLimit_upper <= upper:
            print("\n\nERROR: The maximum value is lower than the upper class limit\n"
                  "Thus, it is advisable to increase the number of classes or class width.")
