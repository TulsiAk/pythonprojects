from IPython.display import clear_output #when using Jupyter Notebook
# Secret Auction Program

dicti = {}
d = True

while d:
    name = input("Name: ")
    bid = int(input("Bid amount: "))
    dicti[name] = bid
    
    c = input("Do you want to have more entries? (yes/no): ").lower()
    if c == "yes":
        clear_output(wait=True)
    else:
        d = False

# Finding the highest bidder
highest_bidder = max(dicti, key=dicti.get)
print(f"\nHighest bidder is {highest_bidder} with a bid of ₹{dicti[highest_bidder]}")
