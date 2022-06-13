import scrapy
import json

class PlayerState(scrapy.Spider):
    name = 'playerState'
    start_urls =  ['https://dak.gg/valorant/en/profile/FilPill-EUW']
    headers = {
   "accept":" application/json, text/plain, */*"
    }

    def parse(self, response):
        url = 'https://val.dakgg.io/api/v1/accounts/JPnyLxsiavseiYbL8xtmWSuFRHdupX43u_hVynD5YScr2_Y32Wt2v5K-NvxvfDRWTL67AHdVSmoLTg/matches'
        
        request = scrapy.Request(url, 
                                 callback = self.parse_api,
                                 headers=self.headers)
        yield request
        
    def parse_api(self,response):
        raw_data = response.body
        data = json.loads(raw_data)
        yield {
               'matches':data['matches']
        }
        