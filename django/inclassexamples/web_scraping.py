# process the HTML to extract the data we care about
# ... build a CSV file

import requests # HTTP requests
from bs4 import BeautifulSoup # HTML parsing

# start with the URL:
url = 'https://stores.brooksrunning.com/region/US/MA'

# download this webpage:
page = requests.get(url)
# page.text is the content of the web page
# tokenize the page into HTML tree
soup = BeautifulSoup(page.content, 'html.parser')

# this section is <div class='tiles wider'>
table = soup.find('div', attrs={'class': 'tiles wider'})
# print(table)

# break the larger div into smaller chunks, one for each 
rows = table.findAll('a')
# print(rows[0])

# go through all stores (rows)
for row in rows:
    # extract the name and address from <span> tags

    name = row.find('span', attrs={'class': 'name'})
    address = row.find('span', attrs={'class': 'address'})

    # print(name, address)
    # print(name.text.strip(), address.text.strip())

    # clean up 
    name = name.text.strip()
    address = address.text.strip().replace('\n', ',')
    print(name, address)


