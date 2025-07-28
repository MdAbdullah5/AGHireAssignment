import requests
from bs4 import BeautifulSoup
import re
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Setup headless Chrome
chrome_opts = Options()
chrome_opts.add_argument("--headless")
chrome_opts.add_argument("--disable-gpu")
chrome_opts.add_argument("--no-sandbox")
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_opts)

page_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
page_response = requests.get(page_url)

collected_items = []

soup_main = BeautifulSoup(page_response.text, 'html.parser')
product_cards = soup_main.find_all("div", class_="product-wrapper card-body")

for item in product_cards:

    link_tag = item.find("a")
    product_name = link_tag.text.strip() if link_tag else ""

    price_tag = item.find("h4")
    product_price = price_tag.text.strip() if price_tag else ""

    stars_container = item.find("div", class_="ratings")
    if stars_container:
        star_count = len(stars_container.find_all("span", class_="ws-icon-star"))
    else:
        star_count = 0

    review_tag = item.find("p", class_="review-count float-end")
    review_total = review_tag.text.strip() if review_tag else ""

    root_url = page_url.split("/")[0] + "//" + page_url.split("/")[2]
    anchor_tag = item.find("a")
    if anchor_tag and anchor_tag.get("href"):
        detail_url = root_url + anchor_tag["href"]
    else:
        detail_url = ""

    browser.get(detail_url)
    detail_soup = BeautifulSoup(browser.page_source, 'html.parser')

    desc_block = detail_soup.find("div", class_="product-wrapper card-body")
    if desc_block:
        raw_desc = desc_block.text.strip()
        formatted_desc = re.sub(r'\s+', ' ', raw_desc)
    else:
        formatted_desc = ""

    collected_items.append({
        "title": product_name,
        "price": product_price,
        "rating": star_count,
        "reviews_count": review_total,
        "product_url": detail_url,
        "description": formatted_desc
    })

with open("output.json", "w", encoding="utf-8") as output_file:
    json.dump(collected_items, output_file, ensure_ascii=False, indent=4)

browser.quit()
