#include<iostream>
#include<deque>
#include<stack>
using namespace std;

int main() {
	string cmd, st;
	int n;
	char param;
	deque<char> L;
	stack<char> R;

	cin >> st >> n;
	for (int i = 0; i < st.size(); i++) {
		L.push_back(st[i]);
	}
	while (n--) {
		cin >> cmd;
		if (cmd == "L" && !L.empty()) {
			R.push(L.back());
			L.pop_back();
		}
		else if (cmd == "D" && !R.empty()) {
			L.push_back(R.top());
			R.pop();

		}
		else if (cmd == "B" && !L.empty()) {
			L.pop_back();
		}
		else if (cmd == "P") {
			cin >> param;
			L.push_back(param);
		}
	}
	//cout << "k";//
	while (!L.empty()) {
		cout << L.front();
		L.pop_front();
	}
	while (!R.empty()) {
		cout << R.top();
		R.pop();
	}
}