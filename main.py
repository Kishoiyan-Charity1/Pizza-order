food =["Burger","Drink","Fries","Apple pie"]
prices =[5,1,3,2]

myorderFood=[]
myorderCost=[]

print("Wecome to Rittys")
print("Can i get your order?")

order = input("Can i take your order?")

foodOrder= input("Please enter item")
if foodOrder=="Burger":
    myorderFood.append(food[0])
    myorderCost.append(prices[0])

elif foodOrder=="Drink":
    myorderFood.append(food[1])
    myorderCost.append(food[1])