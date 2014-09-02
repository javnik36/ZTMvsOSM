from bs4 import BeautifulSoup as parser
import urllib.request as urllib
import re

##Include after end
#url = "http://overpass-api.de/api/interpreter?data=%5Bout%3Axml%5D%3B%28area%283603509824%29%3Barea%283603014990%29%3Barea%283602603447%29%3Barea%283602719113%29%3Barea%283602603448%29%3Barea%283600336313%29%3Barea%283600336311%29%3Barea%283600336310%29%3Barea%283600336309%29%3Barea%283600336304%29%3Barea%283602101329%29%3Barea%283602996965%29%3Barea%283602996986%29%3Barea%283602997041%29%3Barea%283602996990%29%3Barea%283602415879%29%3Barea%283600336137%29%3Barea%283602416275%29%3Barea%283602416274%29%3Barea%283600336138%29%3Barea%283602996903%29%3Barea%283602924728%29%3Barea%283600336688%29%3Barea%283600336679%29%3Barea%283601994190%29%3Barea%283601994189%29%3Barea%283602910919%29%3Barea%283601994191%29%3Barea%283603015006%29%3Barea%283601994186%29%3Barea%283601753833%29%3Barea%283602695156%29%3B%29%2D%3E%2Earea%3B%28node%5B%22highway%22%3D%22bus%5Fstop%22%5D%28area%2Earea%29%3Bnode%5B%22railway%22%3D%22tram%5Fstop%22%5D%28area%2Earea%29%3Bnode%5B%22public%5Ftransport%22%3D%22stop%5Fposition%22%5D%28area%2Earea%29%3Bnode%5B%22public%5Ftransport%22%3D%22platform%22%5D%28area%2Earea%29%3Bway%5B%22public%5Ftransport%22%3D%22platform%22%5D%28area%2Earea%29%3B%29%3Bout%20body%3B%3E%3Bout%20skel%3B"
#path = 'stops.xml'
#urllib.urlretrieve(url, path)

#change path name
data = parser(open('TEMP-XML.xml'))

osm = data.osm
refs = []


##MAKE regex working!
for child in osm.children:
  for child_child in child:
    #ref = re.search("\ref", child_child)
    #dig = re.search("\v="(\d{6})"")



    if ref and dig:
      refs.append(dig.addgroup(0))
    else:
      continue




#  print(child)
#  print("KONIEC DZIECKA")

a = input("jeste glupi")
