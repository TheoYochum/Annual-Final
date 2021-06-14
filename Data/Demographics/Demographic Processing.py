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

