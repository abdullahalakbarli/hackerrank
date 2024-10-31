#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
/*
2 2
3 1 5 4
5 1 2 8 9 3
0 1
1 3
*/

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n, q;
    cin >> n >> q;
    vector <vector <int>> all_data;
    vector <int> result;
    for (int i = 0; i < n; i++){
        int k;
        cin >> k;
        vector <int> lst = {};
        for (int j = 0; j < k; j++){
            int v = 0;
            cin >> v;
            lst.push_back(v);
        }
        all_data.push_back(lst);
    }
    for (int i = 0; i < q; i++){
        int q1, q2;
        cin >> q1 >> q2;
        result.push_back(all_data[q1][q2]);
    }
    for (int i = 0; i < q; i++){
        cout << result[i] << '\n';
    }
    return 0;
}
