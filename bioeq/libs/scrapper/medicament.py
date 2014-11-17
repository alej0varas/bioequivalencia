import pdftableextract as pdftable
import PyPDF2 as pdf
import re

is_header_text = lambda s: (s.find('Bioequivalentes') != -1)

def write(console, *args, **kwargs):
    if console:
        console.write(*args, **kwargs)

def transform(filename, console=None):
    write(console, "  - Parsing...", ending='')

    tablePdf   = pdf.PdfFileReader (file(filename, 'rb'))
    pages      = [ str(p) for p in range(1, len(tablePdf.pages) + 1)]

    # Procesing cells and flattern cells structure
    cells       = [pdftable.process_page(filename, p) for p in pages]
    cells       = [item for sublist in cells for item in sublist]

    table       = []

    write(console, "done")

    for page_table in pdftable.table_to_list(cells, pages):
 
        row_msg_format = "\r\033[K  - %d/%d records transformed"       
 
        page_table_rows = len(page_table)
        idx             = 0
 
        while idx < page_table_rows:
            write(console, row_msg_format % (idx, page_table_rows), ending='')

            cell_len       = sum([len(i) for i in page_table[idx]])

            if (cell_len == 0) or is_header_text(page_table[idx][0]):
                del page_table[idx]
                page_table_rows -= 1
            else:
                # Unicode for all
                for subidx in xrange(len(page_table[idx])):
                    page_table[idx][subidx] = unicode(page_table[idx][subidx], encoding='utf-8').strip()

                # Cases "1. medicament one 2. medicament two"
                if re.search(r'\d\.\W\W', page_table[idx][3]):
                    re_split_cases    = r'\W?\d+\.\W\W'
                    splitted_products = re.split(re_split_cases, page_table[idx][3])[1:]
                    splitted_vendors  = re.split(re_split_cases, page_table[idx][4])[1:]
                    added_products    = len(splitted_products)

                    if not len(splitted_vendors):
                        splitted_vendors = [ page_table[idx][4] ] * added_products

                    for i in xrange(0, added_products):
                        if i > 0: 
                            row_copy         = list(page_table[idx])
                            idx             += 1
                            page_table_rows += 1

                            page_table.insert(idx, row_copy)

                        page_table[idx][3] = unicode(splitted_products[i]).encode('utf-8')
                        page_table[idx][4] = unicode(splitted_vendors[i]).encode('utf-8')

                idx             += 1

        table += page_table

        write(console, row_msg_format % (idx, page_table_rows), ending='')
        
    write(console, '')

    return table