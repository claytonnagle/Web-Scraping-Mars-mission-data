# web-scraping-challenge
A web scraping and rehosting project using the dummy website redplanetscience.com

## Process and Methods
* First, using the splinter browser package, the python code visits the aforementioned website and collects the HTML on the page. 
* Then, the HTML is parsed through using BeautifulSoup to find key components required for the assignment. 
* After finding the relevant components, information is stored in dictionaries and returned
* Returned information is then passed to a localized MongoDB instance which is connected to via PyMongo
* Variables are accessible in the attached HTML via template variables, which allows for the display of information scraped from the website
* A JS button allows for theoretical data refresh, although the website doesn't actually refresh as it's a dummy website for the purpose of this exercise and class
