def is_anagram(str1, str2):

    s1 = sorted(str1.lower().replace(" " ," "))
    s2 = sorted(str2.lower().replace(" " ," "))
    return s1 == s2

w1 , w2 = "listen", "silent"
result = is_anagram(w1, w2)

print(f"IS {w1} and {w2} anagrams ?? : {result}")