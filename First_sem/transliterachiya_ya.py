slovar = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
          'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K',
          'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
          'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc',
          'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E', 'Ю':
              'Iu', 'Я': 'Ia', 'Ъ': '', 'Ь': ''}

s = input()
st = ""
for i in s:
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
print(st)
