#include <string>
#include <algorithm>
#include <cassert>

class Solution {
public:
    int lengthOfLongestSubstring(const std::string& s)
    {
        int used[256];
        std::fill_n(used, 256, 0);

        const int n = s.size();
        int maxlen = 0;
        int l = 0, r = 0;
        while (r < n) {
            used[s[r]]++;
            while (used[s[r]] > 1) {
                used[s[l++]]--;
                assert(l <= r);
            }
            maxlen = std::max(maxlen, r - l + 1);
            r++;
        }

        return maxlen;
    }
};
