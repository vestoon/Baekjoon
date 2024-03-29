#include <iostream>
#include<vector>
using namespace std;

    int blue = 0, white = 0;
    void Divide(vector<vector<int>>& p) {
        int l = p.size();
        int ab = p[0][0];
        int m = l / 2;
        //cerr << l << " " << ab << " " << m << "\n";
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < l; j++) {
                if (p[i][j] != ab) {  // �ٸ��� �����ϱ� ���� ����
                    vector<vector<int>> cp(m,vector<int>(m,-1));
                    for (int i = 0; i < l; i += m) {
                        for (int j = 0; j < l; j += m) {
                            for (int r = i; r < i + m; r++) {
                                copy(p[r].begin() + j, p[r].begin() + j + m, cp[r-i].begin());
                                //copy(p.begin() + i, p.begin() + i + m, cp.begin()); //
                            }
                            Divide(cp);
                        }
                    }
                    return;
                }
            }
        }
        if (ab)
            blue++;
        else
            white++;
    }


    int main() {
        // ����ٰ�
        int N;
        cin >> N;
        vector<vector<int>> paper;  // ������ �����
        // �����̿� �� ĥ�ϱ�
        for (int i = 0; i < N; i++) {
            paper.push_back(vector<int>(N));
            for (int j = 0; j < N; j++) {
                int tmp;
                cin >> tmp;
                //paper[i].push_back(tmp);
                paper[i][j] = tmp;
            }
        }
        

        /*for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << paper[i][j] << ' ';
            }
            cout << endl;
        }*/



        Divide(paper); //
        cout << white << '\n';
        cout << blue;


        // �ڵ� �ۼ��ϱ�
        return 0;
    }
