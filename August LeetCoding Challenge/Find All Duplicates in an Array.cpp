class Solution {
public:
    vector<int> findDuplicates(vector<int>& a) {
        map<int, int> mp;
        vector<int> ans;
        for(auto i:a)
            if(mp[i]++)
                ans.push_back(i);
        return ans;
    }
};
