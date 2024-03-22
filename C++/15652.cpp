#include<iostream>
using namespace std;
bool visited[100];
int arr[100];
int N, M;


void dfs(int d, int id) {
	if (d == M + 1) {
		for (int i = 1; i < M + 1; i++) {
			cout << arr[i] << ' ';
		}
		cout << endl;
	}
	else {
		for (int i = id; i < N + 1; i++) {
			/*if (visited[i] == true)
				continue;*/
			//visited[i] = true;
			arr[d] = i;
			dfs(d + 1, i );
			//visited[i] = false;
		}
	}
}


int main() {
	cin >> N >> M;
	dfs(1, 1);

	return 0;
}