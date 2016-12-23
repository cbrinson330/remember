import os
import fnmatch
import fileinput

def renameFiles():
  updatedScriptTags = 0
  updatedHrefs = 0
  dirToWalk = "Multiscreen_HTML5"
  filesToSearch = ["topictable_0_xml.jsi", "searchfield.js", "Device_Help.log", "device_help.log", "device_help_ex.log", "search.js"]
  
  print "updated files"

  # Loop recursively through the files and find the ones that control the toc and linked files 
  for root, dirnames, filenames in os.walk(dirToWalk):
    for fname in filenames:
			if fname in filesToSearch or fname.startswith('toc'):
				f = os.path.join(root, fname)
				for linenun,line in enumerate(fileinput.FileInput(f,inplace=1)):
					if ".htm" in line:
      	    # Update href to target new php extention
						print line.replace(".htm",".php")
						updatedHrefs += 1
					else:
						print line.rstrip()

		#Loop through all htm files and update them 
    for filename in fnmatch.filter(filenames, '*.htm'):
      # change the extention from htm to php
      base = os.path.splitext(filename)[0]
      newFilename = base + ".php"
      renamedFile = os.path.join(root, newFilename)
      oldFile = os.path.join(root, filename)
      os.rename(oldFile, renamedFile)
      print oldFile 

      for linenum,line in enumerate( fileinput.FileInput(renamedFile,inplace=1) ):
        if linenum==0 :
          # Add php include to the first line of the file
          print "<?php include '/home/calam130/partners/joomla-auth.php'; ?>"
          print line.rstrip()

        elif line.startswith('<?'):
          # Remove javscript template regions from files 
          updatedScriptTags += 1

        elif ".htm" in line:
          # Update href to target new php extention
					print line.replace(".htm",".php")
					updatedHrefs += 1

        else:
            print line.rstrip()


  print ("number of removed javascript template tags = " + str(updatedScriptTags))
  print ("number of updated hrefs = " + str(updatedHrefs))

if __name__ == "__main__":
    renameFiles()
