import pandas as pd
from bs4 import BeautifulSoup as bs
import os 
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    url = "https://redplanetscience.com"

    with browser as browser:
        browser.visit(url)
        mars_html = browser.html
        mars_soup = bs(mars_html, 'html.parser')
    
    news = mars_soup.find("div",id = 'news')
    title_text = news.find_all("div", class_ = 'content_title')[0].text
    article_text = news.find_all("div", class_ = 'article_teaser_body')[0].text

    url = "https://spaceimages-mars.com/"

    browser = Browser('chrome', **executable_path, headless=True)
    with browser as browser:
        browser.visit(url)
        space_images_html = browser.html
        space_images_soup = bs(space_images_html, 'html.parser')
        
    featured_image_url = "https://" + space_images_soup.find("img", class_ = "fancybox-image")['src']
    

    url = "https://galaxyfacts-mars.com/"
    mars_facts = pd.read_html(url)

    mars_comparison = mars_facts[0]
    mars_facts_table = mars_facts[1]

    mars_comparison.columns = mars_comparison.iloc[0,:]
    mars_comparison.set_index('Mars - Earth Comparison', inplace = True)
    mars_comparison = mars_comparison.iloc[1:]

    mars_facts_table.columns = ['Fact','Info']
    mars_facts_table.set_index('Fact', inplace = True)

    mars_facts_table_html = mars_facts_table.to_html()

    hemisphere_image_urls = [
        {"title":"Cerberus Hemisphere","img_url":"https://marshemispheres.com/images/full.jpg"},
        {"title":"Schiaparelli Hemisphere","img_url":"https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
        {"title":"Syrtis Major Hemisphere","img_url":"https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
        {"title":"Valles Marineris Hemisphere","img_url":"https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"} 
    ]

    return_dict = dict()

    return_dict['Red Planet News'] = {"title":title_text, "body":article_text}
    return_dict['Featured Image'] = featured_image_url
    return_dict['Mars Facts'] = mars_facts_table_html
    return_dict['Hemisphere Images'] = hemisphere_image_urls

    return return_dict