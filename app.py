import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "URL": 'https://www.google.com/shopping/product/1?q=flipkart+online+shopping&prds=epd:13816245782252656050,eto:13816245782252656050_0,pid:13816245782252656050&sa=X&ved=0ahUKEwii6riJnpH5AhVjELcAHTwkBxgQ9pwGCAg',
        "name": 'Book_shelf01',
        "target_price": 1300

    },
    {
        "URL": 'https://www.google.com/shopping/product/6614832381559311889?q=flipkart+online+shopping&prds=epd:15226479989657431441,oid:15226479989657431441,pid:3700658128289522842&sa=X&ved=0ahUKEwiShuTovJv5AhWv4TgGHXWfAfkQrRIINQ',
        "name": 'Book_shelf02',
        "target_price": 5000

    },
    {
        "URL": 'https://www.google.com/shopping/product/4897000188228444946?q=flipkart+online+shopping&prds=epd:14052619261719418112,oid:14052619261719418112,pid:13335905704525642419&sa=X&ved=0ahUKEwi8lpXvvJv5AhVnxzgGHQOhCtgQrRIINg',
        "name": 'Hayao_bookshelf',
        "target_price": 6500

    },
    {
        "URL": 'https://www.google.com/shopping/product/3971812451964090451?q=flipkart+online+shopping&prds=epd:17240968004082341198,oid:17240968004082341198,pid:14273111879780854647&sa=X&ved=0ahUKEwi8lpXvvJv5AhVnxzgGHQOhCtgQrRIIMw',
        "name": 'Modern_bookshelf',
        "target_price": 5750

    },
    {
        "URL": 'https://www.flipkart.com/flipkart-smartbuy-storm-powerchef-500-w-mixer-grinder-3-jars-grey-black/p/itma034b2a6b8e6e?pid=MIXFTBYHPFZESGV6&lid=LSTMIXFTBYHPFZESGV6LMVD9U&marketplace=FLIPKART&cmpid=content_mixer-grinder-juicer_12341866279_g_8965229628_gmc_pla&tgi=sem,1,G,11214002,g,search,,498550853752,,,,c,,,,,,,&ef_id=Cj0KCQjw54iXBhCXARIsADWpsG8jyKISCvVBveYWfINJ_EWQy1vHr4lHFUXBqpymJWCKod0VN8zo5_MaApzVEALw_wcB:G:s&s_kwcid=AL!739!3!498550853752!!!g!309904561172!&gclid=Cj0KCQjw54iXBhCXARIsADWpsG8jyKISCvVBveYWfINJ_EWQy1vHr4lHFUXBqpymJWCKod0VN8zo5_MaApzVEALw_wcB',
        "name": 'Mixergrinder',
        "target_price": 1200

    }

]


def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    product_price = soup.find("span", {"class": "g9WBQb"})

    if (product_price == None):
        product_price = soup.find("div", {"class": "_30jeq3 _16Jk6d"})

    return product_price.getText()


result_file =  open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("URL"))
        print(product_price_returned + "-" + every_product.get("name"))

        my_product_price = product_price_returned[1:]
        my_product_price = my_product_price.replace(',','')
        my_product_price = int(float(my_product_price))

        print(my_product_price)
        result_file.write(every_product.get("name") + ' - \t ' + 'available at your price' + 'current_price - ' + 'target_price' + str(my_product_price) + '\n')

    if my_product_price <= every_product.get("target_price"):
        print("available at your price")



    else:
        print("still at current price")



finally:
    result_file.close()





