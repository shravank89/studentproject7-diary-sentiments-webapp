import streamlit as st
import plotly.express as px
from glob import glob
import re
import datetime

from nltk.sentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Getting the lists for plotting
filepaths = glob("diary_pages/*.txt")
date_list = []
pos_list = []
neg_list = []
for filepath in filepaths:
    pattern = re.compile("[0-9-]+")
    finding = re.findall(pattern, filepath)
    date = datetime.datetime.fromisoformat(finding[0])
    date_string = date.strftime("%b %d %Y")

    with open(filepath) as file:
        diary = file.read()
    score = analyzer.polarity_scores(diary)
    date_list.append(date)
    pos_list.append(score["pos"])
    neg_list.append(score["neg"])


# Streamlit part
st.title("Diary Tone")
st.subheader("Positivity")

figure_pos = px.line(x=date_list, y=pos_list, labels={"x": "Date",
                                                  "y": "Positivity"})
st.plotly_chart(figure_pos)

st.subheader("Negativity")

figure_neg = px.line(x=date_list, y=neg_list, labels={"x": "Date",
                                                  "y": "Negativity"})
st.plotly_chart(figure_neg)