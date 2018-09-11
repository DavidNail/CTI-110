#Percentage of males and females
#9/11/2018
#CTI-110 P2HW2 - Male Female Percentage
#David Nail
males = int(input('Enter the number of males in the class: '))
females = int(input('Enter the number of females in the class: '))
total = int(males + females)
x = (males/total)*100
y = (females/total)*100
print ("The class is" ,x, "percent male and" ,y, "percent female")
