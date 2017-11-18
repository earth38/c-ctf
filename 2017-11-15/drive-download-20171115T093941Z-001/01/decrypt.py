def simpleSubstitutionCipher(c1, p1, c2, p2, c3):
   d = []

   for i in range(len(c3)):
        if c1.find(c3[i]) != -1:
            d.append(p1[c1.find(c3[i])])
        else: 
            d.append(p2[c2.find(c3[i])])

   return d

if __name__ == "__main__":
    f = open("question.txt")
    lines =f.readlines()

    c1 = lines[1][7:]
    p1 = lines[2][7:]

    c2 = lines[6][7:]
    p2 = lines[7][7:]

    c3 = lines[9][7:]

    d = simpleSubstitutionCipher(c1, p1, c2, p2, c3)
    print("".join(d))
