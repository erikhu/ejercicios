reverse = {
    'A': 'A',
    'B': '',
    'C': '',
    'D': '',
    'E': '3',
    'F': '',
    'G': '',
    'H': 'H',
    'I': 'I',
    'J': 'L',
    'K': '',
    'L': 'J',
    'M': 'M',
    'N': '',
    'O': 'O',
    'P': '',
    'Q': '',
    'R': '',
    'S': '2',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'Z': '5',
    '1': '1',
    '2': 'S',
    '3': 'E',
    '4': '',
    '5': 'Z',
    '6': '',
    '7': '',
    '8': '8',
    '9': ''
}
def j(case):
    palindrome = True
    mirrored = True
    for i in range(int(len(case)/2)):
        if case[i] != case[len(case)-i-1]:
            palindrome = False
        if reverse[case[i]] != case[len(case)-i-1]:
            mirrored = False

    #center of word if count letters are odd
    if len(case)%2 != 0  and reverse[case[int(len(case)/2)]] != case[int(len(case)/2)]:
        mirrored = False

    if(palindrome and mirrored):
        print("%s -- is a mirrored palindrome." % case)
    elif(not palindrome and not mirrored):
        print("%s -- is not palindrome." % case)
    elif(palindrome):
        print("%s -- is a regular palindrome." % case)
    else:
        print("%s -- is a mirrored string." % case)

def test_case():
   return ["NOTAPALINDROME",
           "ISAPALINILAPASI",
           "2A3MEAS",
           "ATOYOTA",
           "ATO3OTA",
           "MAAM"]

def run():
    for case in test_case():
        j(case)

run()
