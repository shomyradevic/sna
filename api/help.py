from datetime import datetime

def log(value):
    with open(file='activities.log', mode='a') as f:
        f.write(str(datetime.now()) + ' - ' + str(value) + '.' + '\n')
        f.close()