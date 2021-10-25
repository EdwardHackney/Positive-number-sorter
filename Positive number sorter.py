nums = []

running = True
UserInput = ""

print("1:Type a positive number if you want to add a number to the list\n2:Type check to see current numbers\n3:Type sort to sort from least to greatest\n4:Type quit to end the program")

def sort(numList):
    sortedList = []
    while len(numList) > 0:
        minimum = numList[0]
        for num in numList:
            if num < minimum:
                minimum = num
        numList.remove(minimum)
        sortedList.append(minimum)
    return sortedList

while running:
    UserInput = input()
    if UserInput.isnumeric():
        nums.append(int(UserInput))
        print("Number added")
    elif UserInput == "check":
        print(nums)
    elif UserInput == "sort":
        nums = sort(nums)
        print(nums)
    elif UserInput == "quit":
        running = False