from time import gmtime, strftime

today = strftime("%Y-%m-%d %H:%M:%S")
today = today[:16]
print(today)
