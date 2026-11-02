#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <sstream>
#include <cctype>

class StringMatcher {
public:
    static std::string toLowerCase(const std::string& input) {
        std::string result = input;
        std::transform(result.begin(), result.end(), result.begin(),
                       [](unsigned char c) { return std::tolower(c); });
        return result;
    }

    static std::vector<int> computeKMPPrefixTable(const std::string& pattern) {
        int m = pattern.length();
        std::vector<int> lps(m, 0);
        int length = 0;
        int i = 1;

        while (i < m) {
            if (pattern[i] == pattern[length]) {
                length++;
                lps[i] = length;
                i++;
            } else {
                if (length != 0) {
                    length = lps[length - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }

    static std::vector<int> searchPatternKMP(const std::string& text, const std::string& pattern) {
        std::vector<int> matchIndices;
        int n = text.length();
        int m = pattern.length();

        if (m == 0 || n == 0 || m > n) {
            return matchIndices;
        }

        std::vector<int> lps = computeKMPPrefixTable(pattern);
        int i = 0;
        int j = 0;

        while (i < n) {
            if (pattern[j] == text[i]) {
                i++;
                j++;
            }

            if (j == m) {
                matchIndices.push_back(i - j);
                j = lps[j - 1];
            } else if (i < n && pattern[j] != text[i]) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return matchIndices;
    }

    static std::vector<std::string> tokenize(const std::string& text) {
        std::vector<std::string> tokens;
        std::string current;

        for (char ch : text) {
            if (std::isalnum(static_cast<unsigned char>(ch)) || ch == '+' || ch == '#' || ch == '-') {
                current += std::tolower(static_cast<unsigned char>(ch));
            } else {
                if (!current.empty()) {
                    tokens.push_back(current);
                    current.clear();
                }
            }
        }
        if (!current.empty()) {
            tokens.push_back(current);
        }
        return tokens;
    }

    static std::unordered_map<std::string, int> computeFrequencyMap(const std::string& text) {
        std::unordered_map<std::string, int> frequencies;
        std::vector<std::string> tokens = tokenize(text);

        for (const auto& token : tokens) {
            if (token.length() >= 2) {
                frequencies[token]++;
            }
        }
        return frequencies;
    }

    static int countOccurrences(const std::string& corpus, const std::string& keyword) {
        std::string lowerCorpus = toLowerCase(corpus);
        std::string lowerKeyword = toLowerCase(keyword);
        std::vector<int> matches = searchPatternKMP(lowerCorpus, lowerKeyword);
        return static_cast<int>(matches.size());
    }
};

int main() {
    std::string sampleCorpus = "Candidate has experience with React, TypeScript, Docker, and React Native.";
    std::string targetKeyword = "React";

    int count = StringMatcher::countOccurrences(sampleCorpus, targetKeyword);
    std::cout << "Keyword: " << targetKeyword << " | Frequency: " << count << std::endl;

    return 0;
}

