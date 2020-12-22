import fileinput

fileList=['./files/file-1.txt','./files/file-2.txt','./files/file-3.txt']
files=fileinput.input(files=fileList)
for line in files:
    print(line)
    print(files.filename())
    print(files.isstdin())
    print('')
    pass

# $ echo -n 'foo' | python basic.py
# 'foo'
# $