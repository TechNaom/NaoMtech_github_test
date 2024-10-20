#There are 5 houses in a specific area, each described by tuples containing their x and y coordinates, colors, sizes, and the names of the owners.
#Use a for loop to plot each house individually, displaying the first characters of the own#ers’ names next to their respective houses.
from cProfile import label

import matplotlib.pyplot as plot


# Given datasets
x_tuple = (1, 5, 8, 3, 9)
y_tuple = (7, 1, 9, 5, 3)
color_tuple = ('green', 'red', 'orange', 'navy', 'pink')
size_tuple = (250, 50, 200, 100, 175)
name_tuple = ('Michael', 'Tim', 'Jennifer', 'Liz', 'Frank')


#Create figure
plot.figure(figsize=(8,6))


#Iterate datasets
for i in range(len(x_tuple)):
    plot.scatter(x_tuple[i],y_tuple[i],c=color_tuple[i],s=size_tuple[i],label=name_tuple[i])
    plot.text(x_tuple[i]+0.2,y_tuple[i],name_tuple[i],fontsize=12)

plot.xlabel("X coordinates")
plot.ylabel("Y coordinates")
plot.title("Displaying the own#ers’ names")

#Show plot
plot.grid()
plot.show()
