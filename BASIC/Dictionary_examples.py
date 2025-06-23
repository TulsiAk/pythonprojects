travel_log = [
    {"country":"france",
    "visit": 5,
    "cities_visited":["paris", "lille", "lyon"]
    },
   { "country":"india",
    "visit": 2,
    "cities_visited":["delhi", "jaipur"]
    }
]
def add_new_country(country, visits, cities):
    new_country={}
    new_country["country"]=country
    new_country["visit"]=visits
    new_country["cities_visited"]=cities
    travel_log.append(new_country)

add_new_country("russia", 3, ["moscow", "st petersburg", "kazan"])

print(travel_log)