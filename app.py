import streamlit as st
from feedback_analysis import FeedbackAnalysis

@st.cache(allow_output_mutation=True)
def init_analyser():
    return FeedbackAnalysis()

analyser = init_analyser()

st.title('Feedback analysis')
text = st.text_input('Enter your feedback')

if st.button('Submit'):
    sentiment, prob, cluster = analyser.predict(text)
    if sentiment == 'POSITIVE' and prob > 0.9:
        st.write('Feedback sentiment:')
        st.write('positive')
        st.write('Feedback type:')
        st.write('N/A')
    else:
        st.write('Feedback sentiment:')
        st.write('negative')
        st.write('Feedback type:')
        st.write(cluster)

