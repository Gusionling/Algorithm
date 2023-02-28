#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;

int capacity = 16;
string* include = new string[5];
string* bestset = new string[5];
int P[5] = {0, 40,30,50,10 }; //P[0]는 루트노드를 표현하기 위해 설정하였다.
int W[5] = {0, 2,5,10,5 }; //W[0]는 루트노드를 표현하기 위해 설정하였다. 
int numbest = 0;
int maxprofit = 0;
int depth = 0;

bool promising(int i, int profit, int weight) {
	int j, k;
	int totweight;
	float bound;

	if (weight >= capacity) return false;
	else {
		j = i + 1;
		bound = (float)profit;
		totweight = weight;

		while (j <= 4 && (totweight + W[j]) <= capacity) {
			totweight = totweight + W[j];
			bound = bound + P[j];
			j++;
		}
		k = j;
		if (k <= 4) {
			bound = bound + (capacity - totweight) * (float)(P[k] / W[k]);
		}
		return (bound > maxprofit);
	}
}

void knapsack(int i, int profit, int weight) {
	if(weight <= capacity && profit > maxprofit) {
		maxprofit = profit;
		numbest = i;
		copy(include, include + 5, bestset);
		cout <<"maxprofit: "<< maxprofit << endl;
	}

	if (promising(i,profit, weight)) {
		
		include[i+1] = "Yes ";
		knapsack(i + 1, profit + P[i + 1], weight + W[i + 1]);
		include[i+1] = "NO ";
		knapsack(i + 1, profit, weight);
	}
}

int main() {

	knapsack(0, 0, 0);
	for (int i = 1; i <= numbest; i++) {
		cout << "w"<< i <<": "<<bestset[i] << setw(3); //setw(x)는 x만큼의 공간을 확보하고 뒤부터 문자수 만큼 출력
	}cout << endl;
	cout << "The answer: $"<<maxprofit << endl;

	delete[] include;
	delete[] bestset;

	return 0;
}