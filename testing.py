print("Login into your Linkedin Account")
print("********************************")
print()
email = input("Enter your email: ")
password = input("Enter your password: ")

print()
url_list = []
while True:
    url = input("Please insert the linkedin url: ")
    if url is None:
        print("Wrong input!")
    elif url=="q" or url=="Q":
        break
    else:
        url_list.append(url)
from scrapping import Scraping
sc = Scraping(email,password)
result = sc.store_all_information(url_list)
print(result)

