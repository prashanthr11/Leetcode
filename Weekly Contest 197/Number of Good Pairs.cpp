class Solution {
public:
    int numIdenticalPairs(vector<int>& a) {
        int cnt = 0;
        int n = a.size();
        
        for(int i = 0; i < n; ++i) 
            for(int j = i + 1; j < n; ++j) 
                if(a[i] == a[j])    ++cnt;
                
        return cnt;
        
    }
};
