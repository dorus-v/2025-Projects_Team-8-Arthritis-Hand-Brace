import matplotlib.pyplot as plt


# Gegeven data
x_waarden = [2, 3, 4, 5, 6, 7, 8, 9]
y_waarden = [0.6845803764097439, 0.7107355256748643, 0.7055512240760954,
             0.7147620673723962, 0.7469254962938094, 0.7585170005156745,
             0.7756403691946019, 0.8163512637862057]

# Plot maken
plt.figure(figsize=(8, 5))
plt.plot(x_waarden, y_waarden, marker='o', linestyle='-', color='blue', label='Waarden')
plt.title("Plot van x-waarden vs y-waarden")
plt.xlabel("x-waarden")
plt.ylabel("y-waarden")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
