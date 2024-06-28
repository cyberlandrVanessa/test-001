from transformers import pipeline
import streamlit as st
from streamlit.components.v1 import html
import json

# Initialize pipeline globally to avoid reloading it every time
pipe = pipeline('sentiment-analysis')

# Functions
def open_page(url):
    open_script = f"""
        <script type="text/javascript">
            window.open('{url}', '_blank').focus();
        </script>
    """
    html(open_script)

def analyseReview(textIn):   
    if textIn:
        out = pipe(textIn)
        first_element = out[0]
        label = first_element["label"]
        score = first_element["score"] * 100  # Convert to percentage
        #st.header(f"There is a {score:.2f}% probability that you have {label} feelings about the movie.")
        html_str = f"""
        <style>
        p.a {{
          color: white;
          background-color: black;
          font: 15px Arial;
        }}
        </style>
        <p class="a"><br>&nbsp;&nbsp There is a {score:.2f}% probability that you have {label} feelings about the movie.&nbsp;&nbsp&nbsp<br>&nbsp</p>
        """
        st.markdown(html_str, unsafe_allow_html=True)
        st.json(out)
 
def main():
    st.write("_______________________________________")
    st.button('View README file', on_click=open_page, args=('https://docs.google.com/document/d/1vfzPba5eqSnfXkRSk6Z-mWvx67zz67ghw9XwfZ3R41E/edit?usp=sharing',))
    st.title("App 01: Movie Sentiment Analysis TTT")
    st.header("HuggingFace, Json, Python, Streamlit, Transformers")
    text = st.text_area('Write a review of the last movie you saw then press Review It.')
    
    if st.button('Review It!'):
        analyseReview(text)

# Logic
if __name__ == '__main__':
    main()