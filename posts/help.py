def log(value):
    from datetime import datetime
    f = open(file='log.txt', mode='a')
    f.write(str(datetime.now()) + ' - ' + str(value) + "\n")
    f.close()
