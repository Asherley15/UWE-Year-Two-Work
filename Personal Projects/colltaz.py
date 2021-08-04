import matplotlib.pyplot as plt
import numpy as np

# Get Initial number
num = float(input("Please enter your starting number:\n"))

# Set counter to 0
counter = 0

# Create initial arrays from counter and users number
x = np.array([counter])
y = np.array([num])

# Set program to stop once 1 has been reached, beyond this an infinite 4-2-1 loop is formed.
while counter < 300:
    # Increment Counter
    counter += 1

    # Add counter to X axis
    x = np.append(x, [counter])

    # If number is even (Modulo ==0) divide number by 2.
    if (num % 2 == 0):
        num = num / 2
        # Add number to Y Axis array
        y = np.append(y, [num])

    else:
        # If number is odd, 3x+1
        num = num * 3 + 1

        # Add number to Y Axis array
        y = np.append(y, [num])

else:
    # Upon counter reaching 1000:
    print("Reached 1 in", counter, "steps")

    # Plot X and Y arrays
    plt.plot(x, y)

    # Label x and y Axis's
    plt.xlabel('Steps')
    plt.ylabel('Number')

    # Display Graph
    plt.show()
