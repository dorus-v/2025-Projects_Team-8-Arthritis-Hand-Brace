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

y_err= [0.006596087420748464, 0.006187548181318392, 0.006444236732278119, 0.006388844138703775, 0.0058027575323342795, 0.005669752954743812, 0.005395569036881098, 0.004525034124974403]

# Plot maken
plt.figure(figsize=(8, 5))
plt.plot(x_waarden, y_waarden, marker='o', linestyle='-', color='blue', label='Measured value')
plt.errorbar(x_waarden, y_waarden, y_err, linestyle='')
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