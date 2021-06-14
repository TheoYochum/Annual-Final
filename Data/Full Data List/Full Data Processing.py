#Cases Trends Processing
with open('Cases Trends.csv', 'r') as text:
    text = text.read()

#Removes werid characters at the start
text = text[3:]

#Creates a 2d list
text = text.split('\n')
for i in range(len(text)):
    text[i] = text[i].split(',')
#Removes empty list at the end
text.pop()

#Removes United States Column and Histoic Cases Column
for i in range(len(text)):
    text[i].pop(0)
    text[i].pop()

#Covnerting dates to numerical values
for i in range(len(text)):
    if len(text[i][0]) == 10:
        if 'Jan' in text[i][0]:
            text[i][0] = '1/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Feb' in text[i][0]:
            text[i][0] = '2/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Mar' in text[i][0]:
            text[i][0] = '3/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Apr' in text[i][0]:
            text[i][0] = '4/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'May' in text[i][0]:
            text[i][0] = '5/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Jun' in text[i][0]:
            text[i][0] = '6/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Jul' in text[i][0]:
            text[i][0] = '7/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Aug' in text[i][0]:
            text[i][0] = '8/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Sep' in text[i][0]:
            text[i][0] = '9/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Oct' in text[i][0]:
            text[i][0] = '10/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Nov' in text[i][0]:
            text[i][0] = '11/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Dec' in text[i][0]:
            text[i][0] = '12/' + text[i][0][4:5] + '/' + text[i][0][6:]
    elif len(text[i][0]) == 11:
        if 'Jan' in text[i][0]:
            text[i][0] = '1/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Feb' in text[i][0]:
            text[i][0] = '2/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Mar' in text[i][0]:
            text[i][0] = '3/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Apr' in text[i][0]:
            text[i][0] = '4/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'May' in text[i][0]:
            text[i][0] = '5/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Jun' in text[i][0]:
            text[i][0] = '6/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Jul' in text[i][0]:
            text[i][0] = '7/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Aug' in text[i][0]:
            text[i][0] = '8/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Sep' in text[i][0]:
            text[i][0] = '9/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Oct' in text[i][0]:
            text[i][0] = '10/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Nov' in text[i][0]:
            text[i][0] = '11/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Dec' in text[i][0]:
            text[i][0] = '12/' + text[i][0][4:6] + '/' + text[i][0][7:]

#Flipping the list
text = [text[0]] + text[::-1]
text = text[:-1]
    
out = open('Cases Trends.txt', 'w')
out.write(str(text))
out.close()

###########################################

#Deaths Trends Processing
with open('Deaths Trends.csv', 'r') as text:
    text = text.read()

#Removes werid characters at the start
text = text[3:]

#Creates a 2d list
text = text.split('\n')
for i in range(len(text)):
    text[i] = text[i].split(',')
#Removes empty list at the end
text.pop()

#Removes United States Column and Histoic Cases Column
for i in range(len(text)):
    text[i].pop(0)
    text[i].pop()

#Covnerting dates to numerical values
for i in range(len(text)):
    if len(text[i][0]) == 10:
        if 'Jan' in text[i][0]:
            text[i][0] = '1/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Feb' in text[i][0]:
            text[i][0] = '2/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Mar' in text[i][0]:
            text[i][0] = '3/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Apr' in text[i][0]:
            text[i][0] = '4/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'May' in text[i][0]:
            text[i][0] = '5/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Jun' in text[i][0]:
            text[i][0] = '6/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Jul' in text[i][0]:
            text[i][0] = '7/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Aug' in text[i][0]:
            text[i][0] = '8/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Sep' in text[i][0]:
            text[i][0] = '9/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Oct' in text[i][0]:
            text[i][0] = '10/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Nov' in text[i][0]:
            text[i][0] = '11/' + text[i][0][4:5] + '/' + text[i][0][6:]
        if 'Dec' in text[i][0]:
            text[i][0] = '12/' + text[i][0][4:5] + '/' + text[i][0][6:]
    elif len(text[i][0]) == 11:
        if 'Jan' in text[i][0]:
            text[i][0] = '1/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Feb' in text[i][0]:
            text[i][0] = '2/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Mar' in text[i][0]:
            text[i][0] = '3/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Apr' in text[i][0]:
            text[i][0] = '4/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'May' in text[i][0]:
            text[i][0] = '5/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Jun' in text[i][0]:
            text[i][0] = '6/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Jul' in text[i][0]:
            text[i][0] = '7/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Aug' in text[i][0]:
            text[i][0] = '8/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Sep' in text[i][0]:
            text[i][0] = '9/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Oct' in text[i][0]:
            text[i][0] = '10/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Nov' in text[i][0]:
            text[i][0] = '11/' + text[i][0][4:6] + '/' + text[i][0][7:]
        if 'Dec' in text[i][0]:
            text[i][0] = '12/' + text[i][0][4:6] + '/' + text[i][0][7:]

#Flipping the list
text = [text[0]] + text[::-1]
text = text[:-1]

out = open('Deaths Trends.txt', 'w')
out.write(str(text))
out.close()

###########################################

#Cases Total Processing
with open('Cases and Deaths Total.csv', 'r') as text:
    text = text.read()
#Removes werid characters at the start
text = text[3:]

#Creates a 2d list
text = text.split('\n')
for i in range(len(text)):
    text[i] = text[i].split(',')
    
#Removes in order American Samoa, Federated States of Micronesia, Nothern Mariana Islands, Palau, Republic of Marshall Islands, Empty List
text.pop(4)
text.pop(11)
text.pop(27)
text.pop(43)
text.pop(44)
text.pop()

#Removes Irrelevant Collumn Entries Leaving only State/Territory, Total Cases, Cases per 100000, Total Deaths, Deaths per 100000
for i in range(len(text)):
    text[i].pop(2)
    text[i].pop(2)
    text[i].pop(2)
    text[i].pop(4)
    text[i].pop(4)
    text[i].pop(4)
    for ii in range(13):
        text[i].pop(5)

#Limits it to Cases
for i in range(len(text)):
    text[i] = text[i][:-2]

out = open('Cases Total.txt', 'w')
out.write(str(text))
out.close()


###########################################

#Deaths Total Processing

with open('Cases and Deaths Total.csv', 'r') as text:
    text = text.read()
#Removes werid characters at the start
text = text[3:]

#Creates a 2d list
text = text.split('\n')
for i in range(len(text)):
    text[i] = text[i].split(',')
    
#Removes in order American Samoa, Federated States of Micronesia, Nothern Mariana Islands, Palau, Republic of Marshall Islands, Empty List
text.pop(4)
text.pop(11)
text.pop(27)
text.pop(43)
text.pop(44)
text.pop()

#Removes Irrelevant Collumn Entries Leaving only State/Territory, Total Cases, Cases per 100000, Total Deaths, Deaths per 100000
for i in range(len(text)):
    text[i].pop(2)
    text[i].pop(2)
    text[i].pop(2)
    text[i].pop(4)
    text[i].pop(4)
    text[i].pop(4)
    for ii in range(13):
        text[i].pop(5)

#Limits it to Deaths
for i in range(len(text)):
    text[i] = [text[i][0]] + text[i][-2:]

out = open('Deaths Total.txt', 'w')
out.write(str(text))
out.close()

###########################################

#Vaccines Total Processing

with open('Vaccinations Total.csv', 'r') as text:
    text = text.read()

#Removes werid characters at the start
text = text[3:]

#Creates a 2d list
text = text.split('\n')
for i in range(len(text)):
    text[i] = text[i].split(',')
    
#Removes empty list at the end
text.pop()

#Removes Buearu of Prisons, Department of Defense, Federated States of Micronesia, Indian Health SVC, Veterans Health
text.pop(6)
text.pop(10)
text.pop(12)
text.pop(17)
text.pop(53)

#Removes Columns leaving only relevant

for i in range(len(text)):
    for ii in range(35):
        text[i].pop(27)
    for ii in range(8):
        text[i].pop(16)
    for ii in range(2):
        text[i].pop(14)
    for ii in range(2):
        text[i].pop(10)
    for ii in range(2):
        text[i].pop(6)
    for ii in range(3):
        text[i].pop(3)
    
out = open('Vaccinations Total.txt', 'w')
out.write(str(text))
out.close()

###########################################

#Vaccines Trends Processing

with open('Vaccinations Trends.csv', 'r') as text:
    text = text.read()

#Removes werid characters at the start
text = text[3:]

#Creates a 2d list
text = text.split('\n')
for i in range(len(text)):
    text[i] = text[i].split(',')
    
#Removes empty list at the end
text.pop()

#Removes every entry with Report as the Date Type as they only reprot the change in the 7-day average and 
for i in range(len(text))[::-1]:
    if text[i][0] == 'Report':
        text.pop(i)

#Omits all data from Long Term Care Facilities as combinging them with the rest of the data would be too difficult
for i in range(len(text))[::-1]:
    if text[i][2] == 'LTC':
        text.pop(i)

#Removes all Columns for Date Type, Program, Daily Counts of Dose 1 or 2, 7-day Average Dose 1 or 2, Daily Changes, Daily Count of Fully Vaccinated,
for i in range(len(text)):
    text[i].pop(0)
    text[i].pop(1)
    text[i].pop(2)
    text[i].pop(2)
    text[i].pop(3)
    text[i].pop(3)
    text[i].pop(3)
    text[i].pop(4)
    text[i].pop(4)
    text[i].pop(4)
    text[i].pop(4)

out = open('Vaccinations Trends.txt', 'w')
out.write(str(text))
out.close()

###########################################

#Demographics Processing

demographicList = ['Age', 'Ethnicity', 'Sex']

#Writes a text file for each group of deaths
for i in demographicList:
    with open(i + ' Deaths.csv', 'r') as text:
        text = text.read()

    #Removes werid characters at the start
    text = text[3:]

    #Creates a 2d list
    text = text.split('\n')
    for ii in range(len(text)):
        text[ii] = text[ii].split(',')
    
    #Removes Empty List
    text.pop()
    
    out = open(i + ' Deaths.txt', 'w')
    out.write(str(text))
    out.close()

#Writes a text file for each group of cases
for i in demographicList:
    with open(i + ' Cases.csv', 'r') as text:
        text = text.read()

    #Removes werid characters at the start
    text = text[3:]

    #Creates a 2d list
    text = text.split('\n')
    for ii in range(len(text)):
        text[ii] = text[ii].split(',')
    
    #Removes Empty List
    text.pop()
    
    out = open(i + ' Cases.txt', 'w')
    out.write(str(text))
    out.close()

#Writes a text file for each group of vaccinations
for i in demographicList:
    with open(i + ' Vaccination.csv', 'r') as text:
        text = text.read()

    #Removes werid characters at the start
    text = text[3:]

    #Creates a 2d list
    text = text.split('\n')
    for ii in range(len(text)):
        text[ii] = text[ii].split(',')
    #Removes last two columns as they are unecessary
    for ii in range(len(text)):
        text[ii] = text[ii][:-2]
    
    #Removes empty list
    text.pop()
    
    out = open(i + ' Vaccination.txt', 'w')
    out.write(str(text))
    out.close()