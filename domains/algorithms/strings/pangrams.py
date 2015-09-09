s = raw_input().lower()
alphabet = list("abcdefghijklmnopqrstuvwxyz")
for i in range(len(s)):
    if s[i] in alphabet:
        alphabet.remove(s[i])

print "not pangram" if alphabet else "pangram"
