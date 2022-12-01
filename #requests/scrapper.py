import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Statue-Legend-Adventure-Higashikata-Jyousuke/dp/B00AB74XIM/ref=sr_1_2?keywords=jojo%27s+bizarre+adventure+part+8&qid=1563620883&s=books&sr=1-2-catcorr' # amazon link

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'} # google my user agent and paste

condition = False

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    # title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:])

    if(converted_price < 1700):
        send_mail()

    print(converted_price)
    # print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('jaroslawgyro4@gmail.com','password-goes-here') #user, password

    subject = 'Price fell down!'
    body = ('Check the amazon link: ' + URL)

    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'jaroslawgyro4@gmail.com',
        'hrozmarynowski776@gmail.com',
        msg
    )
    
    global condition
    condition = True
    
    print('HEY EMAIL HAS BEEN SEND!')
    server.quit()

if (condition == False):
    check_price()
    time.sleep(10) # not too frequent, two or once a day it's fine