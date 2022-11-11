import streamlit as st
from PIL import Image
import sys
sys.path.insert(1, 'C/Users/agali/source/repos/Streamlit/Streamlit')
import FoodBot



def make_order_func (good_ing, bad_ing):
    placeholder = st.empty()
    make_order = placeholder.button('✅Готово. Зробити замовлення 👍')
    if make_order:
        placeholder.empty()
        st.markdown(f'<p><strong>Ваше замолення опрацьовується🛒. Це може зайняти декілька хвилин🕔</strong></p>', unsafe_allow_html=True)
        # якщо користувач не ввів жодних параметрів, то шукаємо піци просто
        # перевірка на те чи ігредієнти написані 
        #if isinstance(good_ing, list) and isinstance(bad_ing, list):
            
        
        if (good_ing == '' and bad_ing == '') or (len(good_ing) == 0 and len(bad_ing) == 0):
            pandagood = set()
            pandabad = []
            order = FoodBot.getCheapestPizza(pandabad, pandagood, 1) #figure out logging
            link = order[0]
            price = order[1]
            image = order[2]
            st.write("За вашими критеріями знайдено [піцу]({0}) за {1} грн".format(link, price) )
            #order_image = Image.open(r'C:\Users\agali\source\repos\Streamlit\Streamlit\images\ing_order_pizza.png')
            #st.image(order_image)
            st.image(image)
        else:
            global good_ing_set
            if good_ing == '' or len(good_ing) == 0:
                good_ing_set = set()
            else:
                if isinstance(good_ing, list):
                    good_ing_set = set(good_ing) #check maybe something is wrong here
                else:
                    good_ing_set = set(good_ing.split(', '))

            global bad_ing_list
            if bad_ing == '' or len(bad_ing) == 0:
                bad_ing_list = []
            else:
                if isinstance(bad_ing, list):
                    bad_ing_list = bad_ing
                else:
                    bad_ing_list = bad_ing.split(', ')
        order = FoodBot.getCheapestPizza(bad_ing_list, good_ing_set, 1)        
        link = order[0]
        price = order[1]
        image = order[2]
        st.write("За вашими критеріями знайдено [піцу]({0}) за {1} грн".format(link, price) )
        #order_image = Image.open(r'C:\Users\agali\source\repos\Streamlit\Streamlit\images\ing_order_pizza.png')
        #st.image(order_image)
        st.image(image)

ingredients = ['шинка', 'cир моцарела', 'ковбаса папероні', 'помідори чері', 'оливки', 'корейська морква', 'базилік', 'бекон', 'салямі', 'мисливські ковбаски', 'кальмар', 'креветка', 'неополітанський соус', 'ананас', 'моцарела', 'огірок' , 'печериці', 'маслини']


st.set_page_config(page_title="Зробити замовлення", page_icon="🛒")
st.markdown("# 🍕Давай знайдемо піцу разом")
st.sidebar.header("Зробити замовлення")

make_order_image = Image.open(r'C:\Users\agali\source\repos\Streamlit\Streamlit\images\order.jpg')
st.image(make_order_image, caption='Cheepest Online Pizza')
st.write(
    """Ми допоможемо підібрати піцу на твій смак. 
    Для того, щоб зробити замовлення потрібно спочатку вказати
   "Бажані" та "Небажані" інгредієнти."""
)

options = st.radio(
    'Бажаєте обрати ігредієнти зі списку? Чи можливо ввести самі?',
    ('Ввести самому','Обрати зі списку'))

if options == 'Ввести самому':
    st.markdown(f'<p>Будь ласка вкажіть бажані та небажані інгредієнти за наступним шаблоном:</p><p><strong>бажані інгредієнти:</strong> моцарела, шинка</p><p><strong>небажані інгредієнти:</strong> корейська морква, базилік</p><p>На випадок, якщо ви не хочете вказувати бажані або небажані інгредієнти то поставте прочерк &quot;-&quot;</p>', unsafe_allow_html=True)
    good_ing = st.text_input('Інгредієнти, які Ви любите','моцарела, шинка')
    print(good_ing)
    bad_ing = st.text_input('Інгредієнти, які Ви не любите', 'корейська морква, базилік')
    print(bad_ing)
    make_order_func(good_ing,bad_ing)

if options == 'Обрати зі списку':
    good_ing = st.multiselect(
        'Інгредієнти, які Ви любите',ingredients)
    bad_ing = st.multiselect(
        'Інгредієнти, які Ви не любите',ingredients)
    make_order_func(good_ing,bad_ing)




#for i in range(1, 101):
#    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#    status_text.text("%i%% Complete" % i)
#    chart.add_rows(new_rows)
#    progress_bar.progress(i)
#    last_rows = new_rows
#    time.sleep(0.05)

#progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
#st.button("Re-run")