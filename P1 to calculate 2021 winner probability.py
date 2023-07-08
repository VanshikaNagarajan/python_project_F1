#importing libraries
import requests
import pandas as pd
import json
from sklearn.preprocessing import MinMaxScaler

#Define the urls of the API's


results_url = "https://ergast.com/api/f1/2021/14/results.json"
standings_url = "https://ergast.com/api/f1/2021/driverStandings.json"


print(results_url)
print(standings_url)

#defining the parameters of API request

params = {'api_key': 'your_api_key_here'}

print("your api key")

#to get requests from the API

response = requests.get("http://ergast.com/api/f1/drivers.json?callback=myParser")
print(response.url)


results_response = requests.get(results_url, params=params)
print("Response code:", response. status_code)

standings_response = requests.get(standings_url, params=params)

#check the response status
if results_response.status_code == 200 and standings_response.status_code == 200:
    #the request was succssful
    results_data = json.loads(results_response.text)
    standings_data = json.loads(standings_response.text)
    print(results_response.text)
    print(standings_response.text)
    print(results_data)
    print(standings_data)
else:
    #one or both request failed
    print("Error: Could not retrieve data from API.")
print(type(standings_data))
print(type(results_data))

standings = standings_data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
drivers = [entry['Driver']['givenName'] + ' ' + entry['Driver']['familyName'] for entry in standings]
points = [(entry['points']) for entry in standings]
print(drivers)
print(points)


#Normalize the points between 0 and 1.
#points already in sorted array.

points = [395.5, 387.5, 226, 190, 164.5, 160, 159, 115, 110, 81, 74, 43, 34, 32, 16, 10, 7, 3, 0, 0, 0]
scaler = MinMaxScaler()
points_reshaped = [[point] for point in points]
normalized_points = scaler.fit_transform(points_reshaped)

#print the normalized points
for i in range(len(points)):
    print(f"Original Points: {points[i]}, Normalized Points: {normalized_points[i][0]}")

#assigning weights
Weight_Wins = 0.5
Weight_Points = 0.3
Weight_Constructor = 0.2

#calculte the composite score
def calculate_composite_score(data, weights):
    normalized_data = normalize_data(data)

    weighted_sum = sum(normalized_data[i] * weights[i] for i in range(len(data)))
    return weighted_sum
def normalize_data(data):
    min_value = min(data)
    max_value = max(data)
    normalized_data = [(x - min_value) / (max_value - min_value) for x in data]

    return normalized_data

data = [5,2,3]
composite_score = (Weight_Wins * data[0] + Weight_Points * data[1] + Weight_Constructor * data[2])


print("Composite Score: ", composite_score)

#to find the composite scores for each driver
composite_scores = []
for entry in standings:
    wins = int(entry['wins'])
    driver_points = float(entry['points'])
    constructor_points = 0.0
    if 'Constructors' in entry and entry['Constructors']:
        constructor_points = float(entry['Constructors'][0].get('points', 0))

    composite_score = (Weight_Wins * wins) + (Weight_Points * driver_points) + (Weight_Constructor * constructor_points)
    composite_scores.append(composite_score)

for i in range(len(drivers)):
    print(f"Driver: {drivers[i]}, Composite Score: {composite_scores[i]}")
    

    #Calculate the sum of all composite scores
    total_score = sum(composite_scores)
print("Total Score: ", total_score)
    
    
#to calculate the probability o every driver to win the race
probabilities = [(score / total_score) * 100 for score in composite_scores]
for i in range(len(drivers)):
    print(f"Driver: {drivers[i]}, Probability of Winning: {probabilities[i]: .2f}%")


    #to calculate the winner of the race
    winner_index = probabilities.index(max(probabilities))
    winner = drivers[winner_index]
print("Winner of the F1 Race held in 2021: ", winner)

    
