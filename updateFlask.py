import sys
from flask import Flask
app = Flask('updateFlask')

@app.route("/")
def update():
    tl = tail_lines('/var/log/syslog',10,1)
    f = file('/path/to/www/file.txt', 'w')
    for line in tl:
        # TODO: split line if too long
        f.write(line + "\n")
    f.close()
    return "OK"

def tail_lines(filename,linesback=10,returnlist=0):
    '''Does what "tail -10 filename" would have done
       Parameters:
            filename   file to read
            linesback  Number of lines to read from end of file
            returnlist Return a list containing the lines instead of a string

    '''
    avgcharsperline=75

    file = open(filename,'r')
    while 1:
        try: file.seek(int(-1 * avgcharsperline * linesback),2)
        except IOError: file.seek(0)
        if file.tell() == 0: atstart=1
        else: atstart=0

        lines=file.read().split("\n")
        if (len(lines) > (linesback+1)) or atstart: break
        #The lines are bigger than we thought
        avgcharsperline=avgcharsperline * 1.3 #Inc avg for retry
    file.close()

    if len(lines) > linesback: start=len(lines)-linesback -1
    else: start=0
    if returnlist: return lines[start:len(lines)-1]

    out=""
    for l in lines[start:len(lines)-1]: out=out + l + "\n"
    return out
