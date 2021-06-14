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
    