class Solution {
public:
    int numIdenticalPairs(vector<int>& a) {
        int cnt = 0;
        unordered_map<int, int> mp;
        for(auto i:a) {
            cnt += mp[i];
            mp[i]++;
        }
        
        return cnt;
        
    }
};
