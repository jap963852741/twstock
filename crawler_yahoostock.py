import requests
import http.cookiejar as cookielib
from bs4 import BeautifulSoup

mafengwoSession = requests.session()
mafengwoSession.cookies = cookielib.LWPCookieJar(filename="mafengwoCookies.txt")

header = {

    'Upgrade-Insecure-Requests': '1'
    ,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Mobile Safari/537.36'
}

def get_The_Net_Asset_Value(stock_code):
    resp = mafengwoSession.get("https://tw.stock.yahoo.com/d/s/company_"+stock_code+".html", headers=header,
                               allow_redirects=False)
    Soup = BeautifulSoup(f"text = {resp.text}", 'lxml')
    for idx, tr in enumerate(Soup.find_all('tr')):
        # if idx != 0 :
            tds = tr.find_all('td')
            for i in tds :
                if '每股淨值' in i.contents[0] :
                    return i.contents[0]
    # print(comment)

def get_Establishment_time(stock_code):
    resp = mafengwoSession.get("https://tw.stock.yahoo.com/d/s/company_"+stock_code+".html", headers=header,
                               allow_redirects=False)
    Soup = BeautifulSoup(f"text = {resp.text}", 'lxml')
    next = [0]
    for idx, tr in enumerate(Soup.find_all('tr')):
            tds = tr.find_all('td')
            for i in tds :
                if max(next) == 1 :
                    return stock_code+";"+i.contents[0]
                if '上市(櫃)時間' in i.contents[0] :
                    next.append(1)


def get_EPS(stock_code):
    resp = mafengwoSession.get("https://histock.tw/stock/financial.aspx?no="+stock_code+"&st=2", headers=header,
                               allow_redirects=False)
    Soup = BeautifulSoup(f"text = {resp.text}", 'lxml')
    eps = ""
    for idx, tr in enumerate(Soup.find_all('tr')):
        if idx == 5 : #年eps和
            tds = tr.find_all('td')
            for i in tds:
                # eps.append(i.contents[0])
                eps+=i.contents[0]+','
    return eps


def get_Debt_Asset_ratio(stock_code):
    resp = mafengwoSession.get("https://histock.tw/stock/financial.aspx?no="+stock_code+"&t=4", headers=header,
                               allow_redirects=False)
    Soup = BeautifulSoup(f"text = {resp.text}", 'lxml')
    for idx, tr in enumerate(Soup.find_all('tr')):
        if idx == 1:
            tds = tr.find_all('td')
            return stock_code+','+tds[0].contents[0]+","+tds[1].contents[0]





def get_ROE(stock_code):
    resp = mafengwoSession.get("https://histock.tw/stock/financial.aspx?no="+stock_code+"&t=3&st=2", headers=header,
                               allow_redirects=False)
    Soup = BeautifulSoup(f"text = {resp.text}", 'lxml')
    ROE = stock_code
    # ROA =[]
    for idx, tr in enumerate(Soup.find_all('tr')):
        tds = tr.find_all('td')
        try:
            ROE = ROE +','+ tds[1].contents[0]
            # print(tds[1].contents[0])
        except:
            pass
    return ROE


# 現金股利發放率
def get_Dividend_Payout_Ratio(stock_code):
    resp = mafengwoSession.get("https://histock.tw/stock/financial.aspx?no="+stock_code+"&t=3&st=9", headers=header,
                               allow_redirects=False)
    Soup = BeautifulSoup(f"text = {resp.text}", 'lxml')
    ROE = stock_code
    # ROA =[]
    for idx, tr in enumerate(Soup.find_all('tr')):
        tds = tr.find_all('td')
        try:
            ROE = ROE +','+ tds[1].contents[0]
            # print(tds[1].contents[0])
        except:
            pass
    # print(ROE)
    return ROE



def get_Tradin_volume(stock_code):
    resp = mafengwoSession.get("https://www.cnyes.com/twstock/ps_historyprice/"+stock_code+'.html', headers=header,
                               allow_redirects=False)
    Soup = BeautifulSoup(f"text = {resp.text}", 'lxml')
    volume = stock_code
    for idx, tr in enumerate(Soup.find_all('tr')):
        tds = tr.find_all('td')
        # print(tds[7].contents[0])
        try:
            volume = volume +';'+ tds[7].contents[0]
            # print(tds[7].contents[0])
        except:
            pass
    # print(ROE)
    return volume

def get_Now_Tradin_volume(stock_code):
    resp = mafengwoSession.get("https://m.cnyes.com/twstock/profile.aspx?code="+stock_code, headers=header,
                               allow_redirects=False)
    Soup = BeautifulSoup(f"text = {resp.text}", 'lxml')
    for idx, tr in enumerate(Soup.find_all('tr')):
        tds = tr.find_all('td')
        try:
            if idx == 7:
                return  stock_code+';'+tds[0].contents[0]
        except:
            pass
    # print(ROE)


if __name__=='__main__':
    a = get_Now_Tradin_volume('1101')

    # print(a)