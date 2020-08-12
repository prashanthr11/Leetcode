class Solution {
public:
    vector<int> getStrongest(vector<int>& a, int k) {
        sort(begin(a), end(a));
        int med = a[(a.size() - 1) / 2];
        sort(a.begin(), a.end(), [&] (int u, int v) {
            int x = abs(u - med), y = abs(v - med);
        if(x != y)
            return x > y;
        return u > v;
        });
        vector<int> res;
        for(int i = 0; i < k; ++i)  res.push_back(a[i]);
        
        return res;
    }
};
