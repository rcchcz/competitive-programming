// https://atcoder.jp/contests/abc219/tasks/abc219_b
#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    string S1, S2, S3, T;
    stringstream ss;    
    cin >> S1;
    cin >> S2;
    cin >> S3;
    cin >> T;

    for(auto i = 0; i < T.size(); i++) {
        if(T[i] == '1') ss << S1;
        else if(T[i] == '2') ss << S2;
        else if(T[i] == '3') ss << S3;
    }

    string r = ss.str();
    cout << r;

}