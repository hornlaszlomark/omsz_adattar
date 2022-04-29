# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 20:01:38 2022

@author: Laci
"""

import requests
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime


class Adattar():
    
    base_url = 'https://odp.met.hu/weather/weather_reports/synoptic/hungary/'
    
    @property
    def hourly(self):
        return self.base_url + 'hourly/csv/'
    
    @property
    def minutes10(self):
        return self.base_url + '10_minutes/csv/'
    
    @property
    def gas_daily(self):
        return self.base_url + 'gas_daily/csv/'
    @property
    def average_daily(self):
        return self.base_url + 'avg_daily/csv/'
    @property
    def daily(self):
        return self.base_url + 'daily/csv/'
    
    @property
    def daily_rain(self):
        return self.base_url + 'daily_rain/csv/'
    
    @property
    def monthly(self):
        return self.base_url + 'monthly/csv/'
    
    @property
    def meta(self):
        return self.base_url + 'meta/'

    
    def read_contents(self):
        page = requests.get(self.hourly)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup
    
    def get_filenames(self):
        search_all_links = self.read_contents()
        search_all_links = [link.text for link in search_all_links.find_all('a')]
        filter_target_data = list(filter(lambda x: '_20' in x, search_all_links))
        return filter_target_data

def download(full_filepath:str, download_folder:str):
    #base_url = f'https://odp.met.hu/weather/weather_reports/synoptic/hungary/{type}/csv/'
    filename = full_filepath.split('/')[-1]
    
    urllib.request.urlretrieve(full_filepath, download_folder + filename)


if __name__ == '__main__':
    today = datetime.today()
    today_string = f'{today:%Y-%m-%d}'
    
    download_folder = 'C:/Users/Laci/Downloads/'
    
    a = Adattar() 
    url = a.hourly
    
    active_files = a.get_filenames()
    
    for file in active_files:
        print(file)
        download(url + file, download_folder)
        