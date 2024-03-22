#include<iostream>
using namespace std;
bool visited[100];
int arr[100];
int N, M;


void dfs(int d, int id) { // 여기서 매개변수 d 는 시작하는 깊이를 말하는건가?
	if (d == M+1) {
		for (int i = 1; i < M+1; i++) {
			cout << arr[i] << ' ';
		}
		cout << endl;
	}
	else {
		for (int i = id; i < N + 1; i++) {
			if (visited[i] == true)
				continue;
			visited[i] = true;
			arr[d] = i;
			dfs(d + 1, i+1);
			visited[i] = false;
		}
	}
}


int main() {
	cin >> N >> M;
	dfs(1,1);
	
	return 0;
}
// 뎁스가 매개변수로 꼭 필요할까? nm 도 전역변수가 아니라서 재귀만들때 매개변수로 넣어줘야 함