import requests
from constants import URLS, HEADERS
from Question_1 import question_1
from Question_2 import question_2
from Question_3 import question_3


def main():
  print("...starting...\n")

  all_subway_data_list = requests.get(url=URLS["GET_SUBWAY_ROUTES"], headers=HEADERS).json()["data"]

  question_1(all_subway_data_list)
  
  stops_to_routes_map = question_2(all_subway_data_list)
  
  question_3(stops_to_routes_map)


  print("\n...done...")
  
  
main()