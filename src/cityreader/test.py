import csv

class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __str__(self):
    # return f"{self.name} {self.lat} {self.lon}"
    return f"({self.name}, {self.lat}, {self.lon})"


def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  with open('cities.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader[1:]:
      print(row)

    # cities.extend(newcities)
    # cities.extend([City(row[0], row[3], row[4]) for row in csvreader[1:]])
    return cities

cities = cityreader()

# cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
# for c in cities:
#     print(c)
