from forwardtestscraperclass import *
import datetime as dt
import time

adani = ForwardTest('ADANIPORTS',dt.timedelta(minutes=5),1)
axis = ForwardTest('AXISBANK',dt.timedelta(minutes=5),1)
adani.start()
time.sleep(150)
axis.start()
adani.join()
axis.join()
