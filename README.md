# Problem Area
I am interested in solving the problem of finding budget and environmentally friendly car. How might we use machine learning to find a car that is environmentally friendly and fuel efficient within our budget? This is an important problem because the cost of living have increased, last summer gas prices went till 216cents/litre. And this summer we have seen increase in gas prices from 145cents/litre to 169cents/litre. We also have a lot of cars on the road contributing to GHG emissions into the environment and not many people can afford to buy an electric car as they are costly and there is inflation and salaries are still the same as before.
# The User
The users are millennials, zillenials and generation Z as these generations care a lot about our environmental impact and are mainly looking for either our first car or another car that is cost effective and environmentally friendly due to rising cost of living.
# The Big Idea
I found someone on Kaggle using the same Fuel Consumption dataset from the open data by government of Canada website but they seem to be using it to determine factors that influence CO2 emissions. While what I am trying to do is build a recommendation system combining different datasets to provide users suggestion on buying a car within their budget that’s environmentally friendly. This is the project I found that is using similar dataset but for different purpose: CO2 Emission by Vehicles | Kaggle
# The Impact
As mentioned in the problem area, it will help people be environmentally responsible while staying within their budget because not everyone can afford an electric vehicle and the cost of living has increased. So, it will solve 2 problems, help users choose fuel efficient cars with low CO2 emissions killing 2 birds with one stone.
# Data Dictionary for Fuel Consumption Rating dataset (main dataset)
| Column                           | Non-Null Count  | Dtype   |
|----------------------------------|-----------------|---------|
| Model_Year                       | 6951 non-null   | int64   |
| Make                             | 6951 non-null   | object  |
| Model                            | 6951 non-null   | object  |
| Vehicle_Class                    | 6951 non-null   | object  |
| Engine_Size(L)                   | 6951 non-null   | float64 |
| Cylinders                        | 6951 non-null   | int64   |
| Transmission                     | 6951 non-null   | object  |
| Fuel_Type                        | 6951 non-null   | object  |
| Fuel_Consumption-City(L/100 km)  | 6951 non-null   | float64 |
| Fuel_Consumption-Hwy(L/100 km)   | 6951 non-null   | float64 |
| Fuel_Consumption-Comb(L/100 km)  | 6951 non-null   | float64 |
| CO2_Emissions(g/km)              | 6951 non-null   | int64   |
| CO2_Rating                       | 6951 non-null   | int64   |
| Smog_Rating                      | 6951 non-null   | int64   |

# DSCapstone Task List
- [x] Collect Data for Fuel Consumption for cars
- [X] Collect prices data
- [x] Import the Data
- [x] Clean the Data for fuel consumption
    - [x] Determine null values and handle them
    - [x] Check if the data types are correct
    - [x] Check if there is any other cleaning needed (cases, similar values but diff format etc)
    - [x] look for duplicate rows and columns
    - [x] clean the header (parts of header is on line 1 and parts of it is on line 2)
- [x] Visualize the data for relationships
    - [x] Box Plot Fuel Consumption By Vehicle Class i.e. SUV, light truck, car etc
    - [x] Histogram to see the distribution of Fuel Consumption
    - [x] Box plot by Make for Fuel Consumption for each Vehicle Class
    - [x] Box plot by Make for Fuel Consumption
        - [x] add insight for all graphs 
    - [x] Box plot of CO2 rating by Vehicle Class
    - [x] Histogram to see the distribution of CO2 rating
    - [x] Box plot by Make for CO2 rating for each Vehicle Class
    - [x] Box plot by Make for CO2 rating
        - [x] add insight for all graphs 
    - [x] Box Plot of smog rating by Vehicle Class
    - [x] Histogram to see the distribution of Smog rating
    - [x] Box plot by Make for Smog Rating for each Vehicle Class
    - [x] Box plot by Make for Smog Rating
        - [x] add insight for all graphs 
- [x] Clean the prices data
    - [x] Split Make Model Year into seprate columns
    - [x] determine null values
    - [x] look for duplicate rows and columns
    - [x] check if the prices makes sense if not deal accordingly
    - [x] for one of the prices files convert USD to candian dollars from 2 years ago exchange rate
- [x] Join the prices data
       
