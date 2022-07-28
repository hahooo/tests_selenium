import time
import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINKS_TEXT
        assert expected_links == actual_links, 'Validating Nav Links Text'
        # homepage_nav.get_nav_link_by_name('Beauty').click()
        # time.sleep(5)
        for index in range(12):
            print('index', index)
            homepage_nav.get_nav_links()[index].click()
            homepage_nav.driver.delete_all_cookies()
            time.sleep(3)
