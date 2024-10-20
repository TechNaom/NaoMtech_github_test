import statistics
import matplotlib.pyplot as plt

# Initialize an empty list to store numeric values
numbers = []

# While loop to keep asking for numeric input
while True:
    user_input = input("Enter a number or type Q to quit: ")

    if user_input.lower() == 'q':
        break

    try:
        # Try converting input to float
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        # Warn the user if the input is not a number
        print("Please enter a numerical value!")

# If the list is empty, warn and exit
if not numbers:
    print("No valid numbers were entered.")
else:
    # Convert the list to a tuple
    numbers_tuple = tuple(numbers)

    # Print entered numbers
    print(f"Numbers: {numbers_tuple}")

    # Calculate statistics
    count = len(numbers_tuple)
    mean = statistics.mean(numbers_tuple)
    median = statistics.median(numbers_tuple)
    std_dev = statistics.stdev(numbers_tuple) if count > 1 else 0
    maximum = max(numbers_tuple)
    minimum = min(numbers_tuple)

    # Print calculated values
    print(f"Count: {count}")
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

    # Data for visualization
    stats = ['Count', 'Mean', 'Median', 'Std Dev', 'Max', 'Min']
    values = [count, mean, median, std_dev, maximum, minimum]

    # Create a bar graph
    plt.bar(stats, values, color=['blue', 'green', 'red', 'purple', 'orange', 'yellow'])

    # Add title and labels
    plt.title('Statistics of Entered Numbers')
    plt.xlabel('Statistics')
    plt.ylabel('Values')

    # Show the bar graph
    plt.show()
