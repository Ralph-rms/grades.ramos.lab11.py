counter = 0
passed = 0 
list = []

for x in range(5):
    NUM = int(input("Enter the grades of 5 students"))
    if NUM <= 39 or NUM >= 101:
        print("invalid input. number must be between 40 and 100")
        break
    else:
        list.append(NUM)
    if NUM >= 75: 
        passed += 1
        counter += 1 
    else:
        counter += 1
    if counter == 5:
        print()
        sumNums = sum(list)
        averageGrade = sumNums / 5
        averageGrade = round(averageGrade, 2)
        
        PassingPercentage = (passed / len (list)) * 100
        PassingPercentage = round(PassingPercentage, 2)
        
        print("GIven Grade: " + str(list))
        print("Average Grade: " + str(averageGrade))
        print("Number of Students who passed:" + str(passed))
        print("percentage of the studenrs who passed:" + str(PassingPercentage) + "%") 