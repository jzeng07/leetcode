def longestCommonPrefix(strs):
    max_prefix = ""
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    for i in range(len(strs[0])):
        idx = 0
        for j in range(1, len(strs)):
            try:
                if strs[j][i] != strs[0][i]:
                    idx = j + 1
                    return max_prefix
            except IndexError as e:
                idx = j + 1
                return max_prefix
            idx = j + 1
        if idx == len(strs):
            max_prefix += strs[0][i]

    return max_prefix

print longestCommonPrefix(["", "b"])
print longestCommonPrefix([""])
print longestCommonPrefix(["ab", "cd"])
print longestCommonPrefix(["a"])
print longestCommonPrefix(["bb", "b"])
print longestCommonPrefix(["pre-a", "pree-b", "pree-c", "pre-d", "pra"])
             
