import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Streamlit app sarlavhasi
st.title("Streamlit uchun vizualizatsiya demo")

# Ma'lumotlar to'plamini yaratish (example: random data)
@st.cache
def load_data():
    # Tasodifiy ma'lumotlar yaratamiz
    data = {
        'Kategoriya': ['A', 'B', 'C', 'D', 'E'],
        'Qiymat': [23, 45, 56, 78, 33],
        "O'sish": [2.3, 3.4, 4.5, 6.7, 3.4]
    }
    df = pd.DataFrame(data)
    return df

# Ma'lumotlarni yuklash
df = load_data()

# DataFrame'ni ko'rsatish
st.write("Yuklangan ma'lumotlar:", df)

# Seaborn bilan bar chart
st.subheader('Seaborn bilan bar chart')
fig, ax = plt.subplots()
sns.barplot(x='Kategoriya', y='Qiymat', data=df, ax=ax)
st.pyplot(fig)

# Plotly bilan interaktiv grafika
st.subheader('Plotly bilan interaktiv grafika')
fig_plotly = px.bar(df, x='Kategoriya', y='Qiymat', title="Plotly Bar Chart")
st.plotly_chart(fig_plotly)

# Qolgan qismda qo'shimcha interaktiv elementlar ham qo'shish mumkin
st.subheader("Interaktiv elementlar")
kategoriyalar = st.multiselect('Kategoriyani tanlang:', df['Kategoriya'].unique(), default=df['Kategoriya'].tolist())
st.write(f"Siz tanlagan kategoriyalar: {kategoriyalar}")

# Tanlangan kategoriyalarga qarab datafiltrlash
filtered_data = df[df['Kategoriya'].isin(kategoriyalar)]
st.write("Filtrlangan ma'lumotlar:", filtered_data)
