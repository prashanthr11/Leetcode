class Solution {
public:
    int numJewelsInStones(string a, string b) {
        unordered_map<char, int> mp;
        for(auto i:a)
            mp[i]++;
        int ret = 0;
        for(auto i:b) {
            if(mp[i]) 
                ret++;
        }
        return ret;
        
    }
};
