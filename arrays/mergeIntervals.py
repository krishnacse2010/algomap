class Solution:
    def merge(self, intervals):
        mergeInterval = []
        intervals.sort(key=lambda x:x[0])
        

        for interval in intervals:
            if len(mergeInterval) == 0 or interval[0] > mergeInterval[-1][1]:
                mergeInterval.append(interval)
            else:
                mergeInterval[-1] = [mergeInterval[-1][0] , max(interval[1],mergeInterval[-1][1])]
        print(mergeInterval)
            


intervals = [[1,3],[2,6],[8,10],[15,18]]
a=Solution()
a.merge(intervals)
intervals =[[1,4],[4,5]]
a.merge(intervals)