#cd C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts
#streamlit run C:\Users\agali\source\repos\Streamlit\Streamlit\📜_Головна_Сторінка.py

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json
import re
import operator
import time
import datetime


def getPandaPizza (badIngredients: list, goodIngredients: set) -> list:
   
    priceList = []
    ingredientsList = []
    imageList = []
    pizzaIndexs = []
    pizzaIndex = 0
    checker = None  


    html = urlopen("https://panda-pizza.com.ua/sitemap.xml")  
    


    bsObj = BeautifulSoup(html.read(),features="html.parser")
    myL = bsObj.find_all("loc")
    pizza = "https://panda-pizza.com.ua/dishes/pizza/"
    #listOfPizzas = [item.string for item in myL if pizza in item.string]



    #here you can see the list
    listOfPizzas = ['https://panda-pizza.com.ua/dishes/pizza/pitsa-romeo', 
                   'https://panda-pizza.com.ua/dishes/pizza/pitsa-leonardo',
                   'https://panda-pizza.com.ua/dishes/pizza/pitsa-boloniya',
                   'https://panda-pizza.com.ua/dishes/pizza/pitsa-peperchi',
        #           'https://panda-pizza.com.ua/dishes/pizza/pitsa-napoli', 
        #           'https://panda-pizza.com.ua/dishes/pizza/pitsa-margarita', 
        #          'https://panda-pizza.com.ua/dishes/pizza/pitsa-rafaelo',
        #          'https://panda-pizza.com.ua/dishes/pizza/pitsa-barbekyu',
        #         'https://panda-pizza.com.ua/dishes/pizza/pitsa-gavayska',
        #        'https://panda-pizza.com.ua/dishes/pizza/pitsa-sardiniya',
             'https://panda-pizza.com.ua/dishes/pizza/pitsa-peperoni']
         
    #print(listOfPizzas)  
    

   
    # Looking for pizzas which I don't like
    for pizza in listOfPizzas: 
        print(pizza)
        checker = True
        pizzahtml = urlopen(pizza)
        bs = BeautifulSoup(pizzahtml.read(),features="html.parser")
        ingredients_place = bs.find("div","popup-pizza-header")
        

        for item in ingredients_place:
            ingredientsList.append(item.string)            
        ingList = ingredientsList[3].split(', ')
        # ingLowerCase -  ловкейсом список 
        # ['неополітанський соус', 'сир моцарелла', 'шинка', 'печериці свіжі', 'маслини']
        ingLowerCase = [element.lower() for element in ingList] 
        for badIng in badIngredients:
            for ing in ingLowerCase:            
                if badIng in ing:
                    print('Bad Ing', badIng, ' ' , pizzaIndex)
                    checker = False                                   
                    break
        if checker == True:
            ingredientsSet = set(ingLowerCase)
            if (goodIngredients.issubset(ingredientsSet) == True):
                pizzaIndexs.append(pizzaIndex)                
                regex = re.compile(r'data-base-price="(\d+)"')
                result = regex.search(str(bs))
                priceList.append(float(result.group(1)))
                image_place = bs.find("img","img-zoom")
                pizza_image=image_place["src"]
                imageList.append(pizza_image)
        ingredientsList.clear() 
        ingList.clear()
        pizzaIndex += 1         

    if not priceList:
        print('Unfortunately there are no pizzas which satisfy your conditions')
        return 0
    else:   
        minPriceIndex = priceList.index(min(priceList))
        print (listOfPizzas[pizzaIndexs[minPriceIndex]], priceList[minPriceIndex], imageList[minPriceIndex])
        return listOfPizzas[pizzaIndexs[minPriceIndex]], priceList[minPriceIndex], imageList[minPriceIndex]

def getSmakiPizza (badIngredients: list, goodIngredients: set) -> list:
    
    html = urlopen("https://smaki-maki.com/picza/")

    
    bsObj = BeautifulSoup(html.read(),features="html.parser")
        
    ingredientLists = []
    pizzaNames = []
    ingredients = []
    strip_ing = []
    normalList = []
    price = []
    pizzaDict = {}
    priceDict = {}
    count = 2
    pizzaIndex = 0
    images = []
    

    #ingredients_place = bsObj.findAll("p", {"class": "storage"})
    #for item in ingredients_place:
    #            ingredientLists.append(item.string[1:])
    #print(ingredientLists)
    #pizza_place = bsObj.findAll("a", {"class": "product-name"})
    #for item in pizza_place:
    #            pizzaNames.append(item.string)

    #price_place = bsObj.findAll("p", {"class": "product-price"})
    #for item in price_place:
    #           price.append(re.findall("([0-9]+[.]+[0-9]+)", str(item)))

    ingredients_place = bsObj.findAll("div", {"class": "product_description"})
    for item in ingredients_place:
                ingredientLists.append(item.string[1:])
    
    pizza_place = bsObj.findAll("a", {"class": "product_title"})
    for item in pizza_place:
                pizzaNames.append(item.string)
    

    price_place = bsObj.findAll("span", {"class": "price"})
    for item in price_place:
               price.append(re.findall("([0-9]+[.]+[0-9]+)", str(item)))    
    
    image_place = bsObj.findAll("a", {"class": "product_image"})
    for item in image_place:
                images.append(item)
    

    links = bsObj.findAll('a', attrs={'href': re.compile("^https://smaki-maki.com/")})


    for item in ingredientLists:
    
        # item - стрінга, список інгредієнтів однієї піци
        # Неополітанський соус, Сир моцарелла, Шинка, Печериці свіжі, Маслини
        # ingredients - список у якому поелементно записані інгрідієнти
        # ['            Неополітанський соус', 'Сир моцарелла', 'Шинка', 'Печериці свіжі', 'Маслини        ']
        ingredients = item.split(', ')  
    
        for ing in ingredients:
            strip_ing.append(ing.strip())
        # new_strip_ing - затрімений та з ловкейсом список 
        # ['неополітанський соус', 'сир моцарелла', 'шинка', 'печериці свіжі', 'маслини']
        new_strip_ing = [element.lower() for element in strip_ing]   

        # pizzaDict - словник назв піц та їх інгредієнтів
        pizzaDict[pizzaNames[pizzaIndex]] = new_strip_ing

        # pizzaDict - словник назв піц та їх цін
        temp_list = [price[count-2], price[count-1], price[count]]
        priceDict[pizzaNames[pizzaIndex]] = temp_list
        count = count + 3
        # апендимо список new_strip_ing та перевіряємо на погані інгредієнти
  
        normalList.append(new_strip_ing)
        for badIng in badIngredients:                
                for ing in new_strip_ing:            
                    if badIng in ing:
                        print('Bad Ing', badIng, ' ' , pizzaIndex)
                        # POPING THE PIZZAS I DON'T LIKE    
                        if new_strip_ing in normalList:                        
                            normalList.remove(new_strip_ing)                         
                        break                           
        pizzaIndex = pizzaIndex + 1    
        strip_ing.clear()

    finalListsOfgoodIngredients = []
    result = []

    for l in normalList:        
        if (goodIngredients.issubset(l) == True):
            finalListsOfgoodIngredients.append(l)    
    #Check if list is empty. If so, customer needs to change the ingredients
    if not finalListsOfgoodIngredients:
        print('Unfortunately there are no pizzas which satisfy your conditions')
    else:
        myind = []
        finalDict = {}

        for name, ingred in pizzaDict.items():   
            for item in finalListsOfgoodIngredients:
                if item == ingred:
                    myind.append(name)
        
        for name, price in priceDict.items():
            for item in myind:
                if item == name:
                    finalDict[name] = price[1]
                
        pizza = (min(finalDict.items(), key=operator.itemgetter(1))[0])
    
        #Getting the link here
        for item in links:    
            if pizza in item: 
                #Printing the name, list of prices for three sizes (s,m,l) and the url
                #print(pizza, priceDict.get(pizza), (str(item)).split('"')[3])
                #result.append(pizza)
                result.append((str(item)).split('"')[3])
                realprice = priceDict.get(pizza)[1]
                result.append(float(realprice.pop()))                
                             
    return result

def getPizzaLettaPizza (badIngredients: list, goodIngredients: set) -> list:

    html = urlopen("https://pizzaletta.com/sitemap-pt-product-2019-11.xml")
    bsObj = BeautifulSoup(html.read(),features="html.parser")
    myL = bsObj.find_all("loc")
    pizza = "https://pizzaletta.com/product/dostavka"
    listOfPizzas = [item.string for item in myL if pizza in item.string]
    
    ingredientsList = []
    pizzaIndexs = []       
    priceListWithOtherStrings = []    
    priceList = []
    imageList = []
    imageWithOtherStrings = []
    checker = None  
    pizzaIndex = 0

    for pizza in listOfPizzas:
        checker = True       
        pizzahtml = urlopen(pizza)
        bs = BeautifulSoup(pizzahtml.read(),features="html.parser")
        #ingredients_place = bs.find("div","text text-light")
        ingredients_place = bs.find("div","text text-light hide-mob prod-desc")
        for item in ingredients_place:
            # item.string = '\n\t\t\t\t\t\t\t\t\tСоус BBQ, моцарела, мисливські ковбаски, кукурудза, корейська морква\t\t\t\t\t\t\t\t'
            #getting rid of \t and \n
            ingredientsList.append(item.string)
            ingredientsList.append(ingredientsList[0].replace('\t', ''))
            ingredientsList.append(ingredientsList[1].replace('\n', ''))            
        ingList = ingredientsList[2].split(', ')
        for badIng in badIngredients:         
            for ing in ingList:
                if badIng in ing:
                    print('Bad Ing', badIng, ' ' , pizzaIndex)
                    checker = False
                    break
        if checker == True:
            ingredientsSet = set(ingList)            
            if (goodIngredients.issubset(ingredientsSet) == True):
                pizzaIndexs.append(pizzaIndex)                

                price_place = bs.find("span", "item-price const text text-sm text-light hide-mob")                
                for item in price_place:                            
                    priceListWithOtherStrings.append(item.string)
                priceList.append(priceListWithOtherStrings[1])
                priceListWithOtherStrings.clear() 

                image_place = bs.find("div","item-page-banner overflow-hidden animation simple-animation pizza-banner")
                for item in image_place:
                    imageWithOtherStrings.append(str(item))
                imageString = imageWithOtherStrings[1].split("\"") 
                imageList.append(imageString[3])            
                imageWithOtherStrings.clear()
        ingredientsList.clear()
        ingList.clear()
        pizzaIndex += 1
   
    if not priceList:
        print('Unfortunately there are no pizzas which satisfy your conditions')
        return 0
    else:
        intPrices = list(map(int, priceList))
        minPriceIndex = intPrices.index(min(intPrices))
        return listOfPizzas[pizzaIndexs[minPriceIndex]], intPrices[minPriceIndex], imageList[minPriceIndex]        

def getCheapestPizza (badIngredients: list, goodIngredients: set, chat: int):

    # розкоментувати, якщо вирішив робити логування
    f = open(r"C:\Users\agali\source\repos\Streamlit\Streamlit\log_file_{0}.txt".format(chat), "a+")
    date_now = datetime.datetime.now()
    f.write(str(date_now)+"\n")
    
    
    listOfPizzas = []
    panda = getPandaPizza (badIngredients, goodIngredients)
    print(panda)
    if panda == 0:
        #f.write("Ми не знайшли піци за Вашими критеріями на https://panda-pizza.com.ua/ \n")
        f.write("null\n")
    else:
        f.write(str(panda)+"\n")

    smaki = getSmakiPizza (badIngredients, goodIngredients)
    print(smaki)
    if not smaki:
        #f.write("Ми не знайшли піци за Вашими критеріями на https://smaki-maki.com/ \n")
        f.write("null\n")
    else:
        f.write(str(smaki)+"\n")
    

    letta = getPizzaLettaPizza (badIngredients,goodIngredients)
    print(letta)
    if letta == 0:
        f.write("null\n")
    else:
        f.write(str(letta)+"\n")

    f.close()

    if not panda and not smaki and not letta:
        return ("Msg")

    if not panda and not smaki:
        return (letta)

    if not panda and not letta:
        return (smaki)

    if not smaki and not letta:
        return (panda)

    if not panda:
        if smaki[1] < letta[1]:
            return (smaki)
        elif smaki[1] > letta[1]:
            return (letta)
        else: 
            print ("There are two options for you:")
            listOfPizzas.append(letta)
            listOfPizzas.append(smaki)
            return listOfPizzas            

    if not smaki:
        if panda[1] < letta[1]:
            return (panda)            
        elif panda[1] > letta[1]:
            return (letta)            
        else:             
            print ("There are two options for you:")
            listOfPizzas.append(letta)
            listOfPizzas.append(panda)
            return listOfPizzas                

    if not letta:
        if panda[1] < smaki[1]:
            return (panda)
        elif panda[1] > smaki[1]:
            return (smaki)
        else: 
            print ("There are two options for you:")
            listOfPizzas.append(smaki)
            listOfPizzas.append(panda)
            return listOfPizzas

    if panda and letta and smaki:
        if smaki[1] < panda[1] and smaki[1] < letta[1]:
            return (smaki)
        elif panda[1] < smaki[1] and panda[1] < letta[1]:
            return (panda)
        elif letta[1] < panda[1] and letta[1] < smaki[1]:
            return (letta)
        elif smaki[1] == letta[1] and smaki[1] == panda[1] and letta[1] == panda[1]:
            print ("There are three options for you:")
            listOfPizzas.append(smaki)
            listOfPizzas.append(panda)
            listOfPizzas.append(letta)
            return listOfPizzas
        elif smaki[1] == letta[1]:
            print ("There are two options for you:")
            listOfPizzas.append(letta)
            listOfPizzas.append(smaki)
            return listOfPizzas 
        elif smaki[1] == panda[1]:
            print ("There are two options for you:")
            listOfPizzas.append(smaki)
            listOfPizzas.append(panda)
            return listOfPizzas
        elif letta[1] == panda[1]:
            print ("There are two options for you:")
            listOfPizzas.append(letta)
            listOfPizzas.append(panda)
            return listOfPizzas 
        return ("Msg")
    



