import streamlit as st
import pandas as pd

# importing the data
df = pd.read_csv("Sprint3_resulting_dataframe.csv")

# dropping columns not relevant to the user, users may not know how to interpret these values
# They are only considered with fuel efficiency of vehicles and whether they are green or not, and I have given them green vehicles
df.drop(columns = ['CO2_Emissions(g/km)','CO2_Rating','Smog_Rating'], inplace=True)

# Want to filter for vehicles that are green and for which I have price data available
df = df[(df['DBScan_Labels']==0) & (df['Price'].notna())]

# Now I want user to be able to tell what Fuel Type their car actually have.
# Because currently it's a code not actual values of fuel type

# adding the dictory for fuel type
fuel_type = {
    "X": "Regular gasoline",
    "Z": "Premium gasoline",
    "D": "Diesel",
    "E": "Ethanol (E85)",
    "N": "Natural gas"
}
# mapping it to dictionary so users can understand the fuel type
df['Fuel_Type'] = df['Fuel_Type'].map(fuel_type)

# To recommend vehicles to users only choose green ones, from jupyter notebook of sprint 3 we know
# that DBScan_Labels ==0 contains green vehicles
df = df[df['DBScan_Labels'] == 0]

# users don't need to see dbscan labels so dropping it from their view
df.drop(columns=['DBScan_Labels','Unnamed: 0'],inplace = True)

# storing all vehicle classes in a list
vehicle_classes = df['Vehicle_Class'].unique().tolist()
price_start_list = ['10000','20000','30000','40000']
price_end_list = ['20000','30000','40000','50000']

# renaming the price column to Average Price so user can know this just by looking at it
df = df.rename(columns = {'Price':'Average Price(CDN)'})

# Now it is ready for the app
# my app was squished in the centre and my dataframe was cutting off found this fix
st.set_page_config(layout="wide") 

# Add title and the instruction for the user
st.title("🍃Green Vehicle Recommender System🚗")
st.markdown("<font color = 'green'>Please Select Price Range and Vehicle Class for Tailored Recommendation 😃</font>", unsafe_allow_html=True)

# adding drop down menu for user to select price range start and end and vehicle class
price_start = st.selectbox('Price_start',(price_start_list))
price_end = st.selectbox('Price_end',(price_end_list))
vehicle_class_op = st.selectbox('Vehicle Type',(vehicle_classes))

# filtering dataframe based on user input
df = df[(df['Average Price(CDN)'] >= float(price_start)) & (df['Average Price(CDN)'] < float(price_end)) & (df['Vehicle_Class']==vehicle_class_op)]
df = df.sort_values(by=['Fuel_Consumption-Comb(L/100 km)','Average Price(CDN)'], ascending=[True, True])

# styling my dataframe

# Styling the values inside the dataframe
df = df.style.set_properties(**{'background-color':'lightgreen','color':'black','border-color':'green','text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'centre')])])
# Styling the header
df.set_table_styles([{
    'selector': 'th',  # Select the table header cells
    'props': [('background-color', 'green'), ('color', 'white')]
}])

# Providing Legend for Transmission for user readability

# I tried doing it in markdown way as done in Jupyter notebook but it resulted in error so doing it in HTML
st.markdown("<p style='font-weight: bold;'>Legend for Transmission:</p>\n", unsafe_allow_html=True)
trans_legend = """
    <table border="2" width="100%">
    <tr>
    <td>A: Automatic</td>
    <td>AM: Automated Manual</td>
    <td>AS: Automatic with Select Shift</td>
    <td>AV: Continuously Variable</td>
    <td>M: Manual</td>
    <td>3-10: Number of Gears</td>
    </tr>
    </table>
"""
st.markdown(trans_legend,unsafe_allow_html=True)

# displaying my dataframe
st.table(df)