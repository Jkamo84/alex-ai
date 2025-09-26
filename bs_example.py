import requests
from bs4 import BeautifulSoup

url = "https://frasesdelavida.com/frases-de-positivismo/"
response = requests.get(url)  # do a request to the site
print(response)
soup = BeautifulSoup(response.text, "html.parser")  # init a bs4 instance with the html
quotes: list[dict[str, str]] = []
# quote_boxes = soup.find_all(
#     "div", class_="col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top"
# )  # try ind find the elements that have the description given
quote_boxes = soup.find_all("strong")

print(type(quote_boxes))
for box in quote_boxes:
    text = box.text
    print(text)
    print("---" * 10)
