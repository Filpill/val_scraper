import scrapy
import json

class PlayerState(scrapy.Spider):
    name = 'playerState'
    start_urls =  ['https://dak.gg/valorant/en/profile/FilPill-EUW']
    headers = {
    # ":authority:":" val.dakgg.io"
    # ":method:":" GET"
    # ":path:":" /api/v1/accounts/JPnyLxsiavseiYbL8xtmWSuFRHdupX43u_hVynD5YScr2_Y32Wt2v5K-NvxvfDRWTL67AHdVSmoLTg/matches"
    # ":scheme:":" https"
   "accept":" application/json, text/plain, */*"
   # "accept-encoding":" gzip, deflate, br"
   # "accept-language":" en-US,en;q=0.9"
   # "origin":" https://dak.gg"
   # "referer":" https://dak.gg/"
   # "sec-fetch-dest":" empty"
   # "sec-fetch-mode":" cors"
   # "sec-fetch-site":" cross-site"
   # "sec-gpc":" 1"
   # "user-agent":" Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
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
        # for item in data:
        #     matches = item['matches']


        
#         data = json.loads(response.css('script::text').extract()[-1])
#         item_list = data['itemListElement']
#         for item in item_list:
#             yield {item}
        
        
        
        
        
        
        
        
        
#        data = json.loads(response.body)        
#        matches = data['data']['matches']
#         for match in matches:
#             item = {
#                 'Date':match['metadata']['timestamp'],
#                 'Map Name':match['metadata']['mapName'],
#                 'Match Result':match['metadata']['results'],
#                 'Agent Name':match['segments'][0]['metadata']['agentName'],
#                 'kills':match['segments'][0]['stats']['kills']['value'],
#                 'headshots':match['segments'][0]['stats']['headshots']['value'],
#                 'deaths':match['segments'][0]['stats']['deaths']['value'],
#                 'assists':match['segments'][0]['stats']['assists']['value'],
#                 'damage':match['segments'][0]['stats']['damage']['value'],
#                 'damageRecieved':match['segments'][0]['damageRecieved']['mapName']['value'],
#                 'plants':match['segments'][0]['stats']['plants']['value'],
#                 'defuses':match['segments'][0]['stats']['defuses']['value'],
#                 'firstBloods':match['segments'][0]['stats']['firstBloods']['value'],
#                 'kdRatio':match['segments'][0]['stats']['kdRatio']['value'],
#                 'placement':match['segments'][0]['stats']['placement']['value'],
#                 'rank':match['segments'][0]['stats']['rank']['metadata']['tierName'],
#             }

#             time.sleep(2) #sleep timer to prevent getting ip-banned by website
#             yield item
#         print(item)
#         self.id_url = self.id_url+1
#         time.sleep(6)

        # #Looping from keys to get data from other pages, appending to the api request
        # if(self.id_url<=2):
        #     next_page = 'https://api.tracker.gg/api/v2/valorant/standard/matches/riot/FilPill%23EUW?type=competitive&next='+str(self.id_url)
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page,callback=self.parse,dont_filter=True)