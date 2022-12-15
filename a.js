function getFilesToBackup(lastBackup, changes) {
    if(!changes) return []
    const r=changes.filter(c=>c[1]>lastBackup).map(c=>c[0])
    return [...new Set(r)].sort()
  }

  const lastBackup = 1546300800
const changes = [
  [ 3, 1546301100 ],
  [ 2, 1546300800 ],
  [ 1, 1546300800 ],
  [ 1, 1546300900 ],
  [ 1, 1546301000 ]
]

console.log(getFilesToBackup(lastBackup, changes))