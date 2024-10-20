#There are 5 houses in a specific area, each described by tuples containing their x and y coordinates, colors, sizes, and the names of the owners.
#Use a for loop to plot each house individually, displaying the first characters of the owners’ names next to their respective houses.

import matplotlib.pyplot as plot

# Given data
x_tuple = (1, 5, 8, 3, 9)
y_tuple = (7, 1, 9, 5, 3)
color_tuple = ('green', 'red', 'orange', 'navy', 'pink')
size_tuple = (250, 50, 200, 100, 175)
name_tuple = ('Michael', 'Tim', 'Jennifer', 'Liz', 'Frank')

#
plot.figure(figsize=(8,6))

#Iterarting for loop
for i in range(len(x_tuple)):
    plot.scatter(x_tuple[i],y_tuple[i],c=color_tuple[i],s=size_tuple[i],label=name_tuple[i])
    # Add the first character of each owner's name next to their house
    plot.text(x_tuple[i],y_tuple[i],name_tuple[i][0],fontsize=12)

#plot.xlabel("X Axis")
#plot.ylabel("Y Axis")
#plot.title("'Scatter Plot of Houses with Owner Initials'")

plot.grid()
plot.show()