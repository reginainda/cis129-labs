# My Coffee Shop
#Prices
price_for_coffee = 5
  price_for_muffin = 4 
  tax = 0.06
  # ask customer for their order 
  num_of_coffees = int(input("How many coffees does customer want? "))
  num_of_muffins = int(input("How many muffins does customer want? "))
  # calculate the price of coffees and muffins together before tax
  subtotal = (num_of_coffees * price_for_coffee) + (num_of_muffins * price_for_muffin)
  # add tax to the subtotal
  tax = subtotal * tax
  total = subtotal + tax
  # print reciept 
  print("\n********************************") 
  print("My Coffee Shop Receipt")
  print(f"{num_of_coffees} $5 per Coffee: ${num_of_coffees * price_for_coffee:.2f}")
  print(f"{num_of_muffins} $4 per Muffin: ${num_of_muffins * price_for_muffin:.2f}")
  print(f"6% tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
  print("********************************")
  
