import os
import json

RTDIR = os.getcwd()
INPUTDIRW = f'{RTDIR}/input-files'
INPUTDIRT = f'{RTDIR}/overall-data'
TIMESFILENAME = 'TimeComparisons.json'
WEATHERFILENAME = 'data.json'

OUTDIR = f'{RTDIR}/overall-data'
OUTFILENAME = 'TimesData.json'

def getwd():
    os.chdir(INPUTDIRW)
    with open(WEATHERFILENAME) as f:
        weather = json.load(f)
    os.chdir(RTDIR)
    return weather

def gettimes():
    os.chdir(INPUTDIRT)
    with open(TIMESFILENAME) as f:
        times = json.load(f)
    os.chdir(RTDIR)
    return times

def merge(times,weather):
    all = {}
    for i in times:
        for j in weather:
            if times[i] == j['time']:
                temp = j.copy()
                temp.pop('time')
                all[i] = temp
    return all

weath = getwd()
timess = gettimes()
out_data = merge(timess,weath)

os.chdir(OUTDIR)
with open(OUTFILENAME, 'w') as f:
    json.dump(out_data, f)