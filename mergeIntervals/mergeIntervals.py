'''
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].
'''

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def merge_intervals(arr):
    merged = []
    arr.sort(lambda x: x.start)

    start = arr[0].start
    end = arr[0].end

    for i in range(1, len(arr)):
        interval = arr[i]
        if interval.start <= end:
            end = max(end, interval.end) 
        else:
            merged.append(Interval(start,end))
            end = interval[i].end
            start = interval[i].start

    merged.append(Interval(start,end))
    return merged


