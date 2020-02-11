#The Boredless Tourist
#Project from Codecademy computer science pathway

#"Now let’s create some data that we’re going to use to test the functionality that we create for The Boredless Tourist.
#The first is our list of destinations that we’re going to be using.""

# List of destinations
destinations = ["Paris, France","Shanghai, China","Los Angeles, USA","Sao Paulo, Brazil","Cairo, Egypt"]

#Test traveler to see if functionality is working
test_traveler = ['Erin Wilkes','Shanghai, China', ['historical site', 'art']]
# "This is a traveler (a user of The Boredless Tourist application) whose name is Erin Wilkes who likes ...
# historical buildings and art. Erin is in China right now, hopefully we can find some good places to show her."

# "Now that we have test data for a traveler and a list of destinations that we can use, we can start building some of the
# Boredless Tourist‘s functionality. When a traveler arrives at a destination, we want to know where they are! Since we
# use lists for all of our data — we are going to identify each location based on its index in our destinations list.
# But we need to retrieve that index first."

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

#Testing to see if function works - Confirmed
#print(get_destination_index("Paris, France"))
#print(destinations[0])

#Testing with destination not on list - Confirmed ValueError "Hyderabad, India" is not on list
#print(get_destination_index("Hyderabad, India"))

def get_traveler_location(traveler):
    traveler_destination = traveler[1] #accesses traveler's destination string, see test_traveler
    traveler_destination_index = get_destination_index(traveler_destination) #Finds travelers destination w/in destinations list
    return traveler_destination_index

#Test validity, Test subject in Shanghai therefore should return 1 as index in destinations list - Confirmed
#test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index) 
