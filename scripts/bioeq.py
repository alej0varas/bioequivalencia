import string

content = open('uso_tratamiento_bioeq.txt', 'r')

resultados = []
item = []
c = 0
last_n = 9999
gc = 1

for line in content:
    print gc, c, line,
    gc += 1
    result = ''
    line = line.strip()
    if c != 0 and line[0] in string.digits:
        #print 'no estoy en c = 0 y line[0] = ', line[0]
        curr_n = int(line[0])
        if curr_n > last_n:
            #print 'line[0] mayor que last_n = ', last_n
            line = line_prev + line
        else:
            last_n = curr_n
            line_prev = line
            continue
    else:
        last_n = 9999

    item.append(line)

    if c == 0:
        try:
            int(line)
        except:
            print item
            print 
            print resultados
            break
    if c == 7:
        resultados.append(item)
        item = []
        c = 0
    else:
        c += 1


# c = 1
# for i in resultados:
#     try:
#         int(i[0])
#     except:
#         print "\nvalido hasta",  c - 1
#         break
#     c += 1

print resultados

# N
# Uso / Tratamiento
# Principio Activo
# Producto de referencia
# Titular
# Producto Bioequivalente
# Registro
# Titular
