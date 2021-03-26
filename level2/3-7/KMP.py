def search_substring(txt, pat):
    pat_len = len(pat)

    def is_same(substr):
        if substr == pat:
            return True
        return False

    front = pat[0]
    for i in range(len(txt)):
        if txt[i] == front:
            if is_same(txt[i:i + pat_len]):
                return i

    return -1


txt = "aaacaaab"
pat = "aaab"

print(search_substring(txt, pat))




