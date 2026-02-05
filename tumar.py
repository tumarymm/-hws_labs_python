def analize_text(text):
    t=text.lower()
    vowels= ('aeiouy')
    clean=''
    for c in t:
        if 'a' <= c <= 'z':
            clean+=c
        else:
            clean+=''
    u = ''
    for c in clean:
        if c in vowels and c not in u:
            u+=c
    words = []
    w = ''
    for c in clean:
        if c != ' ':
            w += c
        else:
            if len(w) >= 5 and w[-5:] in vowels:
                words.append(w)
            return(len(u),''.join(words))
print(analize_text('Hello, I am Tumar'))