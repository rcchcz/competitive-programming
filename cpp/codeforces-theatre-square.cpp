// https://codeforces.com/contest/1/problem/A
#include <bits/stdc++.h>
using namespace std;

int main() {
    long long int n, m, a, fn, fm;
    cin >> n >> m >> a;
    
    fn = n/a;
    if(fn == 0) fn = 1;
    while(fn * a < n) fn++;

    fm = m/a;
    if(fm == 0) fn = 1;
    while(fm * a < m) fm++;

    cout << fn * fm;   
}