import zipfile, re

banner=''
zip1 = zipfile.ZipFile('channel.zip', 'r')
zipnumber = zip1.open('90052.txt', 'r').read()
banner += zip1.getinfo('90052.txt').comment
number_snatcher = re.compile('is ([0-9]+)')
numbers = number_snatcher.findall(zipnumber)
print numbers
while(numbers):
    zipnumber = zip1.open('%s.txt' % (numbers[0]), 'r').read()
    banner += zip1.getinfo('%s.txt' % (numbers[0])).comment
    number_snatcher = re.compile('is ([0-9]+)')
    numbers = number_snatcher.findall(zipnumber)
    print numbers
    
print banner