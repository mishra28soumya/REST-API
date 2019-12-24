from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

    #Data to serve with our api
PEOPLE = {
    "Farrell": {
       "fname": "Doug",
        "lname":  "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
      "fname": "Bunny",
      "lname": "Easter",
      "timestamp": get_timestamp()
    }
}

#create a handler for our read(GET) people
def read():
    #create list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


