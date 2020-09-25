import mechanize
from bs4 import BeautifulSoup
from urllib import request
from http.cookiejar import CookieJar

from scraping.models import Semester

class Login() :
    
    def __init__(self):

        self.URL = 'https://dangkyhoc.thanglong.edu.vn/'
        self.username = ''
        self.password = ''

        self.cookie = CookieJar()
        self.browser = mechanize.Browser()

    def startLogin(self, username = 'a32007', password='sprite1299@@'):
        self.browser.set_cookiejar(self.cookie)
        self.browser.open(self.URL)

        self.browser.select_form(nr = 0)
        self.browser.form['tbUserName'] = username
        self.browser.form['tbPassword'] = password
        self.browser.submit()
        print("Login success ...")

    def getSchedule(self):
        html = self.browser.open('https://dangkyhoc.thanglong.edu.vn/SinhVien/ThoiKhoaBieuSinhVien.aspx')    
        soup = BeautifulSoup(html,'html.parser')
        return soup


    def __str__(self):
        return (str(self.browser.response().read()))