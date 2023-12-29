#Exercise 4: Guest list: ballot_box_with_check: 

# If you could invite anyone, living, or deceased to dinner, who would you invite? 
# Make a list that include at least three people you'd like to invite for dinner.
# then use your list to print a message to each person inviting them to dinner.

guests = ['April', 'Daniel', 'Fath']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

# Exercise 5: Changing guest list. ballot_box_with_check: 

# Start with your program from exercise 3-4. Add a print at the end of your program stating the name of the guest who can't make it.
# Modify the list replacing the name of the guest who can't make it with the name of the new person that you're inviting.
# Print a second set of invitation messages, one for each person who still in your list. 

#invite some people to dinner.

guests = ['April', 'Daniel', 'Fath']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print("\nSorry," + name + " can't come to dinner.")

#Daniel can't make it to dinner. let's invite Analyn instead.
del(guests[1])
guests.insert(1, 'Analyn')

#print the invitations again.
name = guests[0].title()
print(name + "\n" + name + ",please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

#Exercise 3: shrinking guest list. ballit_box_with_check: 

    #Start with your program from 3-5. Add a new line that prints a message saying that you can only invite two people.
    #Use pop to remove guests from your list one at the time until only two names remove on your list. 
    #Each time you have to pop a name for your list, print a message to that person letting you know that your sorry, you can't invite them to diinner.
    #Print each message to each two people who still on your list, letting them know you're still invited.
    #Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you have an empty list at the end of your program.

#Invite people to dinner 

guests = ['April', 'Daniel', 'Fath']

name = guests[0].title()
print(name + "please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print( "\sorry, "+ name + "Can't make it to dinner.")

#Sorry, Daniel can't make it to dinner. 
del(guests[1])
guests.insert(1, 'analyn')

#print the invitations again. 
name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

#We got a bigger table, so let's add some people in the list.
print("we got a bigger table!")
guests.insert(0,'George')
guests.insert(2,'Mark')
guests.append('tim')

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")

name = guests[4].title()
print(name + ", please come to dinner.")

name = guests[5].title()
print(name + ", please come to dinner.")

#Oh no the table won't arrived on time. 
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)

#Exercise 7: seeing the world: ballot_box_with_a_check: 

places_list = ['Tokyo', 'Seoul', 'England', 'Denmark', 'Singapore']
print(places_list)

print("original order: ")
print(places_list)

print("\nAlphabetical order:")
print(places_list)

print("\nReverse alphabetical:")
print(places_list)

print("\nOriginal order: ")
print(places_list)

print("\nReversed: ")
print(places_list)





