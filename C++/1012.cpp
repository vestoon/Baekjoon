#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#define endl "\n" // don't use when you cover interactive problem
#define all(v) (v).begin(), (v).end()

using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;

int arr[51][51];
//int visited[51][51];

int main() {
#ifndef ONLINE_JUDGE
    freopen("./input1012.txt", "r", stdin);
    freopen("./output1012.txt", "w", stdout);
#endif

    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);


    int T; cin >> T;
    int dx[4] = { 0,0,-1,1 };
    int dy[4] = { 1,-1,0,0 };
    while (T--) {
        int M, N, K; cin >> M >> N >> K;  // M ¿Ã ∞°∑Œ
        int count = 0;
        
        for (int i = 0; i < K; i++) {
            int x, y; cin >> x >> y;
            arr[x][y] = 1;  
        }
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j]) {
                    arr[i][j] = 0;
                    count++;
                    queue<pair<int,int>> bfs;
                    bfs.push({ i,j });
                    while (!bfs.empty()) {
                        pair<int, int> f = bfs.front(); bfs.pop();
                        for (int n = 0; n < 4; n++) {
                            int x = f.first + dx[n], y = f.second + dy[n];
                            if (arr[x][y] && 0 <=  x && x < M  && y < N && 0 <= y) {
                                bfs.push({ x,y });
                                arr[x][y] = 0;
                            }
                        }
                    }
                }
            }
        }
        cout << count << '\n';
        //for (int i = 0; i < 50; i++) {
        //    for (int j = 0; j < 50; j++) {
        //        arr[i][j] = 0; //visited[i][j] = 0;
        //    }
        //}
    }
    return 0;
}
