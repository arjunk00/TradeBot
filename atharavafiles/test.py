from forwardtestscraperclass import *
import datetime as dt

adani = ForwardTest('ADANIPORTS',dt.timedelta(minutes=5),1)
drreddy = ForwardTest('DRREDDY',dt.timedelta(minutes=5),1)
adani.start()
drreddy.start()