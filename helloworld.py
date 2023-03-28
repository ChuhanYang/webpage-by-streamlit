# Import Streamlit library
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import graphviz as graphviz
import seaborn as sns
import altair as alt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import base64
import time

# st.write("Hello")
# st.write('World!!!!')

### Text and Table Elements

# Title
st.title("""This is our Title""")
# Header
st.header("""This is our Header""")
# Sub-header
st.subheader("""This is our Subheader""")
# Caption
st.caption("""This is our Caption""")

#Displaying Plain Text
st.text("Hi,\nPeople\t!!!!!!!!!")
st.text('Welcome to')
st.text(""" Streamlit's World""")

#Displaying Markdown
st.markdown("# Hi,\n# ***People*** \t!!!!!!!!!")
st.markdown('## Welcome to')
st.markdown("""### Streamlit's World""")

#Displaying Latex
st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial u}{\partial t}
   = h^2 \left( \frac{\partial^2 u}{\partial x^2}
      + \frac{\partial^2 u}{\partial y^2}
      + \frac{\partial^2 u}{\partial z^2} \right)''')

# Displaying Python Code
st.subheader("""Python Code""")
code = '''def hello():
     print("Hello, Streamlit!")'''
st.code(code, language='python')

# Displaying Java Code
st.subheader("""Java Code""")
st.code("""public class GFG {
    public static void main(String args[])
    {
        System.out.println("Hello World");
    }
}""", language='javascript')
st.subheader("""JavaScript Code""")
st.code(""" <p id="demo"></p>
<script>
try {
  adddlert("Welcome guest!");
}
catch(err) {
  document.getElementById("demo").innerHTML = err.message;
}
</script> """)

# defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))
#st.dataframe(df)
# Highlighting minimum value objects
st.dataframe(df.style.highlight_min(axis=0))

# defining data in table
#st.table(df)

# Defining Metrics
st.metric(label="Temperature", value="31 °C", delta="1.2 °C")

#Defining Columns
c1, c2, c3 = st.columns(3)
# Defining Metrics
c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Population", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")
st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")

#Defining Nested JSON
st.json({ 
	"Books" :
    [{
    "BookName" : "Python Testing with Selenium",
    "BookID" : "1",
    "Publisher" : "Apress",
    "Year" : "2021",
    "Edition" : "First",
    "Language" : "Python",
    },
    {
        "BookName": "Beginners Guide to Streamlit with Python",
        "BookID" : "2",
        "Publisher" : "Apress",
        "Year" : "2022",
        "Edition" : "First",
        "Language" : "Python"
    }]
} )


# Dataframe in write function
st.write(pd.DataFrame({
     'column one': [5.436, 6.372, 3.645, 4.554, 7.263],
     'column two': [99, 55, 75, 41, 37],
 }))

df = pd.DataFrame(
     np.random.randn(30, 10),
     columns=('col_no %d' % i for i in range(10)))
# defining multiple arguments in write function
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

# Defining random Values for Chart
df = pd.DataFrame(
     np.random.randn(10, 2),
     columns=['a', 'b'])
# Defining Chart
chart = alt.Chart(df).mark_bar().encode(
     x='a', y='b',  tooltip=['a', 'b'])
# Defining Chart in write() function
st.write(chart)

# Magic working on Charts
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
# Magic chart
"chart", chart


### Visualization

st.title('Area')
# Defining dataframe with its values
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"])
# Bar Chart
st.bar_chart(df)
# Line Chart
st.line_chart(df)
# Area Chart
st.area_chart(df)
# Map
st.title('Map')
# Defining Latitude and Longitude
locate_map = pd.DataFrame(
  np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
  columns = ['latitude', 'longitude'])
# Map Function
st.map(locate_map)
# Graphviz dot
st.title('Graphviz')
# Creating graph object
st.graphviz_chart('''
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Result Forecasting"
        "New Data" -> "Model"
} ''')
# # We can define the same edge and nodes
# st.title('Graphviz 2')
# # Create a graphlib graph object
# graph = graphviz.Digraph()
# graph.edge('Training Data', 'ML Algorithm')
# graph.edge('ML Algorithm', 'Model')
# graph.edge('Model', 'Result Forecasting')
# graph.edge('New Data', 'Model')
# st.graphviz_chart(graph)

# Count Chart
# Data Set
df = pd.read_csv("https://raw.githubusercontent.com/Apress/beginners-guide-streamlit-python/main/chapter%203%20charts/files/avocado.csv")
# Defining Count Graph/Plot
fig = plt.figure(figsize=(10, 5))
sns.countplot(x = "year", data = df)
st.pyplot(fig)

# Violin Chart
fig = plt.figure(figsize=(10, 5))
sns.violinplot(x = "year", y="AveragePrice", data = df)
st.pyplot(fig)

# Strip Plot
fig = plt.figure(figsize=(10, 5))
sns.stripplot(x = "year", y="AveragePrice", data = df)
st.pyplot(fig)

#Read albany Dataset
df = pd.read_csv("https://raw.githubusercontent.com/Apress/beginners-guide-streamlit-python/main/chapter%203%20charts/files/albany.csv")
# Box Plot
box_plot = alt.Chart(df).mark_boxplot().encode(
x = "Date",
    y = "Large Bags"
)
st.altair_chart(box_plot)

# Area Plot
area = alt.Chart(df).mark_area(color="orange").encode(
x = "Date",
    y = "Large Bags"
)
st.altair_chart(area)

# Heatmap
heat_map  = alt.Chart(df).mark_rect().encode(
        alt.Y('AveragePrice:Q'),
        alt.X('Large Bags:Q'),
        alt.Color('AveragePrice:Q'),
        tooltip = ['AveragePrice', 'type', 'Large Bags', 'Date']
    ).interactive()
st.altair_chart(heat_map)

# Pie
data = pd.read_csv("https://raw.githubusercontent.com/Apress/beginners-guide-streamlit-python/main/chapter%203%20charts/files/avocado.csv")
st.header("Pie Chart")
# Implementing Pie Plot
pie_chart = go.Figure(
go.Pie(labels = data.type,
    values = data.AveragePrice,
    hoverinfo = "label+percent",
    textinfo = "value+percent"
))
st.plotly_chart(pie_chart)

# Donut Chart
donut_chart = px.pie(
    names = data.type,
    values = data.AveragePrice,
    hole=0.25,
)
st.plotly_chart(donut_chart)

#Scatter
st.header("Scatter Chart")
scat = px.scatter(
    x = data.Date,
    y = data.AveragePrice
)
st.plotly_chart(scat)

# Line Plot
albany_df = data[data['region']=="Albany"]
al_df = albany_df[albany_df["year"]==2015]
#Line
line_chart = px.line(
    x = al_df["Date"],
    y = al_df["Large Bags"]
)
st.header("Line Chart")
st.plotly_chart(line_chart)

line_chart.update_traces(line_color = "orange")

# Bar graph
bar_graph = px.bar(
    al_df,
    title = "Bar Graph",
    x = "Date",
    y = "Large Bags"
    )
st.plotly_chart(bar_graph)

#Bar Color
bar_graph = px.bar(
    x = al_df["Date"],
    y = al_df["Large Bags"],
    title = "Bar Graph",
    color=al_df["Large Bags"]
)
st.plotly_chart(bar_graph)

# Horizontal Bar Graph
bar_graph = px.bar(
    al_df,
    x = "Large Bags",
    y = "Date",
    title = "Bar Graph",
    color="Large Bags",
    orientation='h'
)
st.plotly_chart(bar_graph)

# Subgraphs
fig = make_subplots(rows=3, cols=1)
# First Subplot
fig.add_trace(go.Scatter(
    x=al_df["Date"],
    y=al_df["Total Bags"],
), row=1, col=1)
# Second SubPlot
fig.add_trace(go.Scatter(
    x=al_df["Date"],
    y=al_df["Small Bags"],
), row=2, col=1)
# Third SubPlot
fig.add_trace(go.Scatter(
   x=al_df["Date"],
   y=al_df["Large Bags"],
), row=3, col=1)
st.plotly_chart(fig)


### Data and Media Elements

st.write("Displaying an Images")
# Displaying Image URL
st.image("https://tinyurl.com/322vu3ab")
# Image Courtesy
st.write("Courtesy: unplash.com")

# Emojis with/without shortcodes
emojis = """:rain_cloud: :coffee: :love_hotel: :couple_with_heart: """
# Displaying Shortcodes
st.title(emojis)


### Buttons and Sliders

st.title('Creating a Button') # Defining a Button
button = st.button('Click Here')
if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')

# Radio Button
st.title('Creating Radio Buttons')
# Defining Radio Button
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")

# By default, the first radio button is selected, but you can change it by using indexing. 
st.title('Creating Radio Buttons') 
gender = ('Male', 'Female', 'Others')
# Defining Radio Button with index value
gender = st.radio(
   "Select your Gender",
    gender,
    index = 1)
if gender == 'Male':
    st.write('You have selected Male.')
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")

# Checkbox
st.title('Creating Checkboxes') 
st.write('Select your Hobies:')
# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

st.title('Pre-Select')
check = st.checkbox('Accept all Terms and Conditions***',value=True)

# Drop down
st.title('Creating Dropdown')
hobby = st.selectbox('Choose your hobby: ',
        ('Books', 'Movies', 'Sports'),
index=1)

# Multi-Select
st.title('Multi-Select')
# # Defining Multi_Select with Pre-Selection
# hobbies = st.multiselect(
#        'What are your Hobbies',
#        ['Reading', 'Cooking', 'Watching Movies/TV Series','Playing', 'Drawing', 'Hiking'],
#        ['Reading', 'Playing'])
hobbies = st.multiselect(
      'What are your Hobbies',
      ['Reading', 'Cooking', 'Watching Movies/TV Series',
      'Playing', 'Drawing', 'Hiking'])

# # Download button
# st.title("Download Button")
# # Creating Download Button
# down_btn = st.download_button(
#         label="Download Image",
#         data=open("https://raw.githubusercontent.com/Apress/beginners-guide-streamlit-python/main/chapter%205/files/fam.jpg", "rb"),
#         file_name="lions.jpg",
#         mime="image/jpg"
# )

# Spinner
st.title('Spinner')
# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')


### Forms

st.title("Text Box")
# Creating Text box
name = st.text_input("Enter your Name")
st.write("Your Name is ", name)

st.title("Text Box as Password")
password = st.text_input("Enter your password",type='password')

# Creating Text Area
input_text = st.text_area("Enter your Review")
# Printing entered text
st.write("""You entered:  \n""",input_text)

# Create number input
st.number_input("Enter your Number")

# Create number input
num = st.number_input("Enter your Number", 0, 10, 5, 2)
st.write("Min. Value is 0,  \n  Max. value is 10")
st.write("Default Value is 5,  \n  Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)

st.title("Time")
# Defining Time Function
st.time_input("Select Your Time")

st.title("Date")
# Defining Time Function
st.date_input("Select Your Date", value=datetime.date(1989,12, 25),
	min_value=datetime.date(1987, 1, 1),max_value=datetime.date(2005, 12, 1))

st.title("Select Color")
# Defining color picker
color_code = st.color_picker("Select your Color")
st.header(color_code)