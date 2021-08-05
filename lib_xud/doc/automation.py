import re

def read_mbi(mbi_file, key_str, val_str):
    mbi = open(mbi_file, 'r')
    Lines = mbi.readlines()
    result_re = re.compile(val_str)
    search_re = re.compile('^\s*' + key_str + '\s*=\s*' + val_str)

    for line in Lines:
        m = re.findall(search_re, line)
        try:
            p = m[0].split('=')[1].lstrip()
            n = re.findall(result_re, p)[0]
            break
        except:
            n = 'no match'
    return n


project = read_mbi('./lib_xud/module_build_info', 'TITLE', '.*')
release = read_mbi('./lib_xud/module_build_info', 'VERSION', '[0-9]*\.[0-9]*\.[0-9]*')

print(release)
print(project)