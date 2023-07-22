# This is a Data Science Project 
# 2021 F1 Championship

This project is to find the probability of each driver for winning the championship.
Then, according to the probabilities, finding the winner 

my page link:
<https://github.com/VanshikaNagarajan/python_project_F1>

my code link:
<https://github.com/VanshikaNagarajan/python_project_F1/blob/master/P1%20to%20calculate%202021%20winner%20probability.py>



1. importing the modules
        
    this code imports json, pandas, scikit-learn, requests.
2. defining the API urls
    
    these urls are taken from a API documentation website 
    <>
3. to get requests from API 
    
    here we create an object called response and with the help of it we create functions.

    requests - to make https requests.
    get() , used to get the value of any specified key from a dictionary. 

The specified data gets retrieved.

4. to check weather the data is retreived or not
    
    status code is used.

5. to load and print the data in json 

6. to print the points, driver details and stadings data.

7. to normalize the points/data between 0 and 1

normalizing is important because it makes the points easy to read, to get better and faster results. 

points are first scaled between 0 and 1 by a function called MinMaxScaler(). 

next, Scaler.fit_transform() is used to reshape the data. 

the points are in made in sorted array.

After, normalizing the data, next is to assign the weights.

8. taken 3 objects(to assign weights)

weight_win
weight_points
weight_constructor

the weights are assigned according the positions of the driver from the given data.

9. to calculate the composite score 

        composite_score = (Weight_Wins * data[0] + Weight_Points * data[1] + Weight_Constructor * data[2])

10. to calculate the composite score for each driver

        composite_score = (Weight_Wins * wins) + (Weight_Points * driver_points) + (Weight_Constructor * constructor_points)
        composite_scores.append(composite_score)

11. to calculate the sum of all composite scores

        total_score = sum(composite_scores)


12. to calculate the probability of every driver for winning the race 


        probabilities = [(score / total_score) * 100 for score in composite_scores]

13. to calculate the winner of the race acording to the found probabilities 

        winner_index = probabilities.index(max(probabilities))
        winner = drivers[winner_index]



 

 [reference image(output)] link:
 <https://github.com/VanshikaNagarajan/python_project_F1/tree/master/output>