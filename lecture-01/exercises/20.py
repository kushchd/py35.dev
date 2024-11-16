#
sec = int(input("Enter total sec: "))
days = sec // (24 * 3600)
hours = (sec % (24 * 3600)) // 3600
minutes = (sec % 3600) // 60
seconds = sec % 60
print(days,"days", hours, "hours", minutes, "minutes", seconds, "seconds")