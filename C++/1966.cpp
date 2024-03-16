#include<iostream>
#include<queue>
using namespace std;

int main() {
	int T;
	cin >> T;
	while (T--) { // ĳ�̽� ����ŭ �ݺ�
		int N, M, count= 0, printed = -1;
		queue<pair<int,int>> q;  // ť�� {�ε���, �߿䵵} ������ ������ ����
	
		cin >>  N >> M;
		for (int i = 0; i < N;i++) {  // ť�� ���� �ֱ�
			int inp;
			cin >> inp;
			q.push({ i,inp });
		}

		while (printed != M) {  // Ÿ���� ã�� ������ ���������� ť���� �ϳ��� ����
			int max = 0;  // �ִ밪 ����
			for (int i = 0; i < q.size(); i++) {  // �ִ밪�� ã�� ���� �ݺ���
				if (q.front().second > max) {
					max = q.front().second;
				}
				q.push(q.front());
				q.pop();
			}
			//cout << max << endl; //
			while (q.front().second != max) {  // �� �տ� �ִ밪�� �� ������ ��� ��ȯ��Ŵ
				q.push(q.front());
				q.pop();
			}
			printed = q.front().first;  // ť���� �ϳ� ���� printed �� ����
			q.pop();
			count++;
			//cout << "printed: " << printed << endl; //
			//cout << "ť�� �յ�: " << q.front().first << q.back().first << endl; //
			//cout << "count: " << count << endl << endl; //
		}	
		cout << count << endl;
	}
}