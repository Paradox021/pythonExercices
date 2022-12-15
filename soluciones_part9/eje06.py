# soluciona el problema 13 de adventJs
#https://adventjs.dev/es/challenges/2022/13

def getFilesToBackup(lastBackup, changes):
    #filtrado = filter(  lambda c: c[1]>lastBackup,  changes)
    #mapeado = map( lambda c: c[0]   ,  filtrado )
    #mapeado = [ c[0]  for c in changes if c[1]>lastBackup ]
    #set(mapeado)
    mapeado = { c[0]  for c in changes if c[1]>lastBackup }
    return sorted(mapeado)

lastBackup = 1546300800
changes = [
  [ 3, 1546301100 ],
  [ 2, 1546300800 ],
  [ 1, 1546300800 ],
  [ 1, 1546300900 ],
  [ 1, 1546301000 ]
]

print(getFilesToBackup(lastBackup, changes))
