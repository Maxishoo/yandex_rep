text = []
with open("public.txt", 'r', encoding='utf-8') as fr:
    for line in fr:
        text.append(line.rstrip('\n'))
sdvig = int(input())
newtext = []
for line in text:
    s = ''
    for i in line:
        if i.islower():
            if ord('a') <= ord(i) <= ord('z'):
                newsdvig = ord(i) - ord('a') + sdvig
                if newsdvig < 0:
                    newsdvig = 26 + newsdvig
                s = s + chr(newsdvig % 26 + ord('a'))
            else:
                s = s + i
        else:
            if ord('A') <= ord(i) <= ord('Z'):
                newsdvig = ord(i) - ord('A') + sdvig
                if newsdvig < 0:
                    newsdvig = 26 + newsdvig
                s = s + chr(newsdvig % 26 + ord('A'))
            else:
                s = s + i
    newtext.append(s)
with open('private.txt', 'w', encoding='utf-8') as fw:
    fw.write('\n'.join(newtext))
