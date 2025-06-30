import requests
import pandas as pd
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
}


request = requests.get("https://www.scrapethissite.com/pages/simple/", headers=header)

# soup = BeautifulSoup("Html file.html", "html.parser")
# with open("Html file.html", "w", encoding="utf-8") as file:
#     file.write(str(soup.prettify()))
with open("Html file.html","r", encoding="utf-8") as file:
    content = file.read()
soup = BeautifulSoup(content, "html.parser")

h3_with_i_tag = soup.find_all("h3")
# #################################################################
# for h3_tag in h3_with_i_tag:                                    #
#     i_text = h3_tag.i.text if h3_tag.i else ""                  #
#     h3 = h3_tag.i.get_text(strip=True).replace(i_text, "")      # 
# #################################################################
Name = [h3_tag.get_text(strip=True).replace(h3_tag.i.text if h3_tag.i else "", "") for h3_tag in h3_with_i_tag]

raw_capital = soup.find_all("span",attrs={"class": "country-capital"})
capital = [capita.get_text(strip=True) for capita in raw_capital]

raw_populataion = soup.find_all("span", attrs={"class":"country-population"})
population = [p.get_text(strip=True) for p in raw_populataion]

raw_area = soup.find_all("span", attrs={"class":"country-area"})
area = [a.get_text(strip=True) for a in raw_area]

df = pd.DataFrame({
    "Country name": Name,
    "Capital":capital,
    "Population":population,
    "Area":area
})

df.to_csv("C:/Users/user/Document/Country data/Country Data.csv",index=False)
print("Succusfull")