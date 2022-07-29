from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from base.utils import Utils


class HomepageNav(SeleniumBase, Utils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        """ nav_links - public attribute (публичное свойство) """
        """ _nav_links - protected attribute (служит для обращения внутри класса и во всех его дочерних классах) """
        """ __nav_links - private attribute (служит для обращения только внутри класса) """
        self.__nav_links: str = '#mainNavigationFobs > li'
        self.NAV_LINKS_TEXT = 'Women,Men,Beauty,Home,Furniture,Shoes,Handbags,Jewelry,Kids,Toys,Gifts,Own Your Style,Sale'

    def get_nav_links(self, message='Header Navigation Links') -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, message)

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_web_elements(nav_links)
        return self.join_strings(nav_links_text)

    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)
