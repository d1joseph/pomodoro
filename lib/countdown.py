# simple countdown from t time
import time

def countdown():
    t = int(input('Enter time in minutes: ')) * 60 # convert to minutes
    while t: # while t > 0 for clarity 
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r") # overwrite previous line 
        time.sleep(1)
        t -= 1


if __name__ == "__main__":
    countdown()