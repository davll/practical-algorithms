#include <bits/stdc++.h>

static std::vector<std::string> split_string(std::string&);

// Complete the countSwaps function below.
static void countSwaps(std::vector<int>& a)
{
    int nswaps = 0;
    const int n = a.size();
    for (int i = n; i > 0; --i) {
        for (int j = 0; j < i-1; ++j) {
            if (a[j] > a[j+1]) {
                std::swap(a[j], a[j+1]);
                nswaps++;
            }
        }
    }

    std::cout << "Array is sorted in " << nswaps << " swaps.\n";
    std::cout << "First Element: " << a.front() << "\n";
    std::cout << "Last Element: " << a.back() << "\n";
}

int main()
{
    int n;
    std::cin >> n;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    std::string a_temp_temp;
    std::getline(std::cin, a_temp_temp);

    std::vector<std::string> a_temp = split_string(a_temp_temp);

    std::vector<int> a(n);

    for (int i = 0; i < n; i++) {
        int a_item = std::stoi(a_temp[i]);

        a[i] = a_item;
    }

    countSwaps(a);

    return 0;
}

static std::vector<std::string> split_string(std::string& input_string) {
    std::string::iterator new_end = std::unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
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
