import os
import fnmatch
import fileinput

def fixHack():
  dirToWalk = "lookthink"
  count = 0

  for root, dirnames, filenames in os.walk(dirToWalk): 
    for filename in fnmatch.filter(filenames, '*.php'):
      f = os.path.join(root,filename);
      for linenum,line in enumerate( fileinput.FileInput(f,inplace=1) ): 
        if linenum != 0:
          print line.rstrip()
        else:
          print "<?php"
          count+=1
   

  print(count)


if __name__ == "__main__":
    fixHack()
