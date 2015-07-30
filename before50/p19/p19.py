def dayListBuild():
    dayListBuild = [[0,0,0]]
    for year in range(1900, 2001):
        for month in range(1, 13):
            if month in [4, 6, 9, 11]:
                dayRange = 30
            elif not month - 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                        dayRange = 29
                else:
                    dayRange = 28
            else:
                dayRange = 31
            for day in range(1, dayRange + 1):
                dayListBuild.append([year, month, day])
    return dayListBuild

def sundayList():
    dayList = dayListBuild()
    sundayList = []
    for day in range(len(dayList)):
        if not (day - 6) % 7 and dayList[day][0] > 1900 and not dayList[day][2] - 1:
            sundayList.append(dayList[day])
    return len(sundayList)

print(sundayList())