import matplotlib.pyplot as plt

# Given data
x_tuple = (1, 5, 8, 3, 9)
y_tuple = (7, 1, 9, 5, 3)
color_tuple = ('green', 'red', 'orange', 'navy', 'pink')
size_tuple = (250, 50, 200, 100, 175)
name_tuple = ('Michael', 'Tim', 'Jennifer', 'Liz', 'Frank')

# Create scatter plot
plt.figure(figsize=(8, 6))

# Loop through each house and plot it
for i in range(len(x_tuple)):
    plt.scatter(x_tuple[i], y_tuple[i], c=color_tuple[i], s=size_tuple[i], label=name_tuple[i])
    # Add the first character of each owner's name next to their house
    plt.text(x_tuple[i] , y_tuple[i], name_tuple[i][0], fontsize=12)

# Add labels and title
plt.xlabel('X Coordinates')
plt.ylabel('Y Coordinates')
plt.title('Scatter Plot of Houses with Owner Initials')

# Show plot
plt.grid(True)
plt.show()

