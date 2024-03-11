#include<iostream>
#include<vector>
using namespace std;

int main() {
	vector<string> arr[201];
	int N; cin >> N;
	while (N--) {
		int tmpN; cin >> tmpN;
		string tmpS; cin >> tmpS;
		arr[tmpN].push_back(tmpS);
	}
	for (int i = 1; i < 201; i++) {
		if (!arr[i].empty()) {
			for (string s : arr[i]) {
				cout << i << ' ' << s << '\n';
			}
		}
	}




	return 0;
}