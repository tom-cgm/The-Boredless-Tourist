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
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)
#"Now we want to create and maintain a list of attractions."

attractions = []
for destination in destinations:
    attractions.append([]) # initial empty list for each destination in destinations
def add_attraction(destination,attraction):

    #Catch ValueError such that no attractoin is added to destinations that do not exist
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index] # Find appropriate list for destination in attractions
        attractions_for_destination.append(attraction) #add attraction to list
    except ValueError:
        return

#Add initial attraction
add_attraction("Los Angeles, USA",['Venice Beach',['beach']])
#test function - Passed
#print(attractions)

#Add some more attractions
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

print(attractions)
