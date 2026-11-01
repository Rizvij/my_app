
amt_inr = float(input("Enter amount in INR: "))

exchange_rate = 96
amt_usd = amt_inr / exchange_rate

print("Your amount in USD is $",round(amt_usd, 2))
