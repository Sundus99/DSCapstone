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

# Sprint 1  
**File:** Capstone.ipynb  
- Data cleaning and wrangling
- EDA
- Some prices added from prices dataset to the fuel consumption rating dataset
# Sprint 2  
**File:** Capstone Sprint 2.ipynb  
- used clean data from sprint 1 ommitting the prices column as some were missing and didn't need to include prices for modeling anyways as explained in the overview of the Sprint 2 capstone
- Performed Feature Selection and Exngineering for columns with multicollinearity (dealt with numerical (VIF ANalysis) and categorical columns (chi2 test))
- Baseline Modeling, tuning, and evaluation based on only 4 features as a test
- Visualization of the clusters
- Post processing and basic analysis of the clusters
# Focus for this Sprint  
**File:** Capstone_Sprint3.ipynb  
- Use the feature selected data from Sprint 2 for further feature selection using backward selection as there are columns I am not sure about whether to include or not. These columns include, Make, Transmission_Type and Fuel_Type.
- After backward feature selection, use DBScan model as a final clustering algorithm.
- Analyze the clusters to label them as green or not green
- Add missing data for the prices and resolve any issues
- Build the streamlit app  