with open('Vaccination Trends.csv', 'r') as text:
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
