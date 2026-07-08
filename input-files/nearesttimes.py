from datetime import datetime
import os
import json

RTDIR = os.getcwd()
OUTPUTDIR = f'{RTDIR}/overall-data'
INPUTDIR = f'{RTDIR}/input-files'
PREDSFILENAME = 'AllPredictions.json'
WEATHFILENAME = 'data.json'
TEMPFILENAME = 'TimeComparisons.json'

def getweatherdates():
    os.chdir(INPUTDIR)
    with open(WEATHFILENAME) as f:
        fulldata = json.load(f)
    
    datelist = []
    for i in fulldata:
        datelist.append(i['time'])
    
    for i in range(len(datelist)):
        datelist[i] = datetime.fromisoformat(datelist[i])
    
    return datelist

def getsimulationdates():
    os.chdir(INPUTDIR)
    with open(PREDSFILENAME) as f:
        fulldata = json.load(f)
    
    datelist = []
    dates = fulldata.keys()
    for i in dates:
        times = fulldata.get(i).keys()
        for j in times:
            datelist.append(f'{i}-{j}')
    
    for i in range(len(datelist)):
        datelist[i] = datetime.strptime(datelist[i], "%Y-%m-%d-%H:%M:%S")
    
    return datelist

def nearest_time(target_time, time_list):
    """
    Finds the nearest time in a list of times to a target time.

    Parameters:
    target_time (datetime): The time to compare against.
    time_list (list of datetime): A list of times to search through.

    Returns:
    datetime: The time from the list that is closest to the target time.
    """
    res = min(time_list, key=lambda x: abs(x - target_time))

    return res


wdates = getweatherdates()
simdates = getsimulationdates()

times = {}
for i in simdates:
    times[str(i)] = nearest_time(i,wdates).isoformat()

jsondata = json.dumps(times, indent=4, default=str)

os.chdir(OUTPUTDIR)
with open(TEMPFILENAME,"w") as f:
    f.write(jsondata)