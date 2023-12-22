#include <iostream>
using namespace std;

const int D[7] = { 5,2,3,4,6,7,8 };
int P[6][6];

void print(int P[][6]) {  //배열을 출력하기 위한 함수 
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 6; j++) {
			cout.width(3);
			cout <<  P[i][j]<< " ";
		}
		cout << "\n";
	}
}

int minmult(int n, const int D[7], int P[][6]) { 
	
	int diagonal;
	int M[6][6];
	int flag[2][1]; 
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < 6; j++) {
			P[i][j] = 0;
			M[i][j] = 999;
		}
	}
	for (int i = 0; i < n; i++) {
		M[i][i] = 0;
	}

	for (diagonal = 0; diagonal <= n - 1; diagonal++) { 
		for (int i = 0; i < n - diagonal; i++) {
			int j = i + diagonal;
			for (int k = i; k <= j - 1; k++) {
				flag[0][0] = M[i][k] + M[k + 1][j] + D[i] * D[k+1] * D[j+1]; // 점화식 이용
				flag[1][0] = k+1;     //flag를 이차원 배열로 선언한 이유 
				if (M[i][j] > flag[0][0]) { // if문을 이용하여 Minimum 구현 
					M[i][j] = flag[0][0];
					P[i][j] = flag[1][0];
				}
			}

		}
	}
	cout << "M배열" << endl;
	print(M);
	return M[0][n - 1];
}


void order(int i, int j, int P[][6]) {
	if (i == j) cout << "A" << i;
	else {
		int k = P[i - 1][j - 1];
		cout << "(";
		order(i, k, P);
		order(k + 1, j, P);
		cout << ")";
	}
}

int main() {
	int min = minmult(6, D, P);
	cout<<"M[1][6] = " << min << endl;
	cout << "P배열" << endl;
	print(P);
	order(1, 6, P);
	cout << "\n";
	return 0;
}