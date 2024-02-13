from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import random

driver = webdriver.Chrome()
post_urls = []
chat_url = input("Enter the chat url which posts going to send: ")

def send_message_to_chat_group():
    global post_urls
    global chat_url
    driver.get(chat_url)
    time.sleep(5)
    # get text area
    message_input = driver.find_element("xpath", "//div[@aria-label='Message']")
    for url in post_urls:
        message_input.send_keys(url)
        message_input.send_keys(Keys.RETURN)
        time.sleep(random.randint(5, 10)) 
        message_input.clear()
        time.sleep(random.randint(5, 10))

    post_urls = [] # clear the sent urls.

# instagram explore url
explore_url = 'https://www.instagram.com/explore/'

# get web page
driver.get(explore_url)

# wait until entered
input("Enter the account then enter to continue...")

while True:
    driver.get(explore_url)
    time.sleep(5)

    # get source
    explore_html = driver.page_source

    # use beautifulsoup to analyze webpage 
    soup = BeautifulSoup(explore_html, 'html.parser')
    # get all the posts from your explore
    post_links = [link['href'] for link in soup.find_all('a', href=True) if '/p/' in link['href']]

    post_urls = ["https://instagram.com" + link for link in post_links]

    print("The posts which going to send: ", post_urls)
    send_message_to_chat_group()