import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

#requirements.txt


#Gráfica de barras
st.title('Gráfica de un dataframe: Selección de datos por los usuarios')
url = ''https://docs.google.com/spreadsheets/d/e/2PACX-1vT5rOHwOYb5BJOZNmjktyRXvsg8Xnx4jiAVL6aE35rWpDpLKyBvMA0ityVtoFytMZ1cc9K4DMebb_uU/pub?gid=782515809&single=true&output=csv'
df= pd.read_csv(url)

st.title('Gráfica de barras')

columns = df.columns.tolist()
selected_columns = st.multiselect("Selecciona la columna a graficar, debe ser tipo string", columns, default="home")
s = df[selected_columns[0]].str.strip().value_counts()

trace = go.Bar(x=s.index,y=s.values)


layout = go.Layout(title = "MLB")
data = [trace]
fig = go.Figure(data=data,layout=layout)
st.plotly_chart(fig)

#Gráfica de dispersión
st.title('Gráfica de Dispersión')
valx = st.multiselect("Selecciona un string", columns, default="Country")
valy = st.multiselect("Selecciona la métrica, que debe ser tipo número", columns, default="Ratings")

valoresx = df[valx[0]]
valoresy = df[valy[0]]

trace2 = px.scatter(df,x=valoresx.values,y=valoresy.values)
st.plotly_chart(trace2, theme="streamlit", use_container_width=True)

