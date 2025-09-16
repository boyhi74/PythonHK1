cost = float(input())
tax = 0.05 * cost
tip = 0.18 * cost
total = cost + tax + tip
print(f"{tax:.2f}")
print(f"{tip:.2f}")
print(f"{total:.2f}")
