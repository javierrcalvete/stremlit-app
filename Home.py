import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff

st.sidebar.header('Retails app')

st.title("hello world")

st.header('This is a header with divider', divider='rainbow')

st.markdown("this is with markdown")





x = st.slider('choose an x value', 1, 10)

st.write('value of :red[x] is', x)

st.subheader('area chart')

col1, col2 = st.columns(2)

chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
)

with col1:

    st.dataframe(chart_data,)

with col2:
    
    st.area_chart(chart_data, x="col1", y="col2", color="col3")

st.subheader('math')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.divider()




# Cache the histogram data
@st.cache_data
def generate_histogram():
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    hist_data = [x1, x2, x3]
    group_labels = ['Group 1', 'Group 2', 'Group 3']
    
    fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
    return fig

# Display the histogram
st.subheader('Histogram')
if 'histogram_fig' not in st.session_state:
    st.session_state.histogram_fig = generate_histogram()

st.plotly_chart(st.session_state.histogram_fig, use_container_width=True)