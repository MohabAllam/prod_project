
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout= 'wide', page_title= 'Productivity EDA')

st.image('https://news.blr.com/app/uploads/sites/3/2019/10/improve-productivity.jpg')

# st.title('Garment Employees Productivity EDA Project')

html_title = """<h1 style="color:white;text-align:center;"> Garment Employees Productivity EDA Project </h1>"""
st.markdown(html_title, unsafe_allow_html=True)

df = pd.read_csv('cleaned_df.csv', index_col= 0)

st.dataframe(df)

page = st.sidebar.radio('Pages', ['Univariate Analysis', 'MultiVariate Analysis'])

if page == 'Univariate Analysis':

    st.title('Univariate Analysis')

    for col in df.columns:

        st.plotly_chart(px.histogram(data_frame= df, x= col, title= col))

elif page == 'MultiVariate Analysis':

    prod_per_month_per_dept = (df.groupby(['month', 'department'])['actual_productivity'].mean().round(4) * 100).reset_index()
    st.plotly_chart(px.bar(data_frame= prod_per_month_per_dept, x= 'month', y= 'actual_productivity', text_auto= True, color= 'department',
        title= 'What is the average Productivity per Month per Department ?',
        labels= {'actual_productivity' : 'Average Productivity'}, barmode= 'group',
        color_discrete_sequence= ['green', 'purple']))
