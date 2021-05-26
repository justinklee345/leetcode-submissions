class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        length_of_list = len(strs)

        #determine word of shortest length
        index = 0
        length_of_string = len(strs[0])

        for i in range(0, length_of_list):
            if len(strs[i]) < length_of_string:
                index = i
                length_of_string = len(strs[i])

        test = True

        #compare prefixes

        for l in range(0, length_of_string):
            FORletter = strs[index][l]
            for i in range(0, length_of_list):
                if strs[i][l] == FORletter:
                    if i == length_of_list-1:
                        prefix += FORletter
                else:
                    test = False
                    break
            if test == False:
                break

        return prefix
