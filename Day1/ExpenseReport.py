
target = 2020

print("The target is: " + str(target))

f = open("input.txt")
data = f.readlines()
f.close()



def main():
    value1 = None
    value2 = None
    dataCopy = data[:]
    foundPair = False

    precount = str(len(dataCopy))

    for x in data:
        #iterate through list and get values   
        
        value1 = int(dataCopy.pop(0))
        for element in dataCopy:
            value2 = int(element)
            
            if sumOfValues(value1, value2) is True:
                foundPair = True
                break
        if foundPair == True:
            print("found pair")
            print("value 1: " + str(value1) + " value 2: " + str(value2))
            
            product = value1 * value2
            print("product: " + str(product))
            return


    if foundPair == False:
        print("no pair found")
        # if len(dataCopy)


def sumOfValues(value1, value2):
    sum = value1 + value2
    # outputString = str(value1) + " + " + str(value2) +  " = " + str(sum)

    # with open("output.txt", "a") as myfile:
    #     myfile.write(outputString + "\n")

    if sum == target:
        return True
    return False

if __name__ == "__main__":
    main()

