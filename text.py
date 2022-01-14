s=input()
s=s.split()
censor=["XYZ" , "ADR" , "APK" , "YUJ" , "KOMM" , "QWU" , "LKK" , "RES" , "THU"]
for i in range(len(s)):
    if s[i] in censor:
        s[i]="#" * len(s[i])
a=" ".join(s)
print(a)
