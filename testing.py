print("Login into your Linkedin Account")
print("********************************")
print()
email = input("Enter your email: ")
password = input("Enter your password: ")
print()

##Getting a list of urls
url_list = []
while True:
    url = input("Please insert the linkedin url: ")

    ## if input is none, will want input again
    if url is None:
        print("Wrong input!")

    ##the url input will stop if 'q' or 'Q' is passed
    elif url=="q" or url=="Q":          
        break
    else:
        url_list.append(url)

## import Scraping class
from scrapping import Scraping

##object of Class
sc = Scraping(email,password)

## Getting all information in json format
result = sc.store_all_information(url_list)

## Printing the json result
print(result)

