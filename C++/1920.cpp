#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

bool binSearch(vector<int>& arr, int target) {
	//cout << "searching " << target << '\n'; //
	if ((target < arr[0]) || (arr[arr.size() - 1] < target))
		return false;
	int lo = -1;
	int hi = arr.size();

	while (lo + 1 < hi) {
		int mid = (hi + lo) / 2;
		//cout << "mid = " << mid << endl; //
		if (arr[mid] < target) {
			lo = mid;
		}
		else {
			hi = mid;
		}
	}
	return arr[hi] == target;
}

/*
5
4 1 5 2 3
5
1 3 7 9 5
*/

// 1 2 3 4 5
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);


	int N; cin >> N;
	vector<int> arr;
	while (N--) {
		int tmp; cin >> tmp;
		arr.push_back(tmp);
	}
	sort(arr.begin(), arr.end());



	int M; cin >> M;
	while (M--) {
		int target; cin >> target;
		if (binSearch(arr, target))
			cout << 1;
		else
			cout << 0;
		cout << '\n';


	}


	return 0;
}