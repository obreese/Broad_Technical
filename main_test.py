# As mentioned in my Question 3 output, I have a bit of a time crunch with a midterm tomorrow, so I'll briefly explain my tests rather than fighting with them for a couple hours. I predict having problems with a test suite because some of my API requests (even with the key) might be getting throttled. I hope this achieves the same goal of seeing how I work.

# As a side note, I think the throttling issue could be fixed in testing with some delaying statements, but I've personally only done something like that in typescript and java, so decided against spending the time here.

# ----------------------------------------------------------------------------------
# Question 1:
# This question doesn't rely on input other than the API's results. Due to this, there really aren't edge cases. One test case which asserts the API call returns all the subway data, and the function call returns a list of long names should do the trick. To be very thorough, It could be worth some manual processing on ALL the data and a comparison with the filtered data on route types 0 and 1.

# ----------------------------------------------------------------------------------
# Question 2:

# - test map_route_to_id with a route object, then a route object without an id and expect an error

# - test find_stops_names_for_route with a valid and invalid route_id. Make sure to test with a route with multiple stops and a single stop

# - test find_stops_count_for_route with a valid and invalid route_id. Make sure to test with a route with multiple stops and a single stop

# - test find_most_and_least_stops with empty route_ids to check default values, and with a valid route_ids list. To be very thorough, could mock find_stops_count_for_route and make sure max and min are calculated correctly.

# - test find_stops_to_routes_map with empty and nonempty route_ids. To be thorough, mock find_stops_names_for_route and make sure resulting map is correct for mock data.

# - test find_multi_route_stops with empty, invalid, and valid stop_to_routes_map. No need to mock any internal function, just need to manually determine which stops have multiple associated routes, then check the result.

# - test question_2 with valid and invalid all_subway_routes. End to end simply make sure nothing crashes


# ----------------------------------------------------------------------------------
# Question 3:

# - test find_path with a test stop_to_route mapping that can handle the following cases: unconnected (impossible) two stops, two stops on same route, two stops on different route, two stops on different routes with multiple transfers, invalid stop1, invalid stop2, and stop1 is the same as stop2

# - test question 3 with valid and invalid stop_to_route_map. End to end simply make sure nothing crashes. Also should test invalid inputs