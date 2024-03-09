#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {
	vector<int> arr;
	int N; cin >> N;
	while (N--) {
		int tmp; cin >> tmp;
		arr.push_back(tmp);
	}
	sort(arr.begin(), arr.end());

	for (int x : arr) {
		cout << x << '\n';
	}

	return 0;
}