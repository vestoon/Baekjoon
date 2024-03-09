#include<iostream>
using namespace std;

double grade_to_score(string g) {
	if (g == "A+")
		return 4.5;
	if (g == "A0")
		return 4.0;
	if (g == "B+")
		return 3.5;
	if (g == "B0")
		return 3.0;
	if (g == "C+")
		return 2.5;
	if (g == "C0")
		return 2.0;
	if (g == "D+")
		return 1.5;
	if (g == "D0")
		return 1.0;
	if (g == "E+")
		return 0.5;
	if (g == "F")
		return 0;
}


int main() {
	double size_sum = 0;
	double score_sum = 0;
	for (int _ = 0; _ < 20; _++) {
		string name; cin >> name;
		double size; cin >> size;
		string grade; cin >> grade;
		if (grade == "P")
			continue;
		size_sum += size;
		score_sum += grade_to_score(grade)*size;
	}
	cout << score_sum / size_sum;
	return 0;
}