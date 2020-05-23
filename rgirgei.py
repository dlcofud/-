from selenium import webdriver
import time

article_list = []

def article_Scraping():
    driver = webdriver.Chrome('./chromedriver')
    for i in range(1, 5):
        driver.get('https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=105#&date=%%2000:00:00&page=%d'%i)
        time.sleep(1)
        articles = driver.find_elements_by_css_selector('div.section_body > ul > li > dl > dt > a')
        for article in articles:
            if len(article.text) != 0:
                article_list.append(article.text)
    driver.quit()
    for article in article_list:
        print(article)


article_Scraping()
