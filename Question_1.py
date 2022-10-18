# Maps a route object to a string representing its long name
#
# parameter route: a route object returned by the API
# returns: a string representing the long name of a route
def map_route_to_long_name(route):
    return route["attributes"]["long_name"]

# Executes all the steps of question 1, and handles I/O for it
#
# parameter all_subway_routes: a list of route objects calculated in main. Taken as a parameter to avoid more API calls.
def question_1(all_subway_routes):
  print("-----------------------------Question 1 Start: -----------------------------\n")

  subway_route_long_names = list(map(map_route_to_long_name, all_subway_routes))

  print(subway_route_long_names)
  print("\n-----------------------------Question 1 End-----------------------------\n")
