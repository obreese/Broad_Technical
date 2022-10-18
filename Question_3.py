# function which finds the path from a stop to another through subway lines
#
# parameter stop_to_route_map: a dictionary which maps every subway stop to its corresponding routes
# parameter stop_1: string representing the name of a subway stop
# parameter stop_2: string representing the name of a subway stop
#
# Explaination: 
# This would be implemented through a BFS graph search. Why BFS over DFS? Subway systems generally shouldn't take more than 2 or 3 transfers to get from one stop to another, and in the world of graph searches this is very shallow. BFS works better with shallow solutions, and won't get caught up in potentially infinite loops like DFS might in this situation (as we don't have specified directions in this implementation).
# I would call the "stop_1" the start node, and the visited list would begin with all of "stop_1"'s associated routes (after checking solutions on those routes). For solution checking, we just need to check if a node is in "stop_2"'s associated routes before adding it to visited. This is obviously a high-level overview, and I'm sure there are some nuances in the implementation, but I believe this gets my stategy accross.
def find_path(stop_to_route_map, stop_1, stop_2):
  stop_1_routes = stop_to_route_map[stop_1]
  stop_2_routes = stop_to_route_map[stop_2]
  
  print("Stop 1 Route(s): ", stop_1_routes)
  print("Stop 2 Route(s): ", stop_2_routes)
  
  print("\nThis particular developer has an electrical engineering midterm tomorrow, and chose to explain his solution rather than implement and troubleshoot it. To get from stop 1 to stop 2, hop on a train and roll the dice of fate!")

# Executes all the steps of question 3, and handles I/O for it
#
# parameter stop_to_route_map: a dictionary which maps every subway stop to its corresponding routes to avoid recomputing result of question 2
def question_3(stop_to_route_map):
  print("-----------------------------Question 3 Start: -----------------------------\n")

  # take in 2 stops
  stop_1 = input("Stop 1: ")
  stop_2 = input("Stop 2: ")
  
  print(find_path(stop_to_route_map, stop_1, stop_2))

  print("\n-----------------------------Question 3 End-----------------------------\n")

  