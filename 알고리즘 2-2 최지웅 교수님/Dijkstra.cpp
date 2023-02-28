#include <iostream>
#include <queue>
using namespace std;
#define N 5
queue<int> e;

int W[6][6] = { {0,0,0,0,0,0},{0,0,7,4,6,1},{0,999,0,999,999,999},{0,999,2,0,5,999},{0,999,3,999,0,999},{0,999,999,999,1,0} };
int touch[6] = { 0,0,0,0,0,0 };
int length[6] = { 0,0,0,0,0,0 };

void dijkstra(int n, const int W[6][6]) {

	int vnear;
	for (int i = 1; i <= n; i++) {
		touch[i] = 1;
		length[i] = W[1][i];
	}
	//check each vertex for having shortest path
	for (int j = 1; j < n; j++) {    //n-1번 반복
		int min = 999;
		for (int i = 2; i <= n; i++) {        //length에서 가장 작은 값 찾는 과정
			if (length[i] > 0 && length[i] <= min) {
				min = length[i];
				vnear = i;
			}
		}
		e.push(touch[vnear]); //집합 F를 채우기 위해 큐를 이용
		e.push(vnear);
		
		int index = 1;
		for (int k = 2; k <= n; k++) {
			if (length[vnear] + W[vnear][k] < length[k]) {
				length[k] = length[vnear] + W[vnear][k];
				touch[k] = vnear;
				index = k;
			}
		}
		length[vnear] = -1;
	}
}

int main() {
	
	dijkstra(5, W);
	
	cout << "touch" << endl;
	for (int i = 2; i < 6; i++) {
		cout.width(5);
		cout << touch[i] << " ";
	}cout << "\n";

	cout << "length" << endl;
	for (int i = 2; i < 6; i++) {
		cout.width(5);
		cout << length[i] << " ";
	}cout << "\n";

	cout << "F" << endl;
	for (int i = 2; i <= N; i++)
	{
		cout << "(" << e.front() << ",";
		e.pop();
		cout << e.front() << ") ";
		e.pop();
	}
}