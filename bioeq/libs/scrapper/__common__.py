import mechanize

def download(url, file):
    httpreq = mechanize.Request(url)

    browser = mechanize.Browser()
    browser.set_handle_robots(False)

    browser.open(httpreq)

    httpres = browser.response()
    
    # file = open(filename, 'w+')
    file.write(httpres.read())
    file.close()