#Get input from the user

principle = float(input("Enter the principle amount here in (digits) :"))
rate = float(input("Enter the interest rate (yearly interest in %) :"))
time = float(input("Enter the years")

# Calculate simple interest
simple_interest = (principle * rate * time) / 100

# Display the result
print(f"The simple interest is: {simple_interest}")

# Asks if the user want to know the total amount
total_amount = input("Do you want to know the total amount which is (principle + interest)? (yes/no): ").lower()

if total_amount == "yes":
    # calculate and display the total amount (principle + interest)
    total = principle + simple_interest
    print(f"The total amount is {total}")
esle:
    ("Okay no problem!")