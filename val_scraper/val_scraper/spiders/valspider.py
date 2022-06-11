import scrapy
import json
import time

class PlayerState(scrapy.Spider):
    name = 'playerState'
    start_urls =  ['https://api.tracker.gg/api/v2/valorant/standard/matches/riot/FilPill%23EUW?type=competitive&next=0']
    id_url = 0

    def parse(self, response):
        data = json.loads(response.body)
        matches = data['data']['matches']
        for match in matches:
            item = {
                'Date':match['metadata']['timestamp'],
                'Map Name':match['metadata']['mapName'],
                'Match Result':match['metadata']['results'],
                'Agent Name':match['segments'][0]['metadata']['agentName'],
                'kills':match['segments'][0]['stats']['kills']['value'],
                'headshots':match['segments'][0]['stats']['headshots']['value'],
                'deaths':match['segments'][0]['stats']['deaths']['value'],
                'assists':match['segments'][0]['stats']['assists']['value'],
                'damage':match['segments'][0]['stats']['damage']['value'],
                'damageRecieved':match['segments'][0]['damageRecieved']['mapName']['value'],
                'plants':match['segments'][0]['stats']['plants']['value'],
                'defuses':match['segments'][0]['stats']['defuses']['value'],
                'firstBloods':match['segments'][0]['stats']['firstBloods']['value'],
                'kdRatio':match['segments'][0]['stats']['kdRatio']['value'],
                'placement':match['segments'][0]['stats']['placement']['value'],
                'rank':match['segments'][0]['stats']['rank']['metadata']['tierName'],
            }

            time.sleep(2) #sleep timer to prevent getting ip-banned by website
            yield item
        print(item)
        self.id_url = self.id_url+1
        time.sleep(6)

        #Looping from keys to get data from other pages, appending to the api request
        if(self.id_url<=2):
            next_page = 'https://api.tracker.gg/api/v2/valorant/standard/matches/riot/FilPill%23EUW?type=competitive&next='+str(self.id_url)
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse,dont_filter=True)