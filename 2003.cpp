#include<iostream>
using namespace std;

int arr[100001];
int main() {

    // ����ٰ�

    int N, M;
    cin >> N >> M;

    for (int i = 1; i < N + 1; i++) {
        int tmp;
        cin >> tmp;
        arr[i] = tmp;
    }
    int l = 1, r = 1;  // ��������
    int ans = 0;
    int sum = 0;
    while (!((r > N) && (sum <= M))) {
        sum = 0;
        //cout << "l: " << l << " r: " << r << endl;
        for (int i = l; i < r + 1; i++) {  // l ���� r ������ �κм����� ���� ���
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

    // �ڵ� �ۼ��ϱ�
    return 0;
}
