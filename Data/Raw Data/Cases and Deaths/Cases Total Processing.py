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

# for i in range(len(text[0])):
#     print(text[0][i] + ' ' + str(i))

for i in range(len(text)):
    print(text[i])
