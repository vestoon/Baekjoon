#include<iostream>
using namespace std;

int arr[100001];
int main() {

    // 여기다가

    int N, M;
    cin >> N >> M;

    for (int i = 1; i < N + 1; i++) {
        int tmp;
        cin >> tmp;
        arr[i] = tmp;
    }
    int l = 1, r = 1;  // 투포인터
    int ans = 0;
    int sum = 0;
    while (!((r > N) && (sum <= M))) {
        sum = 0;
        //cout << "l: " << l << " r: " << r << endl;
        for (int i = l; i < r + 1; i++) {  // l 부터 r 까지의 부분수열의 합을 계산
            sum += arr[i];
        }
        if (sum < M) {
            if (r <= N)
                r++;
        }
        else if (sum > M) {
            l++;
        }
        else if (sum == M) {
            ans++;
            if (r <= N)
                r++;
        }
    }
    cout << ans;

    // 코드 작성하기
    return 0;
}
