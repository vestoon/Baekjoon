#include<iostream>
using namespace std;
string q1 = "\"����Լ��� ������?\"";
string story = "\"�� ����. �������� �� �� ����⿡ �̼��� ��� ������ ����� ������ �־���.";
string story2 = "���� ������� ��� �� ���ο��� ������ ������ �߰�, ��� �����Ӱ� ����� �־���.";
string story3 = "���� ���� ��κ� �ǾҴٰ� �ϳ�. �׷��� ��� ��, �� ���ο��� �� ���� ã�ƿͼ� ������.\"";
string ans = "\"����Լ��� �ڱ� �ڽ��� ȣ���ϴ� �Լ����\"";
string ans2 = "��� �亯�Ͽ���. ";


void speak(string s, int x) {
	for (int i = 0; i < x; i++) {
		cout << "____";
	}
	cout << s << '\n';
}

void dfs(int a, int b) {
	speak(q1, b);
	;
	if (a != b) {
		speak(story, b);
		speak(story2, b);
		speak(story3, b);
		dfs(a, b + 1);
	}
	else {
		speak(ans, b);
	}
	speak(ans2, b);
}


int main() {
	int n; cin >> n;
	cout << "��� �� ��ǻ�Ͱ��а� �л��� ������ �������� ã�ư� ������. \n";
	
	dfs(n, 0);

	return 0;
}