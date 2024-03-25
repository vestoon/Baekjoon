#define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
#define endl "\n" // don't use when you cover interactive problem
#define all(v) (v).begin(), (v).end()

using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
typedef pair<ll, ll> pl;

long int biSearch(vector<int>& hay, long int& i, long int& j) {
    long int lo = 0, hi = hay.size() - 1;
    long int mid, glb = lo-1;
    while (hi >= lo) { // glb 찾기
        mid = (lo + hi) / 2;
        if (hay[mid] < i) {
            glb = mid;
            lo = mid+1;
        }
        else {
            hi = mid-1;
        }
    }
    lo = 0; hi = hay.size() - 1;
    long int sub = hi+1;
    while (hi >= lo) { // sub 찾기
        mid = (lo + hi) / 2;
        if (hay[mid] > j) {
            hi= mid-1;
            sub = mid;
        }
        else {
            lo = mid + 1;
        }
        
    }
    //cout << "glb: " << glb << ", " << "sub: " << sub << endl; //
    return sub - glb - 1;
}


int main() {
#ifndef ONLINE_JUDGE
    freopen("./input.txt", "r", stdin);
    freopen("./output.txt", "w", stdout);
#endif

    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);

    // 여기다가

    long int N, Q; cin >> N >> Q;
    vector<int> haybales;
    for (long int i = 0; i < N; i++) {
        long int tmp; cin >> tmp;
        haybales.push_back(tmp);
    }
    sort(haybales.begin(), haybales.end());  // 오름차순 정렬
    long int e = haybales.size();  // ? 이건 왜적음
    while (Q--) {
        long int i, j; cin >> i >> j;
        //cout << "i: " << i << ", " << "j: " << j << endl; // 
        cout << biSearch(haybales, i, j) << '\n';
    }

    // 코드 작성하기
    return 0;
}
