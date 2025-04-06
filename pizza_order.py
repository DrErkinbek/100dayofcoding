print("""Welcome to Python Pizza Deliveries!
      Small pizza (S): $15
      Medium pizza (M): $20
      Large pizza: (L): $25
      Add pepperoni for small pizza (Y or N): $2
      Add pepperoni for medium or large pizza (Y or N): $3
      Add extra cheese for any size pizza (Y or N): +$1 """)

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
else:
    print('You typed the wrong inputs.')
    
if pepperoni == 'Y':
    if size == 'S':
        bill+= 2
    else:
        bill+= 3

if extra_cheese == "Y":
    bill+= 1
     
print(f'Your total to pay is ${bill}')