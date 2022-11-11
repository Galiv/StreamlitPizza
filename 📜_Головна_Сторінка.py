import streamlit as st
from PIL import Image
import time
import datetime
import FoodBot


st.set_page_config(
    page_title="Головна сторінка",
    page_icon="👋",
)

st.sidebar.success("Оберіть будь ласка одну з опцій☝")

first_time_keyboard = [
     '🥒🌶🍅Вказати інгредієнти🥕🧄🧅',
     '📒Переглянути останнє замолення',
     '📓Переглянути замолення за дату',     
     '🍕Знайти піцу без бажаних інгредієнтів',
     '🆘Допомога',
]

 

st.title('Найдешевша Онлайн Піца 👋')
image = Image.open(r'C:\Users\agali\source\repos\Streamlit\Streamlit\images\banner_pizza.png')

panda_pizza_image = Image.open(r'C:\Users\agali\source\repos\Streamlit\Streamlit\images\main-panda-pizza.png')
smakimaki_pizza_image = Image.open(r'C:\Users\agali\source\repos\Streamlit\Streamlit\images\main-smaki-maki.png')
pizzaletta_pizza_image = Image.open(r'C:\Users\agali\source\repos\Streamlit\Streamlit\images\main-pizzaletta.png')

resizedImg1 = panda_pizza_image.resize((225, 325), Image.ANTIALIAS)
resizedImg2 = smakimaki_pizza_image.resize((225, 325), Image.ANTIALIAS)
resizedImg3 = pizzaletta_pizza_image.resize((225, 325), Image.ANTIALIAS)
st.image([resizedImg1,resizedImg2, resizedImg3], width=200)



st.image(image, caption='Cheepest Online Pizza')
