// https://codeforces.com/gym/102861/problem/G
#include <bits/stdc++.h>
using namespace std;

int main() {

	int m_max = 100;
	int control = 100;

	int n;

	cin >> n;

	for(int i = 0; i < n; i++) {
		int box;
		cin >> box;
		control += box;
		if( control > m_max)
			m_max = control;
	}

	cout << m_max;

}