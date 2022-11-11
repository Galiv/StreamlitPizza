import streamlit as st
import time
import datetime
from PIL import Image

st.set_page_config(page_title="Переглянути Замовлення за Дату", page_icon="📒")

st.markdown("# Переглянути Замовлення за Дату")
st.sidebar.header("Переглянути Замовлення за Дату")

d = st.date_input(
    "За яку дату ви хочете переглянути замовлення?",
    datetime.date(2022, 10, 26))
dd = str(d)
with open(r"C:\Users\agali\source\repos\Streamlit\Streamlit\log_file_1.txt", "r") as ifile:    
    for line in ifile:
        #st.write(line)
        if line.startswith(dd):
            pizza_line = next(ifile, '').strip()                
            if pizza_line == 'null':
                st.write("Ми не знайшли піци за Вашими критеріями на https://panda-pizza.com.ua/")
                panda_pizza_image = Image.open(r'C:\Users\agali\source\repos\Streamlit\Streamlit\images\main-panda-pizza.png')
                pandaResizedImg = panda_pizza_image.resize((225, 325), Image.ANTIALIAS)
                st.image(pandaResizedImg)  
            else:    
                st.write(pizza_line)
                pizza_list = pizza_line.split('\'')                
                image = pizza_list[3]
                st.image(image)                  
            pizza_line = next(ifile, '').strip()                    
            if pizza_line == 'null':
                st.write("Ми не знайшли піци за Вашими критеріями на https://smaki-maki.com/")
                smakimaki_pizza_image = Image.open(r'C:\Users\agali\source\repos\Streamlit\Streamlit\images\main-smaki-maki.png')
                smakimakiResizedImg = smakimaki_pizza_image.resize((225, 325), Image.ANTIALIAS)
                st.image(smakimakiResizedImg) 
            else:    
                st.write(pizza_line)
                pizza_list = pizza_line.split('\'')                
                image = pizza_list[3]
                st.image(image)  
            pizza_line = next(ifile, '').strip()                    
            if pizza_line == 'null':
                st.write("Ми не знайшли піци за Вашими критеріями на https://pizzaletta.com/")
                pizzaletta_pizza_image = Image.open(r'C:\Users\agali\source\repos\Streamlit\Streamlit\images\main-pizzaletta.png')
                pizzalettaResizedImg = pizzaletta_pizza_image.resize((225, 325), Image.ANTIALIAS)
                st.image(pizzalettaResizedImg)                
            else:    
                st.write(pizza_line)
                pizza_list = pizza_line.split('\'')                
                image = pizza_list[3]
                st.image(image)   
        #else: st.write("У цей день у Вас не було замовлення. Спробуйте обрати інакшу дату")

ifile.close()