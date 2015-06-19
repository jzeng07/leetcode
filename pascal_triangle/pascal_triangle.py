class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        result = []
        i = 0
        while  i < numRows:
            if i == 0:
                result.append([1])
                i += 1
                continue
            pre_row = result[i-1]
            cur_row = [1]
            for k in xrange(len(pre_row)):
                if k == len(pre_row) - 1:
                    cur_row.append(1)
                    continue
                cur_row.append(pre_row[k] + pre_row[k+1])
            result.append(cur_row)
            i += 1
        return result

    def getRow(self, rowIndex):
        pre_row = []
        i = 0
        if rowIndex == 0:
            return [1]
        while i < rowIndex:
            cur_row = [1]
            for k in xrange(len(pre_row) - 1):
                cur_row.append(pre_row[k] + pre_row[k+1])
            cur_row.append(1)
            i += 1
            pre_row = cur_row
        return cur_row
        


solution = Solution()
triangle = solution.generate(10)
row_n = solution.getRow(9)

for t in triangle:
    print t

print "row_n", row_n
