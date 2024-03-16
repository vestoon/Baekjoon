#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main() {
	int inp; cin >> inp;
	int ans = 0;
	vector<int> position; position.push_back(-1);
	while (inp) {
		position.push_back(inp % 10);
		//cout << "p: " << inp % 10 << endl;
		inp /= 10;
	}
	int acc = 0;
	for (int i = position.size()-1; i > 0; i--) {
		if (position[i] == 1) {
			ans++;
		}
		else if (position[i]) {  // 0ÀÌ ¾Æ´Ò °æ¿ì
			ans += position[i] + acc;
			acc = 0;
		}
		else {
			acc += 9;
		}
		cout << ans << endl;
		;
	}
	cout << ans;

	return 0;
}