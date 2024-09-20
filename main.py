"""fonctions encodage Artcode"""

def artcode_i(s):
    """fonction itérative"""
    k=0
    lst=[]
    count=0
    for i, char in enumerate(s):
        if char == s[k]:
            count+=1
        else:
            lst.append((s[k],count))
            k=i
            count=1
    lst.append((s[k],count))
    return lst



def artcode_r(s, lst=None):
    """fonction récursive"""
    if lst is None:
        lst=[]
    if len(s) == 0:
        return lst
    char = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == char:
            count += 1
        else:
            break
    lst.append((char, count))
    return artcode_r(s[count:], lst)




#### Fonction principale


def main():
    """utilise les fonctions secondaires"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
