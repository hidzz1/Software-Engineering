sentence = "Hello World"
final_string = ""

for i in range(len(sentence)):

    if i % 2 == 1:

        final_string += sentence[i].upper()

    else:
        
        final_string += sentence[i].lower()

print(final_string)

string = "I am learning to code."

def alternateUppercase(s):
    i = 0
    a = s.split(' ')
    l = []
    for w in a:
        if i:
            l.append(w.upper())
        else:
            l.append(w)
        i = int(not i)
    return " ".join(l)

print(alternateUppercase(string))


