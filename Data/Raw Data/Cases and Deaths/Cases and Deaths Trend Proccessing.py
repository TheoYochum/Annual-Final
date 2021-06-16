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

for i in range(len(text)):
    print(text[i])