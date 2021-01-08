from datetime import datetime
import pytz

PST = pytz.timezone('America/Los_Angeles')
EST = pytz.timezone('America/New_York')
#UTC = pytz.timezone('Europe/London')

dt = datetime.now(timezone.utc)

portlandDT = dt.astimezone(PST)
nycDT = dt.astimezone(EST)
londonDT = dt

if portlandDT >= time(9,00) and porlandDT <= time(17,00):
    print("Portland HQ is open")
else:
    print("Portland HQ is closed")

if nycDT >= time(9,00) and nycDT <= time(17,00):
    print("New York City branch is open")
else:
    print("New York City branch is closed")

if londonDT >= time(9,00) and londonDT <= time(17,00):
    print("London branch is open")
else:
    print("London branch is closed")
