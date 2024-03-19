#include<iostream>
#include<algorithm>
using namespace std;
bool visited[100];
int arr[100], num[100];
int N, M;


void dfs(int d) {
	if (d == M + 1) {
		for (int i = 1; i < M + 1; i++) {
			cout << arr[i] << ' ';
		}
		cout << "\n";
	}
	else {
		for (int i = 1; i < N + 1; i++) {
			if (visited[i] == true)
				continue;
				visited[i] = true;
			arr[d] = num[i];
			dfs(d + 1);
			visited[i] = false;
		}
	}
}


int main() {
	cin >> N >> M;
	int x;
	for (int i = 1; i < N+1; i++) {
		cin >> x;
		num[i] = x;
	}
	sort(num+1, num + N+1);
	
	/*cout << "num: ";
	for (int i = 1; i < N + 1; i++) {
		cout << num[i] << " ";
	}*/
	/*cout << endl;*/
	dfs(1);

	return 0;
}