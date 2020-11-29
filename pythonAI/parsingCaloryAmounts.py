from bs4 import BeautifulSoup as bs
import requests as req
import json

glossary = [
    'canned-fruit', 'fruits', 'tropical-exotic-fruits', 'potato-products', 'vegetables', 'fast-food', 'pizza',
    'cheese', 'cream-cheese', 'milk-dairy-products', 'sliced-cheese', 'yogurt', 'beef-veal', 'cold-cuts-lunch-meat',
    'meat', 'pork', 'offal-giblets', 'poultry-fowl', 'sausage', 'venison-game', 'cakes-pies', 'candy-sweets',
    'ice-cream', 'spreads', 'sauces-dressings', 'pastries-breads-rolls', 'herbs-spices', 'fish-seafood',
    'baking-ingredients', 'vegetable-oils', 'oils-fats', 'nuts-seeds', 'legumes', 'soups', 'dishes-meals',
    'pasta-noodles', 'oatmeal-muesli-cereals', 'cereal-products', 'wine', 'soda-soft-drinks',
    'non-alcoholic-drinks-beverages', 'beer', 'alcoholic-drinks-beverages', 'fruit-juices'
]

foods = []

for productCategory in glossary:
    response = req.get("https://www.calories.info/food/" + str(productCategory))

    soup = bs(response.text, 'lxml')

    foodNamesHTML = soup.find_all('td', {'class': 'food'})
    caloryAmountsHTML = soup.find_all('td', {'class': 'kcal'})

    for foodName, caloryAmount in zip(foodNamesHTML, caloryAmountsHTML):
        foodName = str(foodName.text).lower()
        caloryAmount = caloryAmount.text
        if foodName != 'Food':
            foods.append({'foodName': foodName, 'foodDescription': caloryAmount})


with open('foods.json', 'w', encoding='utf-8') as f:
    json.dump(foods, f, ensure_ascii=False, indent=4)


