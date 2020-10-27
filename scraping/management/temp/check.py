import mechanize
from bs4 import BeautifulSoup
from urllib import request
from http.cookiejar import CookieJar
import xlsxwriter
import random



def randomSoGio():
    return random.choice([30, 45, 54])

def randomHeSo():
    return random.choice([0.75, 1.0, 1.2, 1.5, 1.6, 1.7])



URL = 'https://dangkyhoc.thanglong.edu.vn/'


print('Login before craw :)')
print('\tEnter your username:')
username = input()
print('\tEnter your password:')
password = input()

cj = CookieJar()
browser = mechanize.Browser()
browser.set_cookiejar(cj)
browser.set_handle_robots(False)
browser.open(URL)

browser.select_form(nr = 0)
browser.form['tbUserName'] = username
browser.form['tbPassword'] = password
browser.submit()


html = browser.open('https://dangkyhoc.thanglong.edu.vn/ToanTruong/ChuongTrinhDaoTao.aspx')    
soup = BeautifulSoup(html,'html.parser')

bangmonhoc = soup.find('table', {"class": "tablesv"})
#print(bangmonhoc)
bangmonhoc = bangmonhoc.findChildren('tr')

# Workbook() takes one, non-optional, argument  
# which is the filename that we want to create. 
workbook = xlsxwriter.Workbook('MONHOC.xlsx') 
worksheet = workbook.add_worksheet()

# Start from the first cell. 
# Rows and columns are zero indexed. 
row = 0
column = 0

worksheet.write(row, 0, 'Ma mon')
worksheet.write(row, 1, 'Ten mon')
worksheet.write(row, 2, 'So tin chi')
worksheet.write(row, 3, 'Hoc phan tien quyet')
worksheet.write(row, 4, 'So gio')
worksheet.write(row, 5, 'He so')


row += 1

for monhoc in bangmonhoc:
    monhoc = monhoc.findChildren('td')
    
    print('Ma mon: ', monhoc[1].text)
    print('Ten mon: ', monhoc[2].text)
    print('Hoc phan tien quyet: ', monhoc[3].text)
    #print('Tinh chi tien quyet: ', monhoc[4].text)
    print('So tin chi: ', monhoc[5].text)

    worksheet.write(row, 0,  monhoc[1].text)
    worksheet.write(row, 1,  monhoc[2].text)
    worksheet.write(row, 2,  monhoc[5].text)
    worksheet.write(row, 3,  monhoc[3].text)
    worksheet.write(row, 4, randomSoGio())
    worksheet.write(row, 5, randomHeSo())
    row += 1

    print('---------')
    
workbook.close()

print('Crawl is done.')


