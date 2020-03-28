#include <vector>
#include <algorithm>

class Solution {
public:
    template<typename T, typename F>
    static int binary_seatch(const T* arr, int n, const T& key, F mapper) {
        int l = 0, r = n;
        while (l < r) {
            int m = (l + r) >> 1;
            const T& val = mapper(arr[m]);
            if (val == key) {
                return m;
            } else if (val < key) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return -1;
    }

    std::vector<int> twoSum(const std::vector<int>& nums, int target)
    {
        const int n = nums.size();

        std::vector<int> indirect(n);
        for (int i = 0; i < n; ++i)
            indirect[i] = i;

        std::sort(indirect.begin(), indirect.end(), [&](const int& a, const int& b)->bool{ return nums[a] < nums[b]; });

        for (int i = 0; i < n; ++i) {
            int j = binary_seatch(indirect.data(), n, target - nums[indirect[i]], [&](int k)->int{ return nums[k]; });
            if (j != -1 && j != i) {
                std::vector<int> result;
                result.reserve(2);
                result.push_back(indirect[i]);
                result.push_back(indirect[j]);
                return result;
            }
        }

        return std::vector<int>();
    }
};
