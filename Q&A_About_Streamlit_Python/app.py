# Load Pkgs
import streamlit as st 
import matplotlib.pyplot as plt


st.subheader("Frequently Asked Questions About Streamlit")

## How to Show Help and Docs
st.subheader("How to Show Help and Docs?")
# Method 1
st.help(st)

# Method 2
result = dir(st)
st.write(result)

## How to Link to Pages
st.subheader("How to Link to Pages?")
# Using Markdown
st.markdown("[I'm an inline-style link](https://www.google.com)")


## How to Show Pie Charts
st.subheader("How to Show Pie Charts")
if st.checkbox("Show Pie Charts"):
	labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
	sizes = [15, 30, 45, 10]
	explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
	        shadow=True, startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

	st.pyplot()

## How to Receive User Input
st.subheader("How to Receive User Input")
name = st.text_input("Enter Your Name","Type Here")
result_name = name.title()
st.write(result_name)