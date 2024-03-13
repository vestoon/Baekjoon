#include<iostream>
#include<queue>
#include<deque>
using namespace std;

int main() {
	deque<int> dq;
	string cmd;
	int param, n;
	cin >> n;
	while (n--) {
		cin >> cmd;
		if (cmd == "push_front") {
			cin >> param;
			dq.push_front(param);
		}
		else if (cmd == "push_back") {
			cin >> param;
			dq.push_back(param);
		}
		else if (cmd == "pop_front") {
			if (dq.empty()) {
				cout << -1 << endl;
			}
			else {
				cout << dq.front() << endl;
				dq.pop_front();
			}
		}
		else if (cmd == "pop_back") {
			if (dq.empty()) {
				cout << -1 << endl;
			}
			else {
				cout << dq.back() << endl;
				dq.pop_back();
			}
		}
		else if (cmd == "size") {
			cout << dq.size() << endl;
		}
		else if (cmd == "empty") {
			cout << dq.empty() << endl;
		}
		else if (cmd == "front") {
			if (dq.empty()) {
				cout << -1 << endl;
			}
			else {
				cout << dq.front() << endl;
			}
		}
		else if (cmd == "back") {
			if (dq.empty()) {
				cout << -1 << endl;
			}
			else {
				cout << dq.back() << endl;
			}
		}
	}
}