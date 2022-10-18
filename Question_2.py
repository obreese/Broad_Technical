import requests
from constants import HEADERS, URLS

# Maps a route JSON object to it's ID
#
# parameter route: object returned from the API which represents a route
# returns id: a string representing the route object's id
def map_route_to_id(route):
  return route["id"]
  
# Finds all stop names for a given route
#
# parameter route_id: a string representing the route object's id
# returns: list of strings representing names of all the subway stops
def find_stops_names_for_route(route_id):
    stops_for_route = requests.get(URLS["GET_STOPS_FOR_ROUTE_BASE"] % (route_id), headers=HEADERS).json()["data"]
    
    def map_stop_object_to_name(stop_object):
      return stop_object["attributes"]["name"]

    subway_stop_names = list(map(map_stop_object_to_name, stops_for_route))
    return subway_stop_names  

# Finds the count of all stops for a given route
#
# parameter route_id: a string representing the route object's id
# returns: a number representing how many stops are on the given route
def find_stops_count_for_route(route_id):
    return len(find_stops_names_for_route(route_id))

# Finds the route with the most and least stops, along with their repective stop counts
#
# parameter subway_route_ids: list of string identifiers for routes
# returns max_and_min_map: dictionary containing all the necessary output information in one object
def find_most_and_least_stops(subway_route_ids):
    max_and_min_map = {
      "max_route": subway_route_ids[0],
      "max_count": find_stops_count_for_route(subway_route_ids[0]),
      "min_route": subway_route_ids[0],
      "min_count": find_stops_count_for_route(subway_route_ids[0])
    }
    
    for route_id in subway_route_ids[1:]:
      stops_count_for_route = find_stops_count_for_route(route_id)
      
      if stops_count_for_route > max_and_min_map["max_count"]:
        max_and_min_map["max_route"] = route_id
        max_and_min_map["max_count"] = stops_count_for_route
        
      elif stops_count_for_route < max_and_min_map["min_count"]:
        max_and_min_map["min_route"] = route_id
        max_and_min_map["min_count"] = stops_count_for_route
        
    return max_and_min_map
  
  
# Finds a dictionary which maps every subway stop to its corresponding routes
#
# parameter subway_route_ids: a list of route_id strings which represent each subway route
# returns stop_to_routes_map: a dictionary which maps every subway stop to its corresponding routes
def find_stops_to_routes_map(subway_route_ids):
  stop_to_routes_map = {}
  
  for route_id in subway_route_ids:
    for stopName in find_stops_names_for_route(route_id):
      if stopName in stop_to_routes_map:
        stop_to_routes_map[stopName] += [route_id]
      else:
        stop_to_routes_map[stopName] = [route_id]
  
  return stop_to_routes_map
  
# Finds a dictionary mapping from subway stops to corresponding routes for stops that have multiple routes
#
# parameter stop_to_routes_map:a dictionary which maps every subway stop to its corresponding routes
# returns multi_stop_to_routes: a dictionary mapping from subway stops to corresponding routes for stops that have multiple routes
def find_multi_route_stops(stop_to_routes_map):
  multi_stop_to_routes = {}
  
  for stop in stop_to_routes_map.keys():
    if len(stop_to_routes_map[stop]) > 1:
      multi_stop_to_routes[stop] = stop_to_routes_map[stop]
  
  return multi_stop_to_routes

# Executes all the steps of question 2, and handles I/O for it
#
# parameter all_subway_routes: a list of route objects calculated in main. Taken as a parameter to avoid more API calls.
# returns stop_to_routes_map: a dictionary which maps every subway stop to its corresponding routes to avoid recomputing in question 3
def question_2(all_subway_routes):
  print("-----------------------------Question 2 Start: -----------------------------\n")

  subway_route_ids = list(map(map_route_to_id, all_subway_routes))
  
  # parts 1 and 2 of question 2
  print(find_most_and_least_stops(subway_route_ids), "\n")
  
  # part 3 of question 2
  stop_to_routes_map = find_stops_to_routes_map(subway_route_ids)
  multi_stop_to_routes = find_multi_route_stops(stop_to_routes_map)
  
  print(multi_stop_to_routes)
    
  print("\n-----------------------------Question 2 End-----------------------------\n")
  
  return stop_to_routes_map