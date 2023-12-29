# Exercise 4: Deli: ballot_box_with_check: 

# Make a list called sandwich_orders and fill it with the names of various sandwuches.
# Then make a empty list called finished_sandwiches.
# Loop through the list of sandwich orders and print a message for each order, such as I made tuna sandwich. 
# As each sandwich is made, move it to the list to finish sandwhiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I am working with your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches: 
    print(f"I made a {sandwich} sandwich. ")


# Exercise 5: No pastrami ballot_box_with_check: 

# Using the list sandwich_orders from 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all.
# Occurence of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami', 
    'turkey', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I am sorry, we're all run out of pastrami today.")
while 'pastrami' in sandwich_orders: 
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")


