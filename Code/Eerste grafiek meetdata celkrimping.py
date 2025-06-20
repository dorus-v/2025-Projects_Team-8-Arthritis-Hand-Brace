import matplotlib.pyplot as plt


# Gegeven data
x_waarden = [2, 3, 4, 5, 6, 7, 8, 9]
y_waarden = [
            0.6738163147980806,
            0.6974220979862596,
            0.688413993731318, 
            0.6946060678505313,
            0.7258131054104111, 
            0.7352160093373624,
            0.7509882011038868, 
            0.7936531053777592]

theo_y_waarden = []
while len(theo_y_waarden) < 8:
    theo_y_waarden.append(2/3.14)
# Plot maken
plt.figure(figsize=(8, 5))
plt.plot(x_waarden, y_waarden, marker='o', linestyle='-', color='blue', label='Measured value')
plt.plot(x_waarden, theo_y_waarden, linestyle='--', color='red', label='Theoretical value')
plt.xlabel("Number of cells", fontsize=15)
plt.ylabel("Shrinkage factor", fontsize=15)
plt.tick_params(axis="both", labelsize=13)
plt.xlim(2,9)
plt.ylim(0.60, 0.8)
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
plt.savefig("grafiek.png")