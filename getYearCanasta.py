from getData import getData
data = getData('./csv/DATOS_CANASTA_BASICA.csv')

gobernors = list(set(map(lambda x: x['GOBIERNO'], data)))

def getGobernYears(gobernor):
    yearsOfGobern = list(map(lambda x: x if x['GOBIERNO'] == gobernor else None,data))
    yearsOfGobernFilter = list(filter(None, yearsOfGobern))
    return yearsOfGobernFilter

def getLastYearGobern(gobernor):
    yearsOfGobern = getGobernYears(gobernor)
    lastMonthGoberned = yearsOfGobern[len(yearsOfGobern) - 1]
    return lastMonthGoberned

def lastYearEachGobernor():
    lastYearOfGobernors = []
    for gobernor in gobernors:
        lastYearOfGobernors.append(getLastYearGobern(gobernor))
    lastYearOfGobernorsOrdered = sorted(lastYearOfGobernors, key=lambda x: x['YEAR'])
    return lastYearOfGobernorsOrdered

def canastaPerYear():
    info = lastYearEachGobernor()
    years = list(map(lambda x: x['YEAR'], info))
    canasta = list(map(lambda x: float(x['COSTO_CANASTA'].replace(',','.')), info))
    return years, canasta