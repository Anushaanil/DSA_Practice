'''
 # @ Create Time: 2025-09-04 13:57:04
 # @ Modified time: 2025-11-17 00:38:52
 '''


def insert(intervals, newInterval):
    res = []
    start = 0
    end = 0 
    
    for i in range(1, len(intervals)):
        print(intervals[i-1][0], newInterval[0], intervals[i][0])
        
        print(intervals[i-1][1], newInterval[1], intervals[i][1])
        
        #  <= intervals[i][0]
        
        if intervals[i-1][0] <= newInterval[0]:
            start = min(intervals[i-1][0], newInterval[0])
            print('start', start)
        
        if intervals[i-1][1] <= newInterval[1]:
            end = newInterval[1]
        
        else:
            res.append(intervals[i])
            print('else', res)
        
        print('end', end)
        res.append([start, end])
        print('here', res)
            
        
            
    return res


# intervals = [[1,3],[6,9]]
# newInterval = [2,5]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))