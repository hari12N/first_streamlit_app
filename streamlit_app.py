import pandas
import streamlit

streamlit.title('My parents new healthy diner')
streamlit.text('🥣bluberry oatmeal🥣')
streamlit.text('🥗kale and potates🥗')

my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
#streamlit.dataframe(my_fruit_list)

#Lets put a pick list here so they can pick the fruit they want
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)

