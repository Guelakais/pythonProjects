import pandas as pd
from datetime import datetime
import numpy as np
import time
import pathlib

FOCUS_DATA_PATH = "./focus.txt"

def logFocusTime(start, end):
    if not pathlib.Path(FOCUS_DATA_PATH).is_file():
        with open(FOCUS_DATA_PATH, "w+") as focus:
            focus.write(f"{start} {end}")
            focus.write("\n")
    else:    
        with open(FOCUS_DATA_PATH, "a") as focus:
            focus.write(f"{start} {end}")
            focus.write("\n")


def trackFocus():
    start = int(time.time())
    end_session = input("Press to finish tracking")
    end = int(time.time())
    total = (end - start) / 3600
    print(f"Tracked: {total} hours")
    today_total = calculateFocusTime()
    print(f"Total focus time tracked today: {today_total}")
    logFocusTime(start, end)



def loadFocus():
    with open(FOCUS_DATA_PATH, "r") as focus:
        focusData = [f.strip("\n") for f in focus.readlines()]
    
    timeStarts = np.array([int(f.split()[0]) for f in focusData])
    timeEnds = np.array([int(f.split()[1]) for f in focusData])

    durations = (timeEnds - timeStarts)/3600
    timeStartsStamp = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')\
                       for ts in timeStarts]
    
    dateStartsStamp = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d')\
                       for ts in timeStarts]
        
    
    return timeStartsStamp,dateStartsStamp,durations


def create_focus_df():
    today = datetime.strftime(datetime.today(),format="%Y-%m-%d")
    timeStartsStamp,dateStartsStamp,durations=loadFocus()
    df = pd.DataFrame(dict(dates=dateStartsStamp, focus=durations))
    return df


def calculateFocusTime():
    df = create_focus_df()
    todayFocus = df[df["dates"]==today]["focus"].sum()

    return todayFocus