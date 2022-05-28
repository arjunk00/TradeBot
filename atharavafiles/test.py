from forwardtestscraperclass import *
import datetime as dt

adani = ForwardTest('ADANIPORTS',dt.timedelta(minutes=5),1)
axis = ForwardTest('AXISBANK',dt.timedelta(minutes=5),1)
# hind = ForwardTest('HINDUNILVR',dt.timedelta(minutes=5),1)


# drreddy = ForwardTest('DRREDDY',dt.timedelta(minutes=5),1)
adani.start()
# hind.start()
axis.start()
adani.join()
axis.join()
# drreddy.start()