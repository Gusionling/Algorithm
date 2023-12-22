#include <iostream>
using namespace std;
#define N 4

float P[4] = { (float)3 / 8, (float)3 / 8, (float)1 / 8, (float)1 / 8 };
float A[6][6];
int R[6][6]; 


void printf(float F[][6]) { //float 배열을 출력해주는 함수
	for (int i = 1; i < N+2; i++) {
		for (int j = 0; j < N+1; j++) {
			cout.width(5);
			cout << F[i][j] << " "; 
		}
		cout << "\n";
	}
}

void printi(int F[][6]) { //int 배열을 출력해주는 함수 
	for (int i = 1; i < N+2; i++) {
		for (int j = 0; j < N+1; j++) {
			cout.width(5);
			cout << F[i][j] <<" ";
		}
		cout << "\n";
	}
}

void optsearchtree(const float P[], float minavg, int R[][6]) {
	
	for (int i = 0; i < N + 2; i++) {
		for (int j = 0; j < N + 2; j++) {
			A[i][j] = 999;
			R[i][j] = 0;
		}
	}
	for (int i = 1; i < N + 1; i++) {
		A[i][i-1] = 0; R[i][i-1] = 0;
	}
	for (int i = 1; i < 5; i++) {
		A[i][i] = P[i-1]; R[i][i] = i; 
	}
	for (int diagonal = 1; diagonal < 4; diagonal++) {
		for (int i = 1; i <= 4 - diagonal; i++) {
			int j = i + diagonal;
			float sum = 0.0; 
			for (int k = i; k <= j; k++) {
				sum = sum + P[k-1];
			}
			for (int k = i; k <= j; k++) {
				
				if (A[i][j] > A[i][k - 1] + A[k + 1][j] + sum) {
					A[i][j] = A[i][k - 1] + A[k + 1][j] + sum;
					R[i][j] = k;
				}
			}
		}
	}
	minavg = A[1][4];
}

int main()
{
	float minavg=999;
	optsearchtree(P, minavg, R);
	cout << "A배열" << endl;
	printf(A);
	cout << "\n";
	cout << "R배열" << endl;
	printi(R);
}