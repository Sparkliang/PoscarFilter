# POSCAR
import re
f = open('D:/PythonCodes/Others/po.txt', 'rt')
data = f.read()
f.close
data = re.sub(r'Li', r' ', data)
data = re.sub(r'Ni', r' ', data)
data = re.sub(r'O', r' ', data)
data = re.sub(r'Al', r' ', data)
data = re.sub(r'Co', r' ', data)
with open('D:/PythonCodes/Others/po.txt', 'wt') as f:
                f.write(data)
