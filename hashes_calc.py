import sys
if sys.version_info[0] < 3:
    raw_input("You need to run this with Python 3!\nPress Enter to exit...")
    sys.exit(1)

import os, hashlib 

if not os.path.exists('tsd'):
    input("\nERROR: Cannot find tsd folder.\n\nPress Enter to exit...")
    sys.exit(1) 

if os.path.sep == "\\":
  eol = '\n'
else:
  eol = '\r\n'

fout = open('hashes.txt','w')
for dirpath, dirs, files in os.walk('tsd'):
  for filename in files:
    fname = os.path.join(dirpath,filename)
    with open(fname, 'rb') as f:
      if fout.tell():
        fout.write(eol)
      fout.write('FileName = "/' + fname.replace(os.path.sep, '/') + '"' + eol)
      fout.write('FileSize = "' + str(os.stat(fname).st_size) + '"' + eol)
      i=0
      while True:
        sha1 = hashlib.sha1()
        data = f.read(524288) #BUF_SIZE
        if not data:
         break
        sha1.update(data)
        if i>0:
            n = str(i)
        else:
            n =''
        fout.write('Checksum'+ n + ' = "' + sha1.hexdigest() + '"' + eol)
        i+=1
if fout.tell():
 print('hashes.txt is recalculated :)')
else:
 print('Something went wrong :(')
fout.close()