from forwardtestscraperclass import *
import datetime as dt
import time

adani = ForwardTest('ADANIPORTS',dt.timedelta(minutes=1),1)
# axis = ForwardTest('AXISBANK',dt.timedelta(minutes=5),1)
# hind = ForwardTest('HINDUNILVR',dt.timedelta(minutes=5),1)
# hind.start()
adani.start()
# time.sleep(150)
# axis.start()
adani.join()
# axis.join()
