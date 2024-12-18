import datetime

timestamp_low = -1354503710
timestamp_high = 31047188

full_timestamp = (timestamp_high << 32) | (timestamp_low & 0xFFFFFFFF)

timestamp_seconds = full_timestamp / 10**7
timestamp = datetime.datetime(1601, 1, 1) + datetime.timedelta(seconds=timestamp_seconds)

print(timestamp)
