import matplotlib
matplotlib.use("TkAgg")  
import matplotlib.pyplot as plt


x = [float(i) for i in input("Enter X values separated by commas: ").split(",")]
y = [float(i) for i in input("Enter Y values separated by commas: ").split(",")]


if len(x) != len(y):
    print("Error: X and Y must have the same number of values.")
else:
    # Plot
    plt.plot(x, y, marker='o')
    plt.xlabel("X values")
    plt.ylabel("Y values")
    plt.title("Simple X-Y Plot")
    plt.grid(True)
    plt.show()