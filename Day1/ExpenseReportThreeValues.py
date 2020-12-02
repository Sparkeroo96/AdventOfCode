
target = 2020

print("The target is: " + str(target))

f = open("input.txt")
data = f.readlines()
f.close()



def main():
    value1 = None
    value2 = None
    value3 = None
    dataCopy = data[:]
    foundCombo = False

    precount = str(len(dataCopy))

    for x in data:
        #iterate through list and get values   
        
        value1 = int(dataCopy.pop(0))
        thirdData = dataCopy[:]
        for element in dataCopy:
            value2 = int(element)
            
            for finalElement in thirdData:
                value3 = int(finalElement)

                if sumOfValues(value1, value2, value3) is True:
                    foundCombo = True
                    break

            if foundCombo is True:
                break


        if foundCombo == True:
            print("found pair")
            print("value 1: " + str(value1) + " value 2: " + str(value2) + " value 3: " + str(value3))
            
            product = value1 * value2 * value3
            print("product: " + str(product))
            return


    if foundCombo == False:
        print("no pair found")
        # if len(dataCopy)


def sumOfValues(value1, value2, value3):
    
    sum = value1 + value2 + value3

    if sum == target:
        print("value1 " + str(value1))
        print("value2 " + str(value2))
        print("value3 " + str(value3))
        print("sum" + str(sum))
        print("target" + str(target))
        return True
    return False

if __name__ == "__main__":
    main()

