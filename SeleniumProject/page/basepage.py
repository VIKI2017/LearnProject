from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import yaml


with open("../data/config.yml") as f:
    data = yaml.safe_load(f)
    baseurl = data['data']['URL']
    user = data['data']['user']
    code = data['data']['code']



class BasePage(object):

    def __init__(self,driver:WebDriver=None):
        self.driver = driver
        # self.driver = webdriver.Chrome()
        # self.driver.get(baseurl)
        # self.driver.maximize_window()
        self.timeout = 30
        # self.driver.implicitly_wait(5)
        # self.driver.implicitly_wait(self,5)



    #重写元素定位方法
    def find_element(self, *loc):
        driver = self.driver
        try:
            WebDriverWait(driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # ele = self.driver.find_element(*loc)
            ele = driver.find_element(*loc)
            return ele
        except:
            print ('Can Not Find The Element %s In Page' % loc[1])
            raise



    def is_element_exists(self, *loc):
        '''
        在15秒内判断元素是否存在
        :param loc: 定位方式
        :return:
        '''
        ele = False
        if self.driver.find_element(*loc) is not None:
            ele = True
            return ele
        else:
            return ele

    # 重写元素定位方法
    def find_elements(self, *loc):
        eles = self.driver.find_elements(*loc)

        try:
            if len(eles):
                # length = len(self.driver.find_elements(*loc))
                # ele = self.driver.find_elements(*loc)
                return eles
        except:
            print ('Can Not Find The Element %s In Page' % loc[1])
            raise