import streamlit as st
import pandas as pd
import numpy as np


st.title("hello world")

st.header('This is a header with divider', divider='rainbow')

st.markdown("this is with markdown")

col1, col2 = st.columns(2)



x = st.slider('choose an x value', 1, 10)

st.write('value of :red[x] is', x)

st.subheader('area chart')

chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
)

st.area_chart(chart_data, x="col1", y="col2", color="col3")