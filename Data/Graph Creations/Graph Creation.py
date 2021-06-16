import matplotlib.pyplot as plt

# #template
# #####################################################
# 
# #Name
# 
# with open('filename.txt', 'r') as data:
#     data = data.read()
# data = eval(data)

def axis(datain, index):
    axisout = []
    for i in range(1, len(data)):
        axisout.append(datain[i][index])
    return axisout, datain[0][index]

#Bar plot basics
# plt.clf()
# xaxis, xlabel = axis(data, xindex)
# yaxis, ylabel = axis(data, yindex)
# for i in range(len(yaxis)):
#     yaxis[i] = int(yaxis[i])
# print(xaxis)
# print(yaxis)
#plt.bar(xaxis, yaxis)


# #####################################################
# 
# # Cases Total
# 
# with open('Cases Total.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# data = data[:-1]
# 
# #Sets axes
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 1)
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = int(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# #Sets ticks and labels
# plt.xticks(rotation=45, size = 15, ha='right')
# plt.yticks(ticks = range(0, 3800000, 500000), labels = range(0, 3800000, 500000), size = 15)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel(ylabel, size = 25)
# plt.suptitle('The Cases of COVID-19 per US State/Territory', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# 
# #plt.show()
# plt.savefig('Cases Total', bbox_inches = 'tight')
# plt.clf()
# 
# ######################################################
# 
# #Deaths Total
# 
# with open('Deaths Total.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# data = data[:-1]
# 
# #Sets axes
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 1)
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = int(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# #Sets ticks and labels
# plt.xticks(rotation=45, size = 15, ha='right')
# plt.yticks(size = 15)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel(ylabel, size = 25)
# plt.suptitle('The Deaths due to COVID-19 per US State/Territory', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# 
# #plt.show()
# plt.savefig('Deaths Total', bbox_inches = 'tight')
# plt.clf()
# 
# #####################################################
# 
# #Cases Per 100000
# 
# with open('Cases Total.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# #Sets axes
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 2)
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = int(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# #Sets ticks and labels
# plt.xticks(rotation=45, size = 15, ha='right')
# plt.yticks(size = 15)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel(ylabel, size = 25)
# plt.suptitle('The Cases of COVID-19 per US State/Territory Accounting for Population', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# 
# #plt.show()
# plt.savefig('Cases Population', bbox_inches = 'tight')
# plt.clf()
# 
# ######################################################
# 
# #Deaths Per 100000
# 
# with open('Deaths Total.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# #Sets axes
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 2)
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = int(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# #Sets ticks and labels
# plt.xticks(rotation=45, size = 15, ha='right')
# plt.yticks(size = 15)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel(ylabel, size = 25)
# plt.suptitle('The Deaths due to COVID-19 per US State/Territory Accounting for Population', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# 
# #plt.show()
# plt.savefig('Deaths Population', bbox_inches = 'tight')
# plt.clf()
# 
# #####################################################
# 
# #Vaccination Total
# 
# with open('Vaccinations Total.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# # for i in range(len(data)):
# #     print(data[i])
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 1)
# 
# xlabel = 'State/Territory'
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = int(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# #Sets ticks and labels
# plt.xticks(rotation=45, size = 15, ha='right')
# plt.yticks(ticks = range(0, 50000000, 5000000), labels = range(0, 50000000, 5000000), size = 15)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel(ylabel, size = 25)
# plt.suptitle('Vaccines delivered to each State/Territory', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# 
# #plt.show()
# plt.savefig('Vaccinations Total', bbox_inches = 'tight')
# plt.clf()
# 
# #####################################################
# 
# #Vaccination Total
# 
# with open('Vaccinations Total.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# # for i in range(len(data)):
# #     print(data[i])
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 2)
# 
# xlabel = 'State/Territory'
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = int(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# #Sets ticks and labels
# plt.xticks(rotation=45, size = 15, ha='right')
# plt.yticks(size = 15)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel(ylabel, size = 25)
# plt.suptitle('Vaccines delivered to each State/Territory Accounting for Population', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# 
# #plt.show()
# plt.savefig('Vaccinations Population', bbox_inches = 'tight')
# plt.clf()
# 
# 
# #####################################################
# 
# #Full vs One Dose
# 
# with open('Vaccinations Total.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 4)
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 6)
# 
# xlabel = 'State/Territory'
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots again
# plt.bar(xaxis, yaxis, alpha = 0.5, color = 'r')
# 
# #Sets ticks and labels
# plt.xticks(rotation=45, size = 15, ha='right')
# plt.yticks(size = 15)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel('Percentage of Population', size = 25)
# plt.suptitle('Percentage Population Partially Vaccinated vs Fully Vaccinated by State/Territory', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# plt.legend(['Fully Vaccinated', 'Partially Vaccinated'])
# 
# #plt.show()
# plt.savefig('Vaccination Dosage Comparison', bbox_inches = 'tight')
# plt.clf()
# 
# #####################################################
# 
# #Pfizer vs Moderna vs Janssen
# 
# with open('Vaccinations Total.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# moderna = 0
# pfizer = 0
# janssen = 0
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# for i in range(1, len(data) - 1):
#     moderna += int(data[i][7])
#     pfizer += int(data[i][8])
#     janssen += int(data[i][9])
# 
# plt.figure(figsize=(25,15))
# plt.bar(['Moderna', 'Pfizer', 'Janssen'], [moderna, pfizer, janssen])
# 
# 
# plt.xticks(size = 20)
# plt.yticks(ticks = range(0, 75000000, 10000000), labels = range(0, 75000000, 10000000), size = 20)
# plt.xlabel('Type of Vaccine', size = 25,)
# plt.ylabel('Number of People Fully Vaccinated', size = 25)
# plt.suptitle('Full Vaccinations per Vaccine Type', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# plt.subplots_adjust(left = 0.112, bottom = 0.07, right = 0.97, top = 0.91, wspace = 0.2, hspace = 0.2)
# plt.tight_layout()
# 
# #plt.show()
# plt.savefig('Vaccination Type Comparison', bbox_inches = 'tight')
# plt.clf()
# 
# 
# #####################################################
# 
# #Vaccine Trends
# 
# with open('Vaccinations Trends.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# xaxis, xlabel = axis(data, 0)
# 
# yaxis, ylabel = axis(data, 1)
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# plt.figure(figsize=(25,15))
# 
# plt.bar(xaxis, yaxis)
# 
# yaxis, ylabel = axis(data, 3)
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# plt.plot(xaxis, yaxis, color = 'r')
# 
# plt.xticks(rotation = 45, ticks = xaxis[::2], ha = 'right', size = 10)
# plt.yticks(ticks = range(0, 4500000, 500000), labels = range(0, 4500000, 500000), size = 20)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel('Doses Administered Daily', size = 25)
# plt.suptitle('The Change in Vaccines Administered per Day', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# plt.legend(['7-Day Average', 'Vaccinations per Day'])
# 
# plt.subplots_adjust(left = 0.112, bottom = 0.07, right = 0.97, top = 0.91, wspace = 0.2, hspace = 0.2)
# plt.tight_layout()
# 
# #plt.show()
# plt.savefig('Vaccination Trends', bbox_inches = 'tight')
# plt.clf()
# 
# #####################################################
# 
# #Deaths Trends
# 
# with open('Deaths Trends.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# xaxis, xlabel = axis(data, 0)
# 
# yaxis, ylabel = axis(data, 1)
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# plt.figure(figsize=(25,15))
# 
# plt.bar(xaxis, yaxis)
# 
# yaxis, ylabel = axis(data, 2)
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# plt.plot(xaxis, yaxis, color = 'r')
# 
# plt.xticks(rotation = 45, ticks = xaxis[::7], ha = 'right', size = 15)
# plt.yticks(ticks = range(0, 4500, 500), size = 20)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel('Deaths', size = 25)
# plt.suptitle('The Change COVID 19 Deaths per Day', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# plt.legend(['7-day Average', 'Deaths per Day'])
# 
# plt.subplots_adjust(left = 0.112, bottom = 0.07, right = 0.97, top = 0.91, wspace = 0.2, hspace = 0.2)
# plt.tight_layout()
# 
# #plt.show()
# plt.savefig('Deaths Trends', bbox_inches = 'tight')
# plt.clf()
# 
# #####################################################
# 
# #Cases Trends
# 
# with open('Cases Trends.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# xaxis, xlabel = axis(data, 0)
# 
# yaxis, ylabel = axis(data, 1)
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# plt.figure(figsize=(25,15))
# 
# plt.bar(xaxis, yaxis)
# 
# yaxis, ylabel = axis(data, 2)
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# plt.plot(xaxis, yaxis, color = 'r')
# 
# plt.xticks(rotation = 45, ticks = xaxis[::7], ha = 'right', size = 15)
# plt.yticks(size = 20)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel('Cases', size = 25)
# plt.suptitle('The Change COVID 19 Cases per Day', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# plt.legend(['7-day Average', 'Cases per Day'])
# 
# plt.subplots_adjust(left = 0.112, bottom = 0.07, right = 0.97, top = 0.91, wspace = 0.2, hspace = 0.2)
# plt.tight_layout()
# 
# #plt.show()
# plt.savefig('Cases Trends', bbox_inches = 'tight')
# plt.clf()
# 
# #####################################################
# 
# #Age Cases
# 
# with open('Age Cases.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 3)
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# yaxis, ylabel = axis(data, 1)
# 
# #xlabel = 'State/Territory'
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots again
# plt.bar(xaxis, yaxis, alpha = 0.5, color = 'r', width = 0.6)
# 
# plt.xticks(size = 20)
# plt.yticks(size = 20)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel('Percentage of Population', size = 25)
# plt.suptitle('Age Based Percentage of Population Compared to Percentage of Cases', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# plt.legend(['Percent of US Population', 'Percent of Cases'])
# 
# #plt.show()
# plt.savefig('Age Cases', bbox_inches = 'tight')
# plt.clf()
# 
# #####################################################
# 
# #Sex Cases
# 
# with open('Sex Cases.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 3)
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# yaxis, ylabel = axis(data, 1)
# 
# #xlabel = 'State/Territory'
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots again
# plt.bar(xaxis, yaxis, alpha = 0.5, color = 'r', width = 0.6)
# 
# plt.xticks(size = 20)
# plt.yticks(size = 20)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel('Percentage of Population', size = 25)
# plt.suptitle('Sex Based Percentage of Population Compared to Percentage of Cases', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# plt.legend(['Percent of US Population', 'Percent of Cases'])
# 
# #plt.show()
# plt.savefig('Sex Cases', bbox_inches = 'tight')
# plt.clf()
# 
#####################################################

#Ethnicity Cases

with open('Ethnicity Cases.txt', 'r') as data:
    data = data.read()
data = eval(data)

# for i in range(len(data[0])):
#     print(data[0][i] + ' ' + str(i))

xaxis, xlabel = axis(data, 0)
yaxis, ylabel = axis(data, 3)

#Converts yaxis to integers
for i in range(len(yaxis)):
    yaxis[i] = float(yaxis[i])

#Plots
plt.figure(figsize=(25,15))
plt.bar(xaxis, yaxis)

yaxis, ylabel = axis(data, 1)

#xlabel = 'State/Territory'

#Converts yaxis to integers
for i in range(len(yaxis)):
    yaxis[i] = float(yaxis[i])

#Plots again
plt.bar(xaxis, yaxis, alpha = 0.5, color = 'r', width = 0.6)

plt.xticks(size = 15)
plt.yticks(size = 20)
plt.xlabel(xlabel, size = 25,)
plt.ylabel('Percentage of Population', size = 25)
plt.suptitle('Ethnicity Based Percentage of Population Compared to Percentage of Cases', size = 30)
plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')

#Formating
plt.tight_layout()
plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
plt.legend(['Percent of US Population', 'Percent of Cases'])

#plt.show()
plt.savefig('Ethnicity Cases', bbox_inches = 'tight')
plt.clf()

# 
# #####################################################
# 
# #Age Deaths
# 
# with open('Age Deaths.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 3)
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# yaxis, ylabel = axis(data, 1)
# 
# #xlabel = 'State/Territory'
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots again
# plt.bar(xaxis, yaxis, alpha = 0.5, color = 'r', width = 0.6)
# 
# plt.xticks(size = 20)
# plt.yticks(size = 20)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel('Percentage of Population', size = 25)
# plt.suptitle('Age Based Percentage of Population Compared to Percentage of Deaths', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# plt.legend(['Percent of US Population', 'Percent of Deaths'])
# 
# #plt.show()
# plt.savefig('Age Deaths', bbox_inches = 'tight')
# plt.clf()
# 
# #####################################################
# 
# #Sex Deaths
# 
# with open('Sex Deaths.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 3)
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# yaxis, ylabel = axis(data, 1)
# 
# #xlabel = 'State/Territory'
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots again
# plt.bar(xaxis, yaxis, alpha = 0.5, color = 'r', width = 0.6)
# 
# plt.xticks(size = 20)
# plt.yticks(size = 20)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel('Percentage of Population', size = 25)
# plt.suptitle('Sex Based Percentage of Population Compared to Percentage of Deaths', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# plt.legend(['Percent of US Population', 'Percent of Deaths'])
# 
# #plt.show()
# plt.savefig('Sex Deaths', bbox_inches = 'tight')
# plt.clf()
# 
# #####################################################
# 
# #Ethnicity Deaths
# 
# with open('Ethnicity Deaths.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 3)
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# yaxis, ylabel = axis(data, 1)
# 
# #xlabel = 'State/Territory'
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots again
# plt.bar(xaxis, yaxis, alpha = 0.5, color = 'r', width = 0.6)
# 
# plt.xticks(size = 20)
# plt.yticks(size = 20)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel('Percentage of Population', size = 25)
# plt.suptitle('Ethnicity Based Percentage of Population Compared to Percentage of Deaths', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# plt.legend(['Percent of US Population', 'Percent of Deaths'])
# 
# #plt.show()
# plt.savefig('Ethnicity Deaths', bbox_inches = 'tight')
# plt.clf()
# 
# #####################################################
# 
# #Age Vaccinations
# 
# with open('Age Vaccination.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 3)
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# yaxis, ylabel = axis(data, 1)
# 
# #xlabel = 'State/Territory'
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots again
# plt.bar(xaxis, yaxis, alpha = 0.5, color = 'r', width = 0.6)
# 
# plt.xticks(size = 20)
# plt.yticks(size = 20)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel('Percentage of Population', size = 25)
# plt.suptitle('Age Based Percentage of Population Compared to Percentage of Vaccinations', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# plt.legend(['Percent of US Population', 'Percent of Vaccinations'])
# 
# #plt.show()
# plt.savefig('Age Vaccination', bbox_inches = 'tight')
# #plt.clf()
# 
# #####################################################
# 
# #Sex Vaccinations
# 
# with open('Sex Vaccination.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 3)
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# yaxis, ylabel = axis(data, 1)
# 
# #xlabel = 'State/Territory'
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots again
# plt.bar(xaxis, yaxis, alpha = 0.5, color = 'r', width = 0.6)
# 
# plt.xticks(size = 20)
# plt.yticks(size = 20)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel('Percentage of Population', size = 25)
# plt.suptitle('Sex Based Percentage of Population Compared to Percentage of Vaccinations', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# plt.legend(['Percent of US Population', 'Percent of Vaccinations'])
# 
# #plt.show()
# plt.savefig('Sex Vaccination', bbox_inches = 'tight')
# plt.clf()
# 
# #####################################################
# 
# #Ethnicity Vaccinations
# 
# with open('Ethnicity Vaccination.txt', 'r') as data:
#     data = data.read()
# data = eval(data)
# 
# # for i in range(len(data[0])):
# #     print(data[0][i] + ' ' + str(i))
# 
# xaxis, xlabel = axis(data, 0)
# yaxis, ylabel = axis(data, 3)
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots
# plt.figure(figsize=(25,15))
# plt.bar(xaxis, yaxis)
# 
# yaxis, ylabel = axis(data, 1)
# 
# #xlabel = 'State/Territory'
# 
# #Converts yaxis to integers
# for i in range(len(yaxis)):
#     yaxis[i] = float(yaxis[i])
# 
# #Plots again
# plt.bar(xaxis, yaxis, alpha = 0.5, color = 'r', width = 0.6)
# 
# plt.xticks(size = 20)
# plt.yticks(size = 20)
# plt.xlabel(xlabel, size = 25,)
# plt.ylabel('Percentage of Population', size = 25)
# plt.suptitle('Ethnicity Based Percentage of Population Compared to Percentage of Vaccinations', size = 30)
# plt.grid(b=True, which = 'major', axis = 'y', linestyle = '--')
# 
# #Formating
# plt.tight_layout()
# plt.subplots_adjust(left = 0.13, bottom = 0.155, right = 0.977, top = 0.926, wspace = 0.195, hspace = 0.2)
# plt.legend(['Percent of US Population', 'Percent of Vaccinations'])
# 
# #plt.show()
# plt.savefig('Ethnicity Vaccination', bbox_inches = 'tight')
# plt.clf()