import streamlit as st
from PyPDF2 import PdfFileReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
cv = CountVectorizer()


#function to read pdf
def read_file(file):
    pdf_reader = PdfFileReader(file)
    page_count = pdf_reader.numPages
    all_text = ""
    for i in range(page_count):
        page = pdf_reader.getPage(i)
        all_text += page.extractText()

    return all_text

#function for checking
def check_similarity(text):
    count_matrix = cv.fit_transform(text)
    match_result = cosine_similarity(count_matrix) [0][1]
    result = match_result*100
    return result

def main():
    html_temp1 = """<div style="background-color:#6D7B8D;padding:10px">
                        		<h4 style="color:white;text-align:center;">Resume Similarity Checker</h4>
                        		</div>
                        		</br>"""
    st.markdown(html_temp1, unsafe_allow_html=True)
    menu = ["Home", "Check Similarity", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        # color codes  ff1a75  6D7B8D
        html_temp2 = """
                		<div style="background-color:#98AFC7;padding:10px">
                		<h4 style="color:white;text-align:center;">This application Helps you check similarity between your job description and resume. You can upload both the files in PDF or Doc formate.</h4>
                		</div>
                		<br></br>
                		<br></br>"""

        st.markdown(html_temp2, unsafe_allow_html=True)
        st.subheader("Home")
    elif choice == "Check Similarity":
        html_temp3 = """
                        		<div style="background-color:#98AFC7;padding:10px">
                        		<h4 style="color:white;text-align:center;">Upload file and check similarity between your job description and resume. You can upload both the files in PDF or Doc formate.</h4>
                        		</div>
                        		<br></br>
                        		<br></br>"""

        st.markdown(html_temp3, unsafe_allow_html=True)
        st.subheader("Check Similarity")
        doc_resume=st.file_uploader("Upload Resume", type=["pdf"]) #, "docx", "txt"
        doc_job_desc = st.file_uploader("Upload Job Description", type=["pdf"])  #, "docx", "txt"
        if st.button("Check Simlarity"):
            if doc_resume and doc_job_desc is not None:
                #read resume file
                resume_text = read_file(doc_resume)
                #st.write(resume_text)

                #read job description file
                job_des_text = read_file(doc_job_desc)
                #st.write(resume_text)

                #create a list of text
                text = [resume_text, job_des_text]
                output = check_similarity(text)
                match_percent = round(output, 2)

                st.success("Match: {}%".format(match_percent))
            else:
                st.success("Upload file")
        #st.write("Check similarity of Resume and Job Description")





if __name__ == '__main__':
    main()