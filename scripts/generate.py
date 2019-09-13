import csv
from collections import namedtuple, defaultdict
Item = namedtuple("Item", 'page zine')
items = defaultdict(list)
with open('index.csv') as f:
    reader = csv.reader(f)
    next(reader, None) # skip header
    for row in reader:
        term, page, zine = row
        items[term].append(Item(page.strip(), zine.strip()))

zines = {
        'http': "HTTP: Learn your browser's language",
        'bite-size-networking': "Bite Size Networking",
}
for term, l in items.items():
    zine = l[0].zine
    pages = ', '.join([x.page for x in l])
    print(f'* {term}: [{zines[zine]}][{zine}] p. {pages}')
