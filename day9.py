# Dictionary in Python
# Its data structure that allow us associate a key to a value 
# and pair the two pieces of data together.

colours = {
	"apple": "red",
	"banana": "yellow",
	"peer": "green"
}

print(colours)

# Nested list in dictionary
travel_log = {
	"France": ["Paris", "Lille", "Dijon"],
	"Germany": ["Stuttgart", "Berlin"]
}

print(travel_log["France"][1])

travel_blog = {
	"France": {
		"cities_visited": ["Paris", "Lille", "Georgia"],
		"total_visits": 12
	},
	"Germany": {
		"cities_visited": ["Berlin", "Hamburg", "Munich"],
		"total_visits": 5
	}
}

print(travel_blog["Germany"]["cities_visited"][1])