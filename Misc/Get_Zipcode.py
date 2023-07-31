from geopy.geocoders import Nominatim

# Create the geolocator object with a user-agent
geolocator = Nominatim(user_agent="geoAPiExercises")

# Get city-name from user
place = input("Enter city name: ")

# Geocoding the location
location = geolocator.geocode(place)

# Print details
print(location)