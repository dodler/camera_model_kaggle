import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

driver = webdriver.Firefox(firefox_profile=firefox_profile)

driver.get("https://www.flickr.com/search/?camera=motorola%2Fnexus_6&dimension_search_mode=min&height=3120&width=3120")

images_to_collect = 500

elm_len = 0

while elm_len < images_to_collect:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    photos_class = "overlay"

    elms = driver.find_elements_by_class_name(photos_class)
    print(len(elms))
    elm_len = len(elms)

    try:
        text = 'Load more results'
        btn = driver.find_element_by_class_name('infinite-scroll-load-more').\
            find_element_by_tag_name('button')
        btn.click()
    except NoSuchElementException as e:
        print(e)

    time.sleep(1)

hrefs = list(map(lambda e:e.get_attribute('href'), elms))

with open('hrefs_output.txt','w') as f:
    for h in hrefs:
        f.write(h + '\n')

driver.quit()
