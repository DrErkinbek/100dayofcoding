states_of_usa = ["Alabama", "Alaska", "Arizona", "Arkansas", "California",  
"Colorado", "Connecticut","Delaware","District Of Columbia","Florida",  
"Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky",  
"Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi",  
"Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico",
"New York","North Carolina","North Dakota","Ohio",  "Oklahoma",  "Oregon",  
"Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee",  
"Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin",  
"Wyoming"]

print(states_of_usa[-1])
states_of_usa[0] = 'Ala'
#print(states_of_usa)

# Append method add item to the end of the list.
states_of_usa.append("chicago")
#print(states_of_usa)

# Insert method adds item at a given position.
states_of_usa.insert(1, 'seatle')
# print(states_of_usa)

# Remove method remove the first item from the list
states_of_usa.remove('Ala')
#print(states_of_usa)

# clear Remove all items from the list.
# states_of_usa.clear()
# print(states_of_usa)

#Reverse method reverse the elements of the list in a place.
states_of_usa.reverse()
#print(states_of_usa)

# Copy method returns a shallow copy of the list.
usa = states_of_usa.copy()
print(usa)
