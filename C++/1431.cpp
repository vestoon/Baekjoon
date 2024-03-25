#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;

int main() {
	int N; cin >> N;
	vector<string> arr;
	while (N--) {
		string tmp; cin >> tmp;
		arr.push_back(tmp);
	}

	sort(arr.begin(), arr.end(), [&](string s1, string s2) {
		if (s1.length() != s2.length())
			return s1.length() < s2.length();
		int s1Sum = 0, s2Sum = 0;
		for (char x : s1) {
			if (('0' < x) && (x <= '9')) {
				s1Sum += x - '0';
			}
		}
		for (char x : s2) {
			if (('0' < x) && (x <= '9')) {
				s2Sum += x - '0';
			}
		}
		if (s1Sum != s2Sum) {
			return s1Sum < s2Sum;
		}
		return s1 < s2;
		});
	for (string x : arr) {
		cout << x << '\n';
	}

	return 0;
}