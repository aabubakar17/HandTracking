import unittest
from selenium import webdriver
import page

class pythonOrgSearchTest(unittest.TestCase):
    #the first method that will run
    #for each test case(Test_example) is run the setUp is run again
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")

    #method wont run if the name of the method does not start with test
    #def  test_example(self):
      # print("Test")
       #assert False # if the true then the test case has passed

    #def test_title(self):
        #mainPage = page.MainPage()
        #assert mainPage.is_title_matches() #test if the title matches

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    #method that runs at the end
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
  unittest.main()
