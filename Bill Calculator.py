import time
print("Welcome to the Bill Calculator.\n")

original_amt = float(input("What is the amount of the total bill? \n"))

# Tax
amt = original_amt + (0.09 * original_amt)

# Tip
if input("Would you like to tip?\n(Enter Y for Yes and N for No)\n") == "Y":
    tip = int(input("Enter Tip in % \n"))
    tip_amt = (tip / 100) * amt
    amt += tip_amt

# Split
if input("Would you like to split the bill?\n(Enter Y for Yes and N for No)\n") == "Y":
    people = int(input("Enter the number of people among whom the bill will be split \n"))
    split_bill = amt / people
    print()

# Display
print("YOUR BILL: ")
print(f"Your Total Bill is: {amt: .2f} ")
if "split_bill" in locals():
    print(f"Amount per person after splitting: {split_bill: .2f}")
print()    

# Breakdown
if input("Would you like to see a breakdown of the bill?\n(Enter Y for Yes and N for No)\n") == "Y":
    print()
    print(f"Bill Amount: {amt:.2f}")
    print(f"Tax Added: {(0.09 * original_amt):.2f} (9%)")
    if "tip_amt" in locals():
        print(f"Tip Added: {tip_amt:.2f} ({tip}%)")
    print(f"Total Amount: {amt: .2f}")
    if "split_bill" in locals():
        print(f"Amount per person after splitting: {split_bill:.2f}")
        
time.sleep(10)