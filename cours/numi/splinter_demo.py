from splinter import Browser
#definition de la fonction def func(var):

def fill_form(query='cute panda'):
    #la tabulation permet de definir le périmêtre de la fonction
    
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

#appel de la fonction
resp = fill_form()
print(resp)
