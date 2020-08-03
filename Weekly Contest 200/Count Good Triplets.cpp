class Solution {
public:
    int countGoodTriplets(vector<int>& ar, int a, int b, int c) {
        int n = ar.size(), cnt = 0;
        for(auto i = 0; i < n; ++i) {
            for(auto j = i + 1; j <n; ++j)
            if(abs(ar[i] - ar[j]) <= a) {
                for(auto k = j + 1; k < n; ++k) {
                    if(abs(ar[j] - ar[k]) <= b && abs(ar[i] - ar[k]) <= c)
                       cnt++;
                }
            }
        }
        return cnt;
    }
};
