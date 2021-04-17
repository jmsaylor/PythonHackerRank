def checkMagazine(magazine, note):
    magazine_words = {}
    for word in magazine:
        if word in magazine_words:
            temp = magazine_words[word]
            magazine_words[word] = temp + 1
        else:
            magazine_words[word] = 1

    note_words = {}
    for word in note:
        if word in note_words:
            note_words[word] += 1
        else:
            note_words[word] = 1

    print("mag", magazine_words)
    print("note", note_words)
    result = True
    for word in list(note_words):
        print(word, magazine_words[word] < note_words[word])
        if word not in magazine_words or magazine_words[word] < note_words[word]:
            result = False

    print("Yes" if result else "No")

mag = ['two', 'times', 'three', 'is', 'not', 'four']
note = ['two', 'times', 'two', 'is', 'four']

checkMagazine(mag, note)