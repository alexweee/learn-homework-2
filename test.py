from datetime import date, timedelta, datetime

nw = datetime.now()

print(nw)

delta = timedelta(1, 1, 1, 1, 1, 1, 1, 1)

bz = nw - delta

print(bz)

