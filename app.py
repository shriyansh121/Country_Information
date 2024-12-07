#Importing necessary Libraries
import streamlit as st
import pandas as pd
import json

# Main heading at the top
st.markdown("# 🌍 Discover the World: Learn About Countries")
st.markdown("### Explore key facts, culture, and geography of nations around the globe!")
st.markdown("---")
# List of dropdown options
options = ["Select a category","Largest Countries","Smallest Countries","Longest frontliers","Shortest frontliers","Longest Coastline","Shortest Coastline"]

# Dictionary of largest countries with area
largest_countries = {
    "Russia": "17,098,242 km²",
    "Canada": "9,984,670 km²",
    "China": "9,596,961 km²",
    "United States": "9,525,067 km²",
    "Brazil": "8,515,767 km²"
}
longest_frontliers = {
    "China": "22,143 km",
    "Russia": "20,139 km",
    "Brazil":"14,691 km",
    "India":"14,103",
    "USA":"12,248"
}
shortest_frontliers = {
    "Gibraltar":"1.2 km",
    "Vatican City": "4.0 km",
    "Monaco: ":"4.4 km",
    "Cuba":"29.0 km",
    "San Marino": "39.0 km"
}
smallest_country = {
    "Vatican City":"0.44 km²",
    "Monaco":"2 km²",
    "Nauru":"21 km²",
    "Tuvalu":"26 km²",
    "San Marino": "61 km²",
    "Liechtenstein": "160 km²"
}
long_coast = {
    "Canada":"265,523 km",
    "USA":"1333,312 km",
    "Russia":"110,310",
    "Indonesia":"95181",
    "Chile":"78563"
}
small_coast = {
    "Monaco":"4 km",
    "Bosnia-Herzegovina":"20 km",
    "Tuvalu":"24 km",
    "Jordan":"26 km",
    "Nauru": "30 km"
}
# Create a container to center-align
with st.container():
    # Create two columns for side-by-side images
    col1, col2 = st.columns([1, 1])  # Adjust column width ratios as needed
    
    with col1:
        st.image('unnamed.png', width=300)
    
    with col2:
        st.image('unnamed.webp', width=470)


# Create a dropdown
selection = st.sidebar.selectbox("Choose a category", options)

# Display the largest countries if the "Largest Countries" option is selected
if selection == "Largest Countries":
    st.write("Largest Countries by Area:")
    for country, area in largest_countries.items():
        st.write(f"{country}: {area}")
elif selection=="Longest frontliers":
    st.write("Longest Frontliers: ")
    for country,front in longest_frontliers.items():
        st.write(f"{country}: {front}")
elif selection=="Shortest frontliers":
    st.write("Shortest Frontliers: ")
    for country,short_front in shortest_frontliers.items():
        st.write(f"{country}: {short_front}")
elif selection=="Smallest Countries":
    st.write("Smallest Countries: ")
    for country,small in smallest_country.items():
        st.write(f"{country}: {small}")
elif selection=="Longest Coastline":
    st.write("Longest Coastline: ")
    for country,coast_long in long_coast.items():
        st.write(f"{country}: {coast_long}")
elif selection=="Shortest Coastline":
    st.write("Shortest Coastline: ")
    for country,coast_short in small_coast.items():
        st.write(f"{country}: {coast_short}")

north_america = ['Canada','United States','Mexico','Belize','Guatemala','Honduras','El Salvador',
'Nicaragua','Costa Rica','Panama','Cuba','Jamaica','The Bahamas','Haiti','Dominican Republic',
'St Chritopher and Nevis','Antigua and Barbuda','Dominica','St. Lucia','St. Vincent and the Grenadines',
'Barbados','Grenada','Trinidad and Tobago']
south_america =["Argentina","Bolivia","Brazil","Chile","Colombia","Ecuador","Guyana","Paraguay","Peru",
"Suriname","Uruguay","Venezuela"]
europe = ['Iceland','Norway','Sweden','Denmark','Finland','Ireland','United Kingdom','The Netherlands',
'Luxembourg','Germany','Belgium','France','Monaco','Andorra','Spain','Portugal','Malta','Italy','San Marino',
'Vatican City State','Switzerland','Liechtenstein','Belarus','Estonia','Poland','Czech Republic','Latvia',
'Austria','Lithuania','Slovakia','Hungary','Ukraine','Moldova','Georgia','Armenia','Azerbaijan','Slovenia',
'Croatia','Albania','Bosnia-Herzegovina','Macdonia','Serbia, Montenagro','Romania','Bulgaria','Greece','Cyprus']
asia = [
    'Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 
    'Brunei', 'Cambodia', 'China', 'Cyprus', 'Georgia', 'India', 'Indonesia', 
    'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan', 'Kazakhstan', 'Kuwait', 
    'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 
    'Myanmar', 'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 
    'Philippines', 'Qatar', 'Russia', 'Saudi Arabia', 'Singapore', 'South Korea', 
    'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste', 
    'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen'
]
africa = [
    'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 
    'Central African Republic', 'Chad', 'Comoros', 'Democratic Republic of the Congo', 'Republic of the Congo', 
    'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 
    'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi',
    'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 
    'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 
    'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'
]
australia = ["Australia","Papua New Guinea","New Zealand","Nauru","Palau","Solomon Islands","Vanuatu","Fiji","Tuvalu","Samoa","Kiribati","Marshall Islands"]
continent_options = ["Asia","Africa","North America","South America","Europe","Australia"]
select_continent = st.sidebar.selectbox("Choose a Continent", continent_options)
if select_continent =="North America":
    select_country = st.sidebar.selectbox("Choose a country",north_america)
    with open('North_American_Summaries.json','r') as f:
        na = json.load(f)
    if select_country in na:
        summary_text = na[select_country]
        st.write(f"### Summary of {select_country}")
        styled_text = f"""
        <div style="text-align: justify; font-size: 16px; color:lightyellow">
            {summary_text}
        </div>
        """
        st.markdown(styled_text, unsafe_allow_html=True)
    else:
        st.write("Summary for the selected country is not available.")
elif select_continent =="South America":
    select_country = st.sidebar.selectbox("Choose a country",south_america)
    with open('South_American_Summaries.json','r') as f:
        sa = json.load(f)
    if select_country in sa:
        summary_text = sa[select_country]
        st.write(f"### Summary of {select_country}")
        styled_text = f"""
        <div style="text-align: justify; font-size: 16px; color:pink">
            {summary_text}
        </div>
        """
        st.markdown(styled_text, unsafe_allow_html = True)
    else:
        st.write("Summary for the selected country is not available.")
elif select_continent =="Europe":
    select_country = st.sidebar.selectbox("Choose a country",europe)
    with open('Europe_Summaries.json','r') as f:
        eu = json.load(f)
    if select_country in eu:
        summary_text = eu[select_country]
        st.write(f"### Summary of {select_country}")
        styled_text = f"""
        <div style="text-align: justify; font-size: 16px; color:orange">
            {summary_text}
        </div>
        """
        st.markdown(styled_text, unsafe_allow_html = True)
    else:
        st.write("Summary for the selected country is not available.")
elif select_continent =="Africa":
    select_country = st.sidebar.selectbox("Choose a country",africa)
    with open('Africa_summaries.json','r') as f:
        africa = json.load(f)
    if select_country in africa:
        summary_text = africa[select_country]
        st.write(f"### Summary of {select_country}")
        styled_text = f"""
        <div style="text-align: justify; font-size: 16px; color:gold">
            {summary_text}
        </div>
        """
        st.markdown(styled_text, unsafe_allow_html = True)
    else:
        st.write("Summary for the selected country is not available.")
elif select_continent=="Asia":
    select_country = st.sidebar.selectbox("Choose a country",asia)
    with open('Asian_summary.json', 'r') as f:
        asian_summary = json.load(f)
    if select_country in asian_summary:
        summary_text = asian_summary[select_country]
        st.write(f"### Summary of {select_country}")
        styled_text = f"""
        <div style="text-align: justify; font-size: 16px; color:#98FF98">
            {summary_text}
        </div>
        """
        # Display the styled text in Streamlit
        st.markdown(styled_text, unsafe_allow_html=True)
    else:
        st.write("Summary for the selected country is not available.")
elif select_continent=="Australia":
    select_country = st.sidebar.selectbox("Choose a country",australia)
    australasia_data = pd.read_json('australasia.json')
    #australasia_summary = pd.read_json('countries_summaries.json')
    with open('Australasia_summaries.json', 'r') as f:
        australasia_summary = json.load(f)
    if select_country in australasia_data:
        country_data = australasia_data[select_country]
        # Display the country's details in a readable format
        st.write(f"### Information about {select_country}")
        for key, value in country_data.items():
            st.write(f"**{key}:** {value}")
    else:
        st.write("Data for the selected country is not available.")
    # Check if selected country's summary is available
    if select_country in australasia_summary:
        summary_text = australasia_summary[select_country]
        st.write(f"### Summary of {select_country}")
        styled_text = f"""
        <div style="text-align: justify; font-size: 16px; color: lightblue;">
            {summary_text}
        </div>
        """
        # Display the styled text in Streamlit
        st.markdown(styled_text, unsafe_allow_html=True)
    else:
        st.write("Summary for the selected country is not available.")


