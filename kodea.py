#leer el archivo de selected SNPs, 600 lineas
import re
import csv

lines_small= []
print('Reading small file')
with open("/Users/med-azp/Desktop/python/file_small.csv") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        lines_small.append(line)

lines_small
#leer el archivo grande, 5000 lineas
lines_big= []

print('Reading big file')
with open("/Users/med-azp/Desktop/python/file_big.csv") as tsv:
    for line in csv.reader(tsv, dialect="excel-tab"):
        lines_big.append(line)

f = open("/Users/med-azp/Desktop/python/file_final.csv", 'w')
for line_small in lines_small:
    line_small= line_small[0].split(',')

    for line_big in lines_big:
        if line_small[:2] == line_big[:2]: 
        #asume primera y segunda
            match = re.search('R2=(\d+\.\d+)', line_big[7])
            if match:
                r2 = match.group(1)
            
            f.write(line_big[0] + ',' + line_big[1] + ',' + r2 + '\n')
f.close()