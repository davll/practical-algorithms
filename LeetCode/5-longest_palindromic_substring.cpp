#include <string>
#include <vector>
#include <utility>

struct RLEChar {
    char ch;
    int n;
    int p;
};

class Solution {
public:
    std::string longest_palindrome_v1(const std::string& s)
    {
        const int n = s.size();
        if (n == 0) {
            return "";
        }

        std::vector<std::vector<bool>> ispalindrome(n);
        for (int i = 0; i < n; ++i)
            ispalindrome[i].resize(n, false);

        // substrings with one char
        for (int i = 0; i < n; ++i)
            ispalindrome[i][i] = true;

        // substrings with two chars
        for (int i = 0; i < n-1; ++i)
            ispalindrome[i][i+1] = s[i] == s[i+1];
        
        // other substrings
        for (int k = 2; k < n; ++k) {
            for (int i = 0; i < n-k; ++i)
                if (s[i] == s[i+k])
                    ispalindrome[i][i+k] = ispalindrome[i+1][i+k-1];
        }

        // find maximum len of palindromic substrings
        int maxlen = 0;
        int ans_i;
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j)
                if (ispalindrome[i][j])
                    if (maxlen < j-i+1) {
                        maxlen = j-i+1;
                        ans_i = i;
                    }
        }

        return s.substr(ans_i, maxlen);
    }

    std::string longest_palindrome_v2(const std::string& s)
    {
        const int n = s.size();
        if (n == 0) {
            return "";
        }

        // RLE compression
        std::vector<RLEChar> cs;
        cs.emplace_back(RLEChar { .ch = s[0], .n = 0, .p = 0 });
        for (char c : s) {
            if (cs.back().ch == c) {
                cs.back().n++;
            } else {
                cs.emplace_back(RLEChar { .ch = c, .n = 1, .p = 0 });
            }
        }

        const int m = cs.size();
        if (m == 1) {
            return s;
        }

        for (int i = 1; i < m; ++i)
            cs[i].p = cs[i-1].p + cs[i-1].n;

        std::vector<std::vector<int>> palindrome_size(m);
        std::vector<std::vector<int>> palindrome_wing(m);
        std::vector<std::vector<bool>> palindrome_full(m);
        for (int i = 0; i < m; ++i) {
            palindrome_size[i].resize(m, 0);
            palindrome_wing[i].resize(m, 0);
            palindrome_full[i].resize(m, false);
        }
        
        for (int i = 0; i < m; ++i) {
            palindrome_size[i][i] = cs[i].n;
            palindrome_wing[i][i] = cs[i].n;
            palindrome_full[i][i] = true;
        }
        
        for (int k = 2; k < m; ++k) {
            for (int i = 0; i < m-k; ++i)
                if (cs[i].ch == cs[i+k].ch) {
                    int l = cs[i].n, r = cs[i+k].n;
                    if (palindrome_full[i+1][i+k-1]) {
                        int w = std::min(l, r);
                        palindrome_size[i][i+k] = palindrome_size[i+1][i+k-1] + 2 * w;
                        palindrome_wing[i][i+k] = w;
                        palindrome_full[i][i+k] = l == r;
                    }
                }
        }

        int maxlen = 0;
        int ans_i;
        for (int i = 0; i < m; ++i) {
            for (int j = i; j < m; ++j)
                if (maxlen < palindrome_size[i][j]) {
                    maxlen = palindrome_size[i][j];
                    ans_i = cs[i].p + cs[i].n - palindrome_wing[i][j];
                }
        }

        return s.substr(ans_i, maxlen);
    }

    std::string longestPalindrome(const std::string& s)
    {
        return longest_palindrome_v2(s);
    }
};
