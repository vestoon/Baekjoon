#include<iostream>
#include<queue>
using namespace std;

int main() {
	int T;
	cin >> T;
	while (T--) { // 캐이스 수만큼 반복
		int N, M, count= 0, printed = -1;
		queue<pair<int,int>> q;  // 큐에 {인덱스, 중요도} 순으로 문서를 저장
	
		cin >>  N >> M;
		for (int i = 0; i < N;i++) {  // 큐에 숫자 넣기
			int inp;
			cin >> inp;
			q.push({ i,inp });
		}

		while (printed != M) {  // 타겟을 찾을 때까지 루프돌려서 큐에서 하나씩 빼기
			int max = 0;  // 최대값 설정
			for (int i = 0; i < q.size(); i++) {  // 최대값을 찾기 위한 반복문
				if (q.front().second > max) {
					max = q.front().second;
				}
				q.push(q.front());
				q.pop();
			}
			//cout << max << endl; //
			while (q.front().second != max) {  // 맨 앞에 최대값이 올 때까지 계속 순환시킴
				q.push(q.front());
				q.pop();
			}
			printed = q.front().first;  // 큐에서 하나 빼고 printed 에 저장
			q.pop();
			count++;
			//cout << "printed: " << printed << endl; //
			//cout << "큐의 앞뒤: " << q.front().first << q.back().first << endl; //
			//cout << "count: " << count << endl << endl; //
		}	
		cout << count << endl;
	}
}