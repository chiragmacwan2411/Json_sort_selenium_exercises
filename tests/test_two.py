from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from utilities import selenium_helper
from PageObjects import home_page, poll_booth_page

"""This class gets and executes tests from the different pages in the page-object-model"""
class selenium_test():
    driver = webdriver.Chrome(executable_path="seleniumDriver/chromedriver")
    wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
                                                                           ElementNotVisibleException,
                                                                           ElementNotSelectableException])
    """instances of po classes and helper class"""
    sh = selenium_helper.Selenium_Helper(driver)
    HomePage = home_page.Home_Page(driver, wait)
    Poll_booth_page = poll_booth_page.Poll_botth_page(driver, wait)

    """LIST OF ELEMENT LOCATORS"""
    """Home Page locators"""
    _total_articles = ".article[data-fhtype='story']"
    _icon_title = "//span[@class='topic']//img"
    _poll_content_elms = "//section[@id='poll-content']"
    _vote_options_elms = "//form[@id='pollBooth']//label"
    _vote_click_btn = "//button[contains(text(),'vote now')]"

    """poll booth page locators"""
    _same_total_votes ="//div[@class='poll-bar-group']//div[contains(text(),'{0}')]//parent::div[@class='poll-bar-group']//div[contains(text(),'votes')]" #getting edited at execution to accommodate the value of chosen option

    def test_selenium(self):
        self.sh.initiate_driver()

        """req 1 : browse to base page"""
        try:
            self.HomePage.go_to_home_page("https://slashdot.org/")
        except TimeoutException:
            print("Page load exception occurred")


        """req 2 : print how many articles are there on the page"""
        self.HomePage.total_articles(self._total_articles)


        """req 3 : Print a list of unique (different) icons used on article titles and how many times was it used"""
        self.HomePage.article_stat(self._icon_title)


        """req 4 : Vote for some random option on the daily poll"""
        voting  = self.HomePage.voting(self._poll_content_elms, self._vote_options_elms, self._vote_click_btn)
        print("Option voted for : " + voting)


        """req 5 : Return the number of people that have voted for that same option"""
        # need to use dynamic xpath to get number of total votes for chosen option
        dynamic_same_total_votes_locator = self._same_total_votes.format(voting[:3])

        """'same_option_people' returns number of people voted for the same option as 'voting'"""
        print("Number of people voted for same option : " + str(self.Poll_booth_page.people_with_same_vote(dynamic_same_total_votes_locator)))

        self.sh.finsh_tests()