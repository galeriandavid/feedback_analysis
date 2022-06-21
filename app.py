import streamlit as st
from feedback_analisys import FeedbackAnalisys

@st.cache(allow_output_mutation=True)
def init_analyser():
    return FeedbackAnalisys()

analyser = init_analyser()

st.title('Feedback analisys')
text = st.text_input('Enter your feedback')

if st.button('Submit'):
    sentiment, prob, cluster = analyser.predict(text)
    if sentiment == 'POSITIVE' and prob < 0.9:
        sentiment = 'NEGATIVE'
    st.write('Feedback sentiment:')
    st.write(sentiment.lower())
    st.write('Feedback type:')
    st.write(cluster)

