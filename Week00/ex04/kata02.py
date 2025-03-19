from datetime import datetime

kata = (2019, 9, 25, 3, 30)

# using the datetime module
dates = datetime(*kata).strftime("%m/%d/%Y %H:%M")
print(f"{dates}")

# using the str.format()
print("{:02d}/{:02d}/{:04d} {:02d}:{:02d}".format(kata[1], kata[2], kata[0], kata[3], kata[4]))
