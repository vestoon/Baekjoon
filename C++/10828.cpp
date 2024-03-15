#include <iostream>
#include <stack>
using namespace std;

int main() {
	stack<int> st;
	int n, param;
	string cmd;
	cin >> n;

	while (n--) {
		cin >> cmd;
		if (cmd == "push") {
			cin >>param;
			st.push(param);
		}
		else if (cmd == "pop") {
			if (st.empty()) {
				cout << -1 << endl;
			}
			else {
				cout << st.top() << endl;
				st.pop();
			}
		}
		else if (cmd == "size") {
			cout << st.size() << endl;
		}
		else if (cmd == "empty") {
			cout << st.empty() << endl;
		}
		else if (cmd == "top") {
			if (st.empty()) {
				cout << -1 << endl;
			}
			else {
				cout << st.top() << endl;
			}
		}
	}
}