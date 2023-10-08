slovar = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
          'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K',
          'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
          'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc',
          'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E', 'Ю':
              'Iu', 'Я': 'Ia', 'Ъ': '', 'Ь': ''}
file = open("cyrillic.txt", "r", encoding="UTF-8")
file2 = open("transliteration.txt", "a", encoding="UTF-8")
s = []
for line in file:
    s.append(line)
st = ""
for j in s:
    for i in j:
        if i.isupper():
            if i in slovar:
                st += slovar[i]
            else:
                st += i
        else:
            if i.upper() in slovar:
                st += slovar[i.upper()].lower()
            else:
                st += i
    file2.write(st)
    st = ''
file.close()
file2.close()
