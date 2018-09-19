from random import randint

# Nanti si matriks dan listBidak bakal jadi atribut object state
# Dengan semua fungsi yang ada di bawah sebagai method di object tsb

matriks = [
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.']
  ]

listBidak = []


# inputBidak sebagai tipe data contoh jika sudah diberi input
inputBidak = [
  {
    'jenisBidak': 'K',
    'jumlahBidak': 2
  }, {
    'jenisBidak':'B',
    'jumlahBidak': 2
  }, {
    'jenisBidak':'R',
    'jumlahBidak': 2
  }, {
    'jenisBidak':'Q',
    'jumlahBidak': 2
  }
]

def findBidakInPos(x, y):
  global listBidak
  return len(filter(lambda bidak: bidak['posisi'] == (x, y), listBidak))

def generateRandomBidak(jenisBidak, jumlahBidak):
  # Matriks dan list bidak dibikin global bukan sebagai param fungsti karena nantinya diasumsikan
  # fungsi ini menjadi method dan matriks dan input bidak sebagai attribute pada object state
  global matriks, listBidak
  for i in range(jumlahBidak):
    while True:
      x = randint(0, 7)
      y = randint(0, 7)
      if (not findBidakInPos(x, y)):
        break

    listBidak.append({
      'jenisBidak': jenisBidak, 
      'posisi': (x, y)
    })
    matriks[y][x] = jenisBidak

def generateRandomPapan():
  for bidak in inputBidak:
    generateRandomBidak(**bidak)

# Untuk testing dipanggil di sini
generateRandomPapan()

for i in matriks:
  print(' '.join(i))

for i in listBidak:
  print(i)
