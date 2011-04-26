#!/usr/bin/python3.1

import os
import sys
import http.client

version = "1.22.0"

def main(argv):
  c_begin = [158200, 81900]
  c_end = [158801, 82501]

  total = (c_end[0]-c_begin[0])*(c_end[1]-c_begin[1])
  print (total)
  c = 0
  for x in range(c_begin[0], c_end[0]):
    for y in range(c_begin[1], c_end[1]):    
      c += 1
      result = GetTile(x, y)
      flag = " " if result == 1 else "+"
      if flag == "+":
        print("GET {: >10} {: >10} | {:.2f}% {: ^1}".format(x, y, round((c/total)*100,2), flag))
  return 0

def GetTile(x, y):

  filename = "./map/{x}_{y}_18.jpg".format(x = x, y = y)
  if os.path.isfile(filename):
    return 1
  url = "/tiles?l=sat&v={ver}&x={x}&y={y}&z=18&g=Gagarin".format(x = x, y = y, ver = version)
  conn = http.client.HTTPConnection("sat02.maps.yandex.ru")
  conn.request("GET", url)
  response = conn.getresponse()
  if response.status == 200:
    data = response.read()
    f = open(filename, "wb")
    f.write(data)
    f.close()

  return 0

if __name__ == "__main__":
  sys.exit(main(sys.argv))
