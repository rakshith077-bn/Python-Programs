friends = ["Rolf", "Matt", "Ann", "Ronny", "Heather", "Connor", "Copper"]
guests = ["Rolf", "bob", "Matt", "ruth", "joe", "Connor", "Cooper"]
friends_caps = set([f.title() for f in friends])
guests_caps = set([g.title() for g in guests])
print(friends_caps.intersection(guests_caps)) #the order in the friends list and the guests will be lost if you run that through the set functions



friends = ["Rolf", "Matt", "Ann", "Ronny", "Heather", "Connor", "Copper"]
guests = ["Rolf", "bob", "Matt", "ruth", "joe", "Connor", "Cooper"]
total_friends = [
    for name in guests 
    if f.title() in [f.title() for f in friends]
]
print(total_friends) #the order will not be lost if done like this

