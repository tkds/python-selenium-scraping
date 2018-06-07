# coding: UTF-8
from selenium import webdriver

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'

dcap = {
    "phantomjs.page.settings.userAgent": USER_AGENT,
    'marionette': True
}

MAIL = "hoge@example.com"
PASS = "Passw0rd!"

browser = webdriver.PhantomJS(desired_capabilities=dcap)
browser.implicitly_wait(3)

url_login = "https://www.example.com/"
browser.get(url_login)
print("access page")

browser.implicitly_wait(2)
browser.save_screenshot("topPage.png")

login = browser.find_element_by_xpath("/html/body/header[1]/p[1]/")
login.click()
browser.save_screenshot("loginPage.png")

e = browser.find_element_by_id("mail")
e.clear()
e.send_keys(MAIL)
e = browser.find_element_by_id("ipassword")
e.clear()
e.send_keys(PASS)

frm = browser.find_element_by_css_selector(".login-form form")
frm.submit()
print("submit")

browser.save_screenshot("secretPage.png")

for x in range(1, 100):
    browser.implicitly_wait(2)
    url = "https://example.com/" + str(x) + "/content/"
    browser.get(url)
    page_source = browser.page_source
    outhtml = "/Users/you/get/" + str(x) + ".html"
    with open(outhtml, "w") as f:
        f.write(browser.page_source)

browser.quit()
