# AGHireAssignment

# 🧠 Laptop Product Scraper

A Python web scraper that extracts structured product data (like titles, prices, ratings, reviews, and full descriptions) from a sample e-commerce website.  
This project uses **Selenium (headless)** and **BeautifulSoup** to simulate a browser and navigate product detail pages.

---

## 🌐 Target Website

**URL:** [https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops](https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops)

This is a demo site provided by WebScraper.io for practicing scraping techniques. All laptops are on a single page — no pagination is required.

---

## ✨ Features

- 🔍 Scrapes laptop product listings
- 🔗 Visits each product detail page to extract full description
- 📊 Captures:
  - Title
  - Price
  - Rating (star count)
  - Reviews count
  - Product URL
  - Description
- 🧠 Runs with **headless Chrome**
- 💾 Outputs structured data to `output.json`

---

## 🖥️ Technologies Used

| Tool              | Purpose                        |
|------------------|--------------------------------|
| Python 3.x        | Main programming language       |
| Selenium          | Browser automation (headless)   |
| BeautifulSoup     | HTML parsing                    |
| Requests          | Initial page fetching           |
| WebDriver Manager | ChromeDriver installation       |

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MdAbdullah5/AGHireAssignment
cd AGHireAssignment
