from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--window-size=1280x1696')
# chrome_options.add_argument('--user-data-dir=/tmp/user-data')
# chrome_options.add_argument('--hide-scrollbars')
# chrome_options.add_argument('--enable-logging')
# chrome_options.add_argument('--log-level=0')
# chrome_options.add_argument('--v=99')
# chrome_options.add_argument('--single-process')
# chrome_options.add_argument('--data-path=/tmp/data-path')
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--homedir=/tmp')
# chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
# chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
# chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

# driver = webdriver.Chrome(chrome_options=chrome_options)
url = {
    'google': 'https://www.google.com/search?q=ibex+35&lr=&cr=countryES&hl=es&tbs=ctr:countryES&source=lnms&tbm=nws',
    'bing': 'https://www.bing.com/news/search?q=ibex+35&cc=es',
    'yahoo': 'https://es.news.search.yahoo.com/search?p=ibex+35',
    'duck': 'https://duckduckgo.com/?q=ibex+35&t=h_&iar=news&ia=news&kl=es-es&df=d',
    'qwant' : 'https://www.qwant.com/?q=ibex+35&t=news&r=ES',
    'ibex': 'http://www.bolsamadrid.es/esp/aspx/Indices/Resumen.aspx'
    }


def lambda_handler(event, context):
    # TODO implement
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1280x1696')
    chrome_options.add_argument('--user-data-dir=/tmp/user-data')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--enable-logging')
    chrome_options.add_argument('--log-level=0')
    chrome_options.add_argument('--v=99')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--data-path=/tmp/data-path')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--homedir=/tmp')
    chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"

    wd = webdriver.Chrome(chrome_options=chrome_options)
    text = {'duck': duck(wd), 'qwant': qwant(wd)}
    wd.close()
    return text


def duck(wd):
  wd.get(url['duck'])
  text = [t.text for t in wd.find_elements_by_xpath("//div[@class='results js-vertical-results']/div/div/h2/a")]
  text = list(filter(None, text))
  text = '. '.join(text)
  return text

def qwant(wd):
  wd.get(url['qwant'])
  text = [t.text for t in wd.find_elements_by_xpath("//div[@class='result-type__news__item']/div[@class='result-type__news__text--container']/a")]
  text = ' '.join(text)
  return text