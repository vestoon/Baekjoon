#include<iostream>
using namespace std;
string q1 = "\"재귀함수가 뭔가요?\"";
string story = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.";
string story2 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.";
string story3 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"";
string ans = "\"재귀함수는 자기 자신을 호출하는 함수라네\"";
string ans2 = "라고 답변하였지. ";


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
	cout << "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다. \n";
	
	dfs(n, 0);

	return 0;
}