import os
import json

RTDIR = os.getcwd()
INPUTDIRW = f'{RTDIR}/input-files'
INPUTDIRT = f'{RTDIR}/overall-data'
INPUTDIRL = f'{RTDIR}/input-files'
TIMESFILENAME = 'TimeComparisons.json'
WEATHERFILENAME = 'data.json'
LOCATIONFILENAME = 'AllPredictions.json'

OUTDIR = f'{RTDIR}/overall-data'
OUTFILENAME = 'TimesData.json'

def getjson(inputdir, filename):
    os.chdir(inputdir)
    with open(filename) as f:
        data = json.load(f)
    os.chdir(RTDIR)
    return data

def merge(times,weather,locations):
    all = {}
    for i in times:
        for j in weather:
            if times[i] == j['time']:
                temp = j.copy()
                temp.pop('time')
                all[i] = temp
        for j in locations:
            for k in locations[j]:
                if i == f'{j} {k}':
                    all[i].update(locations[j][k].copy())
    return all

weath = getjson(INPUTDIRW, WEATHERFILENAME)
timess = getjson(INPUTDIRT, TIMESFILENAME)
locs = getjson(INPUTDIRL, LOCATIONFILENAME)
out_data = merge(timess,weath,locs)
print(out_data)

os.chdir(OUTDIR)
with open(OUTFILENAME, 'w') as f:
    json.dump(out_data, f)