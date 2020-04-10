import  traceback

try:
    raise Exception('This is the err message')
except:
    errorfile = open('errlog.txt','a')
    errorfile.write(traceback.format_exc())
    errorfile.close()
    print('The Tracebak info was writtern errlog.txt')