#import urllib.request to get information from the url
import urllib.request
#import json to encode data to json format
import json

#create CountryFile function which creates text file with pretty json
def createCountyFile():
    #creates empty json data
    jsondata = ""
    #50 States' abbreviations. Used for changing url.
    states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
        ]
    #base url which will be changed in a loop for each state
    url = "http://api.sba.gov/geodata/city_county_links_for_state_of/in.json"
    #opens a County Data text file and writes to the file
    f = open('CountyData.txt', 'w')
    #Creates a loop throughout the states list for each state
    for s in states:
        #changes url to new url. The new url will be used to retrieve the
        #corresponding state's data
        url = url[:-7] + s + url[-5:]
        #Assigns newurl to equal the information received from the url
        #creates a loop for information received
        with urllib.request.urlopen(url) as newurl:
            #assigns the informatino received to data and decodes for json integration
            data = newurl.read().decode('utf-8')
            #decodes the json data recieved to python dictionary
            parsed = json.loads(data)
            #encodes the python dictonary back to json but this time with pretty formatting
            jsondata += json.dumps(parsed, sort_keys=True, indent = 4, separators=(',',': ')) 
            #writes the data to the file
            f.write(jsondata)
    #closes the file
    f.close()

#end of function

    



