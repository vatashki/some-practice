installment = input()

total = 0

while installment != "NoMoreMoney":
    if float(installment) < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {float(installment):.2f}")
    total += float(installment)
    installment = input()
    if installment == "NoMoreMoney":
        break

print(f"Total: {total:.2f}")
