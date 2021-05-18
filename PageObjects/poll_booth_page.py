import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class Poll_botth_page:

    """constructor"""
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    """based on voted option, checks and returns the total number of people voted for the same option"""
    def people_with_same_vote(self, same_total_votes_elm):
        time.sleep(.5)
        same_total_votes = self.wait.until(EC.presence_of_element_located((By.XPATH,same_total_votes_elm)))
        ActionChains(self.driver).move_to_element(same_total_votes).perform()
        str_same_total_votes = same_total_votes.text
        num_of_people = str_same_total_votes.split()[0]
        return int(num_of_people)