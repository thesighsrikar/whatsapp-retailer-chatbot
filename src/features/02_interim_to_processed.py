import pandas as pd
import numpy as np

atta_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_atta-flours-sooji.csv"
atta_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_atta-flours-sooji.csv"
df_atta = pd.read_csv(atta_path)

df_atta.columns = ['ProductName', 'SellingPrice', 'NumOfRatings', 'Mrp',
       'Discount', 'Brand', 'Rating', 'Combos', 'QuantityDisplay']

spec_chars = ["!",'"',"#","%","&","'","(",")",
              "*","+",",","-",".","/",":",";","<",
              "=",">","?","@","[","\\","]","^","_",
              "`","{","|","}","~","–"]

df_atta = df_atta[df_atta['ProductName'].notna()]

for char in spec_chars:
    df_atta['ProductName'] = df_atta['ProductName'].str.replace(char, ' ')
    df_atta['Brand'] = df_atta['Brand'].str.replace(char, ' ')
    df_atta['Combos'] = df_atta['Combos'].str.replace(char, ' ')
    df_atta['QuantityDisplay'] = df_atta['QuantityDisplay'].str.replace(char, ' ')
    
df_atta.to_csv(atta_export_path, index=False, header=True)



cakes_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_bakery-cakes-diary.csv"
cakes_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_bakery-cakes-diary.csv"

df_cakes = pd.read_csv(cakes_path)
df_cakes.head()

df_cakes.columns = ['ProductName', 'NumOfRatings', 'SellingPrice', 'Brand', 'Mrp',
       'Combos', 'Discount', 'Rating', 'QuantityDisplay']

df_cakes = df_cakes[df_cakes['ProductName'].notna()]

for char in spec_chars:
    df_cakes['ProductName'] = df_cakes['ProductName'].str.replace(char, ' ')
    df_cakes['Brand'] = df_cakes['Brand'].str.replace(char, ' ')
    df_cakes['Combos'] = df_cakes['Combos'].str.replace(char, ' ')
    df_cakes['QuantityDisplay'] = df_cakes['QuantityDisplay'].str.replace(char, ' ')
    
df_cakes.to_csv(cakes_export_path, index=False, header=True)



bath_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_bath-handwash.csv"
bath_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_bath-handwash.csv"

df_bath = pd.read_csv(bath_path)
df_bath.columns = ['ProductName', 'NumOfRatings', 'SellingPrice', 'Brand', 'Mrp',
       'Discount', 'Combos', 'Rating', 'QuantityDisplay']

df_bath = df_bath[df_bath['ProductName'].notna()]

for char in spec_chars:
    df_bath['ProductName'] = df_bath['ProductName'].str.replace(char, ' ')
    df_bath['Brand'] = df_bath['Brand'].str.replace(char, ' ')
    df_bath['Combos'] = df_bath['Combos'].str.replace(char, ' ')
    df_bath['QuantityDisplay'] = df_bath['QuantityDisplay'].str.replace(char, ' ')
    
df_bath.to_csv(bath_export_path, index=False, header=True)



cookies_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_biscuits-cookies.csv"
cookies_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_biscuits-cookies.csv"

df_cookies = pd.read_csv(cookies_path)
df_cookies.columns = ['ProductName', 'NumOfRatings', 'SellingPrice', 'Combos',
       'QuantityDisplay', 'Mrp', 'Brand', 'Discount', 'Rating']

df_cookies = df_cookies[df_cookies['ProductName'].notna()]

for char in spec_chars:
    df_cookies['ProductName'] = df_cookies['ProductName'].str.replace(char, ' ')
    df_cookies['Brand'] = df_cookies['Brand'].str.replace(char, ' ')
    df_cookies['Combos'] = df_cookies['Combos'].str.replace(char, ' ')
    df_cookies['QuantityDisplay'] = df_cookies['QuantityDisplay'].str.replace(char, ' ')
    
df_cookies.to_csv(cookies_export_path, index=False, header=True)



breakfast_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_breakfast-cereals.csv"
breakfast_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_breakfast-cereals.csv"

df_break = pd.read_csv(breakfast_path)
df_break.columns = ['NumOfRatings', 'ProductName', 'SellingPrice', 'Combos', 'Mrp',
       'Discount', 'Brand', 'Rating', 'QuantityDisplay']

df_break = df_break[df_break['ProductName'].notna()]

for char in spec_chars:
    df_break['ProductName'] = df_break['ProductName'].str.replace(char, ' ')
    df_break['Brand'] = df_break['Brand'].str.replace(char, ' ')
    df_break['Combos'] = df_break['Combos'].str.replace(char, ' ')
    df_break['QuantityDisplay'] = df_break['QuantityDisplay'].str.replace(char, ' ')
    
df_break.to_csv(breakfast_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_choclates-candies.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_choclates-candies.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['NumOfRatings', 'ProductName', 'SellingPrice', 'Combos', 'Brand',
       'Mrp', 'Discount', 'Rating', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_dals-pulses.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_dals-pulses.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'NumOfRatings', 'SellingPrice', 'Mrp',
       'Discount', 'Brand', 'Rating', 'QuantityDisplay', 'Combos']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_dry-fruits.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_dry-fruits.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'SellingPrice', 'NumOfRatings', 'Mrp',
       'Discount', 'Rating', 'Brand', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_edible-oils-ghee.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_edible-oils-ghee.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['SellingPrice', 'NumOfRatings', 'ProductName', 'Mrp',
       'Discount', 'Brand', 'Rating', 'Combos', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_eggs-meat-fish.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_eggs-meat-fish.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'SellingPrice', 'Brand', 'Mrp', 'Discount',
       'Combos', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_feminine-hygiene.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_feminine-hygiene.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'SellingPrice', 'NumOfRatings', 'Mrp', 'Brand',
       'Combos', 'Rating', 'Discount', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_frozen-veggies-snacks.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_frozen-veggies-snacks.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['NumOfRatings', 'ProductName', 'SellingPrice', 'Mrp', 'Brand',
       'Discount', 'Rating', 'Combos', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_fruits-vegetables.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_fruits-vegetables.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'SellingPrice', 'Mrp', 'Combos', 'Discount',
       'Brand', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_indian-mithai.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_indian-mithai.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['NumOfRatings', 'ProductName', 'SellingPrice', 'Brand', 'Rating',
       'Combos', 'Mrp', 'Discount', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_masala-and-spices.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_masala-and-spices.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'NumOfRatings', 'SellingPrice', 'Mrp',
       'Discount', 'Brand', 'Rating', 'Combos', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_noodle-pasta-vermicelli.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_noodle-pasta-vermicelli.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'NumOfRatings', 'SellingPrice', 'Mrp', 'Brand',
       'QuantityDisplay', 'Combos', 'Discount', 'Rating']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_oral-care.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_oral-care.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'NumOfRatings', 'SellingPrice', 'Mrp', 'Combos',
       'Discount', 'Brand', 'Rating', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_organic-staples.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_organic-staples.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'SellingPrice', 'NumOfRatings', 'Mrp',
       'Discount', 'Rating', 'Brand', 'QuantityDisplay', 'Combos']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_pickles-chutney.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_pickles-chutney.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['NumOfRatings', 'ProductName', 'SellingPrice', 'Brand', 'Rating',
       'QuantityDisplay', 'Mrp', 'Discount', 'Combos']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_ready-to-cook-eat.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_ready-to-cook-eat.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'NumOfRatings', 'SellingPrice', 'Brand', 'Mrp',
       'Combos', 'Rating', 'Discount', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_rice-products.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_rice-products.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'SellingPrice', 'Mrp', 'NumOfRatings',
       'Discount', 'Brand', 'Rating', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_salt-sugar-jaggery.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_salt-sugar-jaggery.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['SellingPrice', 'ProductName', 'num-of_Ratings', 'Mrp',
       'Discount', 'Brand', 'Combos', 'Rating', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_snacks-namkeen.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_snacks-namkeen.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'NumOfRatings', 'SellingPrice', 'Combos', 'Brand',
       'Mrp', 'Discount', 'Rating', 'QuantityDisplay']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_spreads-sauces-ketchups.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_spreads-sauces-ketchups.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'NumOfRatings', 'SellingPrice', 'Brand', 'Mrp',
       'QuantityDisplay', 'Discount', 'Rating', 'Combos']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)



choc_path = r"D:\whatsapp-retailer-chatbot\data\interim\BB_tea-beverages.csv"
choc_export_path = r"D:\whatsapp-retailer-chatbot\data\processed\clean_tea-beverages.csv"

df_choc = pd.read_csv(choc_path)
df_choc.columns = ['ProductName', 'SellingPrice', 'NumOfRatings', 'Brand', 'Mrp',
       'Discount', 'Rating', 'QuantityDisplay', 'Combos']

df_choc = df_choc[df_choc['ProductName'].notna()]

for char in spec_chars:
    df_choc['ProductName'] = df_choc['ProductName'].str.replace(char, ' ')
    df_choc['Brand'] = df_choc['Brand'].str.replace(char, ' ')
    df_choc['Combos'] = df_choc['Combos'].str.replace(char, ' ')
    df_choc['QuantityDisplay'] = df_choc['QuantityDisplay'].str.replace(char, ' ')
    
df_choc.to_csv(choc_export_path, index=False, header=True)

print("Procesing DONE!")
