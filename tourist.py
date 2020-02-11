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


# "We want to be able to help our traveler’s find the most interesting places in a new city for them.
# In order to do that we need to match their interests with the possible locations in a city."

def find_attractions(destination,interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for attraction in attractions_in_city:
        possible_attraction =attraction
        attraction_tag = attraction[1] #Retrieve tagged information about the attraction
        for interest in interests: #See if any interests match with attraction tags
            if interest in attraction_tag:
               attractions_with_interest.append(possible_attraction[0]) #appending suitable attractions but only showing name of attraction not the tag
    return attractions_with_interest


# Test, Should return ['LACMA'] Passed
la_arts = find_attractions("Los Angeles, USA",['art'])
print(la_arts)


# Connecting people to attractions they are interested in

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1] # Seperates data for destination
    traveler_interests = traveler[2] # Seperates data for interests
    traveler_attractions = find_attractions(traveler_destination,traveler_interests)
    interests_string = "Hi " + traveler[0] + ", we think that you would enjoy these places around " + traveler_destination +": "
    for attraction in traveler_attractions:
        interests_string = interests_string + "the " + attraction +", "
    return interests_string

#test functionality
smills_france = get_attractions_for_traveler(['Dereck Smill','Paris, France',['monument']])
print(smills_france)
