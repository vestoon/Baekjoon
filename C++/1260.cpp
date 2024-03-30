#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#define endl "\n" // don't use when you cover interactive problem
#define all(v) (v).begin(), (v).end()

using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;

int dfs_visited[1001];
int bfs_visited[1001];
vector<int> edge[1001];

void dfs(int n) {
    if (!dfs_visited[n]) {
        cout << n << ' ';
        dfs_visited[n] = 1;
        for (int i = 0; i < edge[n].size(); i++) {
            dfs(edge[n][i]);
        }
    }
    return;
}



int main() {
#ifndef ONLINE_JUDGE
    freopen("./input.txt", "r", stdin);
    freopen("./output.txt", "w", stdout);
#endif

    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    // 여기다가
    
    int N, M, V; cin >> N >> M >> V;
    for (int i = 0; i < M; i++) {
        int x, y; cin >> x >> y;
        edge[x].push_back(y);
        edge[y].push_back(x);
    }
    for (int i = 1; i <= N; i++) {
        sort(edge[i].begin(), edge[i].end());
    }
    dfs(V);
    cout << '\n';
    queue<int> bfs;
    bfs.push(V);
    bfs_visited[V] = 1;
    while (bfs.size()) {
        cout << bfs.front() << ' ';
        int f = bfs.front();
        vector<int> next = edge[f];
        for (int i = 0; i < next.size(); i++) {
            if (!bfs_visited[next[i]]) {
                bfs.push(next[i]);
                bfs_visited[next[i]] = 1;
            }
        }
        bfs.pop();
    }


    // 코드 작성하기
    return 0;
}
