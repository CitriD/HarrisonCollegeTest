import urllib.request
import json

class CountyData:
    def __init__(self):
        self.states = [
            "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
            "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
            "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
            "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
            "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
            ]

        self.url = "http://api.sba.gov/geodata/city_county_links_for_state_of/in.json"

    def createCountyFile(self):
        jsondata = ""
        f = open('CountyData.txt', 'w')
        for s in self.states:
            self.url = self.url[:-7] + s + self.url[-5:]
            with urllib.request.urlopen(self.url) as newurl:
                data = newurl.read().decode('utf-8')
                parsed = json.loads(data)
                jsondata += json.dumps(parsed, sort_keys=True, indent = 4, separators=(',',': ')) 
                f.write(jsondata)

        f.close()

    def main(self):
        self.createCountyFile()

if __name__ == '__main__':
    CountyData().main()

    



