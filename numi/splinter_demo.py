from splinter import Browser


def fill_form(query='cute panda'):
    
    b = Browser()
    # Visit URL
    url = "http://websta.me/search"
    browser.visit(url)
    browser.fill('q', query)
    # Find and click the 'search' button
    button = browser.find_by_tag('button')
    # Interact with elements
    button.first.click()
    if browser.is_text_present('cutepanda'):
        return browser.html
    else:
        return False

resp = fill_form()
print(resp)
