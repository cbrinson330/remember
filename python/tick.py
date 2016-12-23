#hold status
rows = []
cols = []
diag = []

player1 = 'X'
player2 = 'O'

#check for win
def winCheck():
  gameWon = False
  boardFull = True 

  #check rows for win
  for r in rows:
    if r[0] == r[1] == r[2] and r[0] != 'e':
      gameWon = True

  #check cols for win
  if not gameWon:
    for c in cols:
      if c[0] == c[1] == c[2] and c[0] != 'e':
        gameWon = True

  #check diag for win
  if not gameWon:
    for d in diag:
      if d[0] == d[1] == d[2] and d[0] != 'e':
        gameWon = True
  
  #check rows for full board
  if not gameWon:
    for r in rows:
      for s in r:
        if s == 'e':
          boardFull = False
 
  if gameWon or not gameWon and boardFull:
    return True
  else:
    return False

def setVal(sq, val):
  #sq must be in [x,y] format
  row = sq[0]
  col = sq[1]

  #set row value
  if rows[row][col] == 'e':
    rows[row][col] = val
  else:
    print 'Error square already set'

  #set col value
  if cols[col][row] == 'e':
    cols[col][row] = val
  else:
    print 'Error Square already set'

  #update diag Value from new updated rows
  diag[0][0] = rows[0][0]
  diag[0][1] = rows[1][1]
  diag[0][2] = rows[2][2]
  
  diag[1][0] = rows[0][2]
  diag[1][1] = rows[1][1]
  diag[1][2] = rows[2][0]

def printBoard():
  output = '- - - - -'
  for r in rows:
    output += '\n'
    count = 0
    for s in r:
      count += 1
      if count == 3:
        output += s
      else:
        output += s + ' | '
    output += '\n'
    output += '- - - - -'

  print output;
  
def start():
  while True:
    rows = [['e','e','e'],['e','e','e'],['e','e','e']]
    cols = [['e','e','e'],['e','e','e'],['e','e','e']]
    diag = [['e','e','e'],['e','e','e']]

    printBoard()
    setVal([0,0], player1)
    setVal([0,1], player1)
    setVal([0,2], player1)
    printBoard()
    winCheck()

if __name__ == "__main__":
  start()
