URLS = {
  "GET_SUBWAY_ROUTES": "https://api-v3.mbta.com/routes?filter[type]=0,1",
  "GET_STOPS_FOR_ROUTE_BASE": "https://api-v3.mbta.com/stops?filter[route]=%s&include=route&sort=address"
}

API_KEY = "8997fcec7c21442fa26fc27501d3ed6f"
HEADERS = {'Authorization': 'Bearer %s' % API_KEY}