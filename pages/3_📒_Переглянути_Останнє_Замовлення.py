import streamlit as st
import time
import datetime
from PIL import Image

st.set_page_config(page_title="Переглянути Останнє Замовлення", page_icon="📒")

st.markdown("# Ось який результат Ви отримали останнього разу")
st.sidebar.header("📒Переглянути Останнє Замовлення")

f = open(r"C:\Users\agali\source\repos\Streamlit\Streamlit\log_file_1.txt", "r")

lines = f.readlines()

last_lines = lines[-3:]
it_line = 1
for line in last_lines:
    if line == 'null\n':
        if it_line == 1:
            st.write("Ми не знайшли піци за Вашими критеріями на https://panda-pizza.com.ua/")
            panda_pizza_image = Image.open(r'C:\Users\agali\source\repos\Streamlit\Streamlit\images\main-panda-pizza.png')
            st.image(panda_pizza_image)                
        elif it_line == 2:
            st.write("Ми не знайшли піци за Вашими критеріями на https://smaki-maki.com/")
            smakimaki_pizza_image = Image.open(r'C:\Users\agali\source\repos\Streamlit\Streamlit\images\main-smaki-maki.png')
            st.image(smakimaki_pizza_image)                 
        elif it_line == 3:
            st.write("Ми не знайшли піци за Вашими критеріями на https://pizzaletta.com/")
            pizzaletta_pizza_image = Image.open(r'C:\Users\agali\source\repos\Streamlit\Streamlit\images\main-pizzaletta.png')
            st.image(pizzaletta_pizza_image)
    else:
        st.write(line)        
        pizza_list = line.split('\'')                
        image = pizza_list[3]
        st.image(image) 
    it_line = it_line + 1
    time.sleep(0.5)                
f.close() 
