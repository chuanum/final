#################################
##### Name: Chuan He    
##### Uniqname: chuanum
#################################

from bs4 import BeautifulSoup
import requests
import json
import sys



class weatherinfo:
    '''weather details

    Instance Attributes
    -------------------
    temperaturevalue: string
        the temperature information
    
    wind: string
        the wind information

    humidity: string
        the humidity information

    precip: string
        the precip value information

    '''
    def __init__(self,temp,wind,humidity,precip):
        self.temp = temp
        self.wind = wind
        self.humidity = humidity
        self.precip = precip
        


def get_weather_news():
    ''' get a list of up to 5 latest news on weather

    Parameters
    ----------
    None

    Returns
    -------
    list of weather news
    '''
    url = 'https://weather.com/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    search = soup.find_all(class_ = 'Ellipsis--ellipsis--lfjoB')
    news_list = []
    i = 0
    while len(news_list) <= 5:
        news_list.append(search[i].text)
        i = i+1
    return news_list

def zipcode_get_today_weather(zipcode):
    '''Make an instances from a weather url
    
    Parameters
    ----------
    zipcode: string
        the zipcode from user input
    
    Returns
    -------
    instance
        a local weather instance
    '''
    url = 'https://weather.com/weather/today/l/' + str(zipcode)
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    temp = soup.find(class_ = 'TodayDetailsCard--feelsLikeTempValue--2aogo').text
    wind = soup.find(class_ = 'Wind--windWrapper--1Va1P undefined').text[14:]
    humidity = soup.find_all(class_ = 'WeatherDetailsListItem--wxData--23DP5')[2].text
    precip = soup.find(class_ = 'CurrentConditions--phraseValue--2xXSr').text
    obj = weatherinfo(temp,wind,humidity,precip)
    return obj

def get_hourly_weather(zipcode):
    '''Make a list from a weather url
    
    Parameters
    ----------
    zipcode: string
        the zipcode from user input
    
    Returns
    -------
    list
        hourly weather information
    '''
    url = 'https://weather.com/weather/hourly/l/' + str(zipcode)
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    time = soup.find_all(class_ = 'DetailsSummary--DetailsSummary--QpFD-')
    hw = []
    i = 0
    while len(hw) <= 5:
        hw.append(time[i].text)
        i = i+1
    return hw

def get_10days_weather(zipcode):
    '''Make a list from a weather url

Parameters
----------
zipcode: string
    the zipcode from user input

Returns
-------
list
    daily weather information
'''
    url = 'https://weather.com/weather/tenday/l/' + str(zipcode)
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    time = soup.find_all(class_ = 'DailyContent--DailyContent--rTQY_')
    hw = []
    i = 0
    while len(hw) <= 20:
        hw.append(time[i].text)
        i = i+1
    return hw

def get_weekend_weather(zipcode):
    '''Make a list from a weather url

Parameters
----------
zipcode: string
    the zipcode from user input

Returns
-------
list
    weekend weather information
'''
    url = 'https://weather.com/weather/weekend/l/' + str(zipcode)
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    time = soup.find(class_ = 'DailyContent--DailyContent--rTQY_')
    
    
    return time.text
    


news_request = input('Would you like to hear the latest news about weather? Enter 1 for yes, else for no, or exit：')
if news_request == '1':
    print('-'*20)
    print('Weather News!')
    print('-'*20)
    news_list = get_weather_news()
    for i in news_list:
        print(i)
    print('-'*20)
elif news_request == 'exit':
    sys.exit()

v = True

while v:
    v = False
    zc = input('Please enter a zipcode(e.g. 48105):, or else for exit: ')
    if zc.isnumeric and len(zc) == 5:
        today_obj = zipcode_get_today_weather(zc)
        print('-'*20)
        print('Today Weather!')
        print('-'*20)
        print('Temperature: ' + today_obj.temp)
        print('Wind: ' + today_obj.wind)
        print('Humidity: ' + today_obj.humidity)
        print('Precipitation: ' + today_obj.precip)
        print('-'*20)
    else:
        sys.exit()

    x = True
    while x:
        
        print('Do you need weather info for a different time period?')
        tp = input('1 for hourly, 2 for 10 days, 3 for weekend, back for another zipcode search, or else for exit: ')
        if tp == '1':
            print('-'*20)
            print('Hourly Weather!')
            print('-'*20)
            hw = get_hourly_weather(zc)
            for i in hw:
                print(i)
            print('-'*20)
        elif tp == '2':
            print('-'*20)
            print('10 Day Weather!')
            print('-'*20)
            hw = get_10days_weather(zc)
            for i in hw:
                print(i)
            print('-'*20)

        elif tp == '3':
            print('-'*20)
            print('Weekend Weather!')
            print('-'*20)
            hw = get_weekend_weather(zc)
            print(hw)
            print('-'*20)

        elif tp == 'back':
            x = False
            v = True

        else:
            sys.exit()

        

















