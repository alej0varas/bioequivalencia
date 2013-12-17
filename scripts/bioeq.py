content = open('uso_tratamiento_bioeq.txt', 'r')

resultados = []
item = []
c = 0

for line in content:
    result = ''
    line = line.strip()
    if line == '':
        continue
    item.append(line)
    #print c, line

    if c == 6:
        resultados.append(item)
        item = []
        c = 0
    else:
        c += 1

c = 0
for i in resultados:
    print c
    try:
        int(i[0])
    except:
        print "valido hasta",  c
        break
    c += 1

print resultados[:c + 1]


# N
# Uso / Tratamiento
# Principio Activo
# Producto de referencia
# Titular
# Producto Bioequivalente
# Registro
# Titular
