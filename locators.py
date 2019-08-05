from selenium.webdriver.common.by import By
import time

class WikipediaHomepage(object):
	Random_Link = (By.CSS_SELECTOR, '#n-randompage')

class WikipediaArticle(object):
	First_Heading = (By.CSS_SELECTOR, '.firstHeading')
	Page_Info = (By.LINK_TEXT, 'Page information')
	Search_Box = (By.NAME, 'search')
	Logo = (By.XPATH, '/html/body/div[5]/div[2]/div[1]/a')