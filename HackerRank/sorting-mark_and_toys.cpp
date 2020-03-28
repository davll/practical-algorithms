#include <bits/stdc++.h>

static std::vector<std::string> split_string(std::string);

// Complete the maximumToys function below.
static int maximumToys(std::vector<int>& prices, int k)
{
    std::sort(prices.begin(), prices.end());

    int count = 0;
    for (auto it = prices.begin(); it != prices.end() && k > 0; ++it) {
        if (k >= *it) {
            k -= *it;
            count++;
        }
    }

    return count;
}

int main()
{
    std::ofstream fout(getenv("OUTPUT_PATH"));

    std::string nk_temp;
    std::getline(std::cin, nk_temp);

    std::vector<std::string> nk = split_string(nk_temp);
    int n = stoi(nk[0]);
    int k = stoi(nk[1]);

    std::string prices_temp_temp;
    std::getline(std::cin, prices_temp_temp);

    std::vector<std::string> prices_temp = split_string(prices_temp_temp);
    std::vector<int> prices(n);

    for (int i = 0; i < n; i++) {
        int prices_item = stoi(prices_temp[i]);

        prices[i] = prices_item;
    }

    int result = maximumToys(prices, k);

    fout << result << "\n";

    fout.close();

    return 0;
}

std::vector<std::string> split_string(std::string input_string) {
    auto new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    std::vector<std::string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != std::string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, std::min(pos, input_string.length()) - i + 1));

    return splits;
}
