# import required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#
# instance of Microsoft Edge WebDriver is created with driver path
driver = webdriver.Edge(executable_path="D:\eheMachine\Workspace\codingLab\experimental\selenium-test\edgedriver_win64\msedgedriver.exe")
#
# The driver.get method will navigate to a page given by the URL.
# (Be aware that if your page uses a lot of AJAX on load then WebDriver may not know when it has completely loaded!)
driver.get("http://www.python.org")
#
# The next line is an assertion to confirm that title has “Python” word in it:
assert "Python" in driver.title
#
# the input text element can be located by its name attribute using find_element_by_name method. 
elem = driver.find_element_by_name("q")
#
# Next, we are sending keys, this is similar to entering keys using your keyboard. 
# Special keys can be sent using Keys class imported from selenium.webdriver.common.keys.
# To be safe, we’ll first clear any pre-populated text in the input field (e.g. “Search”) so it doesn’t affect our search results:
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
#
# To ensure that some results are found, make an assertion:
assert "No results found." not in driver.page_source
#
# Finally, the browser window is closed. 
# You can also call quit method instead of close. 
# The quit will exit entire browser whereas close will close one tab, 
driver.close()