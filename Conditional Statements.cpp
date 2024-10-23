#include <bits/stdc++.h>
#include <string>
#include <map>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
string numbertoWords(int);


int main()
{
    string n_temp;
    getline(cin, n_temp);

    int num = stoi(ltrim(rtrim(n_temp)));

    // Write your code here
    string result = numbertoWords(num);
    cout << result << endl;
    return 0;
}
//These 2 functions delete backspaces of the string from right and left 
string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

string numbertoWords(int num) {
    /* This function changes number from 0 to 1 to text*/ 
    if (num == 0) return "zero";
    map<int, string> belowTwenty = {
        {1, "one"}, {2, "two"}, {3, "three"}, {4, "four"}, {5, "five"},
        {6, "six"}, {7, "seven"}, {8, "eight"}, {9, "nine"},
        {10, "ten"}, {11, "eleven"}, {12, "twelve"}, {13, "thirteen"},
        {14, "fourteen"}, {15, "fifteen"}, {16, "sixteen"},
        {17, "seventeen"}, {18, "eighteen"}, {19, "nineteen"}
    };
    map<int, string> tens = {
        {2, "twenty"}, {3, "thirty"}, {4, "forty"},
        {5, "fifty"}, {6, "sixty"}, {7, "seventy"},
        {8, "eighty"}, {9, "ninety"}
    };
    string result;
    if (num <= 9){
        result += belowTwenty[num] + " ";
    } else {
        result += "Greater than 9";
    }
    return result;
}
