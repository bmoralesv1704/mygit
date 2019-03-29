#create a mapping of state to abbreviation
states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan' : 'MI'
}
# CREATE A BASIC SET OF STATES AND SOME CITIES IN THEM
crities = {
        'CA': 'San Franciso',
        'MI': 'Detroit'
        'FL': 'Jacksonville'               
}

    cities['NY'] = 'New York'
    cities['OR'] = 'Portland'
    
     
    print('- '*10)
    print("NY State has: ", cities['NY'])
    print("OR State has: ", cities['OR'])
    # print some states27   
    print('- '*10)
    print("Michigan's abbreviation is: ", states['Michigan'])
    print("Florida's abbreviation is: ", states['Florida'])
    
    # do it by using the state then cities dict
    print('- '*10)
    print("Michigan has: ", cities[states['Michigan']])
    print("Florida has: ", cities[states['Florida']])
    # print every state abbreviation
    print('- '*10)
    for state, abbrev in states.items():
        (print"%s is abbreviated %s"% (state, abbrev))
        # print every city in state
    print('- '*10)
    for abbrev, city in cities.items():
        print("%s has the city %s"% (abbrev, city))
    # now do both at the same time
    print('- '*10)
    for state, abbrev in states.items():
        print("%s state is abbreviated %s and has city %s" % (
                state, abbrev, cities[abbrev]))
    print('- '*10)
    # safely get an abbreviation by state that might not be there
    state = states.get('Texas', None)
    if not state:
        print("Sorry, no Texas.")
    # get a city with a default value
    city = cities.get('TX', 'Does Not Exist')
    print("The city for the state 'TX' is: %s"% city)
    
    
