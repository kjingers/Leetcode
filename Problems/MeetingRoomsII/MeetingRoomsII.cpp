/*

Really only need to store end times in priority queue as minHeap. But I wanted to test making a custom comparator.
*/

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        
        struct myCompare {
            bool operator() (vector<int>& x, vector<int>& y) {
                return x[1] > y[1];
            }  
        };
        
        priority_queue<vector<int>, vector<vector<int>>, myCompare> pq;
        
        sort(intervals.begin(), intervals.end(), [](vector<int>& x, vector<int>& y) {return x[0] < y[0];});
        unsigned long minRooms = 0;
        for(auto& interval : intervals) {
            while(!pq.empty() && interval[0] >= pq.top()[1]) {
                pq.pop();
            }
            pq.push(interval);
            minRooms = max(minRooms, pq.size());
        }
        return minRooms;
        
    }
};
