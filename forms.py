### Forms
import streamlit as st
import datetime
import docx2txt
import pdfplumber
import pandas as pd
from PIL import Image
import io
import os


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



#### File Upload
st.title("DOCX & Text Documents")
# Defining File Uploader Function in a variable
text_file = st.file_uploader("Upload Document",
type=["docx","txt"])
# Button to check document details
details = st.button("Check Details")
# Condition to get document details
if details:
    if text_file is not None:
        # Getting Document details like name, type and size
        doc_details = {"file_name":text_file.name, "file_type":text_file.type,"file_size":text_file.size}
        st.write(doc_details)
        # Check for text/plain document type
        if text_file.type == "text/plain":
            # Read document as string with utf-8 format
            raw_text = str(text_file.read(),"utf-8")
            st.write(raw_text)
        else:
            # Read docx document type
            docx_text = docx2txt.process(text_file)
            st.write(docx_text)


st.title("PDF File")
pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
pdf_button_key = "pdf_details_button"
details_pdf = st.button("Check Details", key=pdf_button_key)
if details_pdf :
    if pdf_file is not None:
        pdf_details = {"filename":pdf_file.name,
        "filetype":pdf_file.type,
                        "filesize":pdf_file.size}
        st.write(pdf_details)
        pdf = pdfplumber.open(pdf_file)
        pages = pdf.pages[0]
        st.write(pages.extract_text())
    else:
        st.write("No PDF File is Uploaded")



st.title("CSV Data")
data_file = st.file_uploader("Upload CSV",type=["csv"])
csv_button_key = "csv_details_button"
details_csv = st.button("Check Details",key=csv_button_key)
if details_csv:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type":data_file.type, "file_size":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")


st.title("Upload Image")
image_file = st.file_uploader("Upload Images",
type=["png","jpg","jpeg"])
image_button_key = "image_details_button"
check_details = st.button("Check Details",key=image_button_key)
if check_details:
    if image_file is not None:
            # To See details
            image_details = {"file_name":image_file.name,
            "file_type":image_file.type,
                            "file_size":image_file.size}
            st.write(image_details)
            # To View Uploaded Image
            image_data = image_file.read()
            image = Image.open(io.BytesIO(image_data))
            st.image(image, width=250)
    else:
        st.write("No Image File is Uploaded")


uploaded_files = st.file_uploader("Multiple Image Uploader",
					type=['jpg','jpeg','png'],
                    help="Upload Images in jpg, jpeg, png format", accept_multiple_files=True,)
multi_img_details = st.button("Check Details",key = "multi_img_button")
for uploaded_file in uploaded_files:
    if multi_img_details:
        if uploaded_file is not None:
            bytes_data = uploaded_file.read()
            image = Image.open(io.BytesIO(bytes_data))
            st.write("file_name:", uploaded_file.name)
            st.image(image, width=100)
        else:
            st.write("No Image File is Uploaded")
            break



# # Defining File Upload Method of Streamlit
# st.title("Saving File to Directory")
# image_file = st.file_uploader("Upload Images",
#             type=["png","jpg","jpeg"])
# # Defining path where file to be saved
# file_save_path = "F:/Books/Apress Streamlit/Chapters/02 Codes/chapter 6 forms/files"
# save_file = st.button("Check Details & Save")
# if save_file:
#     if image_file is not None:
#             # To See details
#             image_details = {"file_name":image_file.name,
#             "file_type":image_file.type,
#                             "file_size":image_file.size}
#             st.write(image_details)
#             # To View Uploaded Image
#             image_data = image_file.read()
#             image = Image.open(io.BytesIO(image_data))
#             st.image(image, width=250)
#             with open(os.path.join(file_save_path,image_file.
#             name),"wb") as f:
#                 f.write((image_file).getbuffer())
#             st.success("Image Saved Successfully")
#     else:
#         st.write("No Image File is Uploaded")     


my_form = st.form(key='form')
my_form.text_input(label='Enter any text')
# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')          