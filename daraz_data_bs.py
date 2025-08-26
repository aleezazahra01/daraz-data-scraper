from bs4 import BeautifulSoup as bs
import pandas as pd
import csv

with open('darazdata.csv',mode='w',encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(["titles",'price','no of mobiles sold','ratings','locations'])

    for page in range(1,6):
        with open(f'daraz_data/phones_page{page}.html',mode='r',encoding='utf-8') as file:
            html_doc=file.read()
            soup=bs(html_doc,'html.parser')
            products = soup.find_all('div', class_='Bm3ON')
            print(f"Page {page}: Found {len(products)} products")


            
            for product in products:
                #finding the titles
                a_tag = product.find('div', class_='RfADt').find('a')
                t=a_tag.get('title')
                # title=t.text.strip() if t else 'N/A'

                #finding the prices
                #<div class="aBrP0"
                p = product.find_next('div', class_='aBrP0')
                price_tag = p.find('span', class_='ooOxS') if p else None
                price = price_tag.text.strip() if price_tag else 'N/A'

                #sold items
                # <div class="_6uN7R"><span class="_1cEkb"><span>1.2K sold</span><span
                s=product.find_next('div',class_='_6uN7R')
                s_tag=s.find('span',class_="_1cEkb") if s else None
                sold_items=s_tag.text.strip() if s_tag else 'nothing sold'

                #no of stars rated
                #<div class="mdmmT _32vUv"><i class="_9-ogB Dy1nx"></i><i class="_9-ogB Dy1nx"></i><i
                            #   class="_9-ogB Dy1nx"></i><i class="_9-ogB Dy1nx"></i><i class="_9-ogB i6t3-"></i><span
            
# Count how many i tags have class "Dy1nx" (which seems to mean filled stars)
                # rating_div = product.find('div', class_='"mdmmT _32vUv"')

                rating_div = product.find('div', class_='mdmmT')
                stars = 0
                if rating_div:
                    stars = len(rating_div.find_all('i', class_='Dy1nx'))


             #location of the product
             #class="qzqFw">(17)</span></div><span class="oa6ri " title="Sindh">Sindh</span>
                # l=product.find('div',class_="qzqFw")
                # l_tag=l.find_all('span',class_="oa6ri")if l else None
                # location=l_tag.text.strip()if l_tag else 'N/A'
                #  class="qzqFw">(264)</span></div><span class="oa6ri " title="Sindh">Sindh</span>
                loc_tag = product.find('span', class_='oa6ri')
                location=loc_tag.get('title')
                # location = loc_tag.text.strip() if loc_tag else 'N/A'

                writer.writerow([t,price,sold_items,stars,location])

df=pd.read_csv('darazdata.csv')
df.fillna(0)
df.to_excel('darazdata.xlsx')





        