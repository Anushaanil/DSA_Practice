'''
Given two arrays arr[] and dep[], that represent the arrival and departure time of i-th train respectively. Find the minimum number of platforms required so that no train has to wait. If the departure time of one train is the same as the arrival time of another train, both trains cannot use the same platform at that time.
 
Note: Time intervals are in the 24-hour format (HHMM), where the first two characters represent hour (between 00 to 23) and the last two characters represent minutes (this will be <= 59 and >= 0). Leading zeros for hours less than 10 are optional (e.g., 0900 is the same as 900).

Input: arr[] = [1000, 935, 1100], dep[] = [1200, 1240, 1130]

Output: 3

Explanation: We need 3 platforms for the arrival of these trains because all three trains have overlapping time.
 
Input: arr[] = [900, 1235, 1100], dep[] = [1000, 1240, 1200]

Output: 1

Explanation: Only 1 platform is required for all the three trains because the departure time of each train is less then arrival time of next train.
'''

# psuedocode
# compare arrival values with departure values 
# if we compare arrival values with the 1st departure time, we get to know if they overlap or not
# keep count as 1 as we need a platform always

[900, 1000, 1100, 1200, 1235, 1240]

def min_platforms(arr, dep):
    platforms_count = 1 # min 1
    for timing in range(1, len(arr)):
        if arr[timing] < dep[0]:
            platforms_count+=1
    return platforms_count

arr= [1315, 1235, 1100]
dep = [1800, 1240, 1200]

[1100, 1200, 1235, 1240, 1315, 1800]
print(min_platforms(arr, dep))