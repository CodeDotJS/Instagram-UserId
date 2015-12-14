import json

import urllib2

import sys

user = sys.argv[1]

def extract(user=user):

    f = urllib2.urlopen('http://jelled.com/ajax/instagram?do=username&username='+user)

    get_JSON = json.load(f)

    files = open(str(user) + '.json', 'w')

    files.write(str (get_JSON))

    files.close()

    return get_JSON["data"][0]["id"]

if __name__ == "__main__":

    print "The Id of " + user + ' is ' + extract()
