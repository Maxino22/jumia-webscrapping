import requests
from bs4 import BeautifulSoup
from csv import writer


url = 'https://www.jumia.co.ke/mlp-supermarket-week/groceries/?source=SX_GEN_CP'

response = requests.get(url)
# print(response)

soup = BeautifulSoup(response.text, 'html.parser')

products = soup.select('.prd ')

with open('jumia.csv', 'w', newline='') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Name', 'Price', 'Ratings']
    csv_writer.writerow(headers)

    for product in products:
        name = product.select_one('h3').get_text()
        price = product.select_one('.prc').get_text()
        reviews = product.select_one('.rev').get_text()
        csv_writer.writerow([name, price, reviews])
        print('Done')
