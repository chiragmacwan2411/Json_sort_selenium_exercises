import time
from random import randrange
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Home_Page:

    """Constructor"""
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    """navigates to the app page"""
    def go_to_home_page(self, home_page_url):
        self.driver.get(home_page_url)
        print("Navigating to base-page")

    """find out and prints total articles"""
    def total_articles(self, articles_elms):
        counter  = 0
        articles =  self.driver.find_elements(By.CSS_SELECTOR,articles_elms)
        for article in articles:
            counter += 1
        print("Total Articles : " + str(counter)  + "\n")


    """prints a list of total unique icons, tracks and displays number of articles in each icon"""
    def article_stat(self, icon_title_elm):
        categories = []
        num_of_article = []
        image_titles = self.driver.find_elements(By.XPATH, icon_title_elm)

        for image_title in image_titles:
            article_title = image_title.get_attribute("title")

            if article_title not in categories:
                categories.append(article_title)
                num_of_article.append(0)

            if article_title in categories:
                index = categories.index(article_title)
                num_of_article[index] += 1


        # for image_title in image_titles:
        #
        #     article_title = image_title.get_attribute("title")
        #
        #     if article_title not in categories:
        #         categories.append(article_title)
        #         num_of_article.append(0)
        #
        # for image_title in image_titles:
        #     article_title = image_title.get_attribute("title")
        #
        #     if article_title in categories:
        #         index = categories.index(article_title)
        #         num_of_article[index] += 1

        result_dict = dict(zip(categories, num_of_article))

        print("----->ARTICLE STAT<-----")
        print(categories)
        for k, v in result_dict.items():
            print(k + " ::: " + str(v))

    """considers all voting options, clicks on one random options and submits the vote"""
    def voting(self, poll_content_elms, vote_options_elms, vote_click_btn_elm):
        time.sleep(3)
        poll_content = self.wait.until(EC.presence_of_element_located((By.XPATH, poll_content_elms)))
        ActionChains(self.driver).move_to_element(poll_content).perform()

        vote_options = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, vote_options_elms)))
        num_of_vote_options = len(vote_options)
        index_to_be_clicked = randrange(num_of_vote_options) - 1
        time.sleep(1)
        elm_to_be_clicked = vote_options[index_to_be_clicked]
        chosen_option = elm_to_be_clicked.text
        elm_to_be_clicked.click()
        self.driver.find_element(By.XPATH, vote_click_btn_elm).click()
        return chosen_option