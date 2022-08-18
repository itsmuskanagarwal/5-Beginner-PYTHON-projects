from replit import clear
from art import logo

print(logo)

bid_details={}
flag = True
while(flag==1):
  name = input("Enter you name: ")
  bid_amount = int(input("Enter you bidding amount: "))
  bid_details[name]=bid_amount

  result = input("Are there any other bidder? 'Y'/'N'")
  if result == 'Y' or result == 'y' :
    flag = True
    clear()
  if result == 'N'or result == 'n':
    flag = False
print("Biding Details: ")

amt =0
for key in bid_details:
  print("Name: ",key," ","Bid Amount:"," ",bid_details[key])
  if amt < bid_details[key]:
    amt = bid_details[key]
    winner = key

print(f"The winner is {winner} with {amt} as bid amount")
