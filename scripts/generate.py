import csv
from collections import namedtuple, defaultdict
items = defaultdict(list)
with open('index.csv') as f:
    reader = csv.reader(f)
    next(reader, None) # skip header
    for row in reader:
        row = [x.strip() for x in row]
        term, page, zine = row
        items[(term, zine)].append(page)

zines = {
        'http': "HTTP: Learn your browser's language",
        'tcpdump': "Let's learn tcpdump",
        'bite-size-networking': "Bite Size Networking",
        'bite-size-linux': "Bite Size Linux",
        'bite-size-command-line': "Bite Size Command Line",
        'debugging': "Linux debugging tools you'll love",
        'perf': "Profiling and tracing with perf",
        'networking': "Networking! ACK!",
        'manager': "Help! I have a manager!",
        'strace': "Spying on your programs with strace",
}

print("<table>")
print("<tr><td>term</td><td>zine</td><td>page</td></tr>")
terms = sorted(items.keys(), key=lambda x: x[0].lower())
for term, zine in terms:
    pages = ', '.join(items[(term, zine)])
    print(f'<tr><td> {term} </td>  <td><a href="https://wizardzines.com/zines/{zine}">{zines[zine]}</a> </td> <td> {pages} </td></tr>')
print("</table>")
