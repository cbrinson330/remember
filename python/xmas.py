import  urllib

def getWinners():

  #numbers to check
  LukeNumber = '0860'
  HelensNumber = '2349'
  
  #Status flags
  helenWon = False
  lukeWon = False

  #get data
  url = 'http://www.lions-lennetal.de/kalender_2014.html'
  response = urllib.urlopen(url)
  f = response.read()

  #parce data
  splitLines = f.split('<!--  Text: [begin] -->')
  lastSec = splitLines[2]
  lastSecSplit = lastSec.split('</p>')
  lines = lastSecSplit[0].split('<br />')

  #loop through data looking for numbers
  for l in lines:
    if l.find(LukeNumber) is not -1:
      lukeWon = True
    if l.find(HelensNumber) is not -1:
      helenWon = True

  #turn on lights
  print lukeWon
  print helenWon
  

if __name__ == "__main__":
  getWinners()
