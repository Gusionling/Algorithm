#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> parent;
vector<pair<int, pair<int, int>>> W;
vector<pair<int, pair<int, int>>> F;


class nodetype {
public:
	int parent;
	int depth;
	nodetype(int parent, int depth) {
		this->parent = parent;
		this->depth = depth;
	}
};

vector<nodetype> U;


void makeset() {
	for (int i = 0; i < 5; i++) {
		U.push_back(nodetype(i + 1, 0));
	}
}

int find(vector<nodetype>& vector, int i) {
	int j;
	j = i;
	while (vector[j - 1].parent != j) {
		j = vector[j - 1].parent;
	}
	return j;
}

void merge(vector<nodetype>& vector, int p, int q) {
	if (vector[p - 1].depth == vector[q - 1].depth) {
		vector[p - 1].depth += 1;
		vector[q - 1].parent = p;
	}
	else if (vector[p - 1].depth < vector[q - 1].depth) {
		vector[p - 1].parent = q;
	}
	else { vector[q - 1].parent = p; }
}

void kruskal() {
	W.push_back(pair<int, pair<int, int>>(2, pair<int, int>(1, 2)));
	W.push_back(pair<int, pair<int, int>>(5, pair<int, int>(1, 3)));
	W.push_back(pair<int, pair<int, int>>(2, pair<int, int>(1, 4)));
	W.push_back(pair<int, pair<int, int>>(4, pair<int, int>(2, 4)));
	W.push_back(pair<int, pair<int, int>>(1, pair<int, int>(3, 4)));
	W.push_back(pair<int, pair<int, int>>(3, pair<int, int>(3, 5)));
	W.push_back(pair<int, pair<int, int>>(6, pair<int, int>(4, 5)));

	cout << "----정렬 전----" << endl;
	cout << "weight, (a,b)" << endl;
	for (int i = 0; i < 7; i++) {
		cout << W[i].first << " (" << W[i].second.first << ", " << W[i].second.second << ")" << endl;
	}cout << "\n";

	sort(W.begin(), W.end());

	cout << "----정렬 후----" << endl;
	cout << "weight, (a,b)" << endl;
	for (int i = 0; i < 7; i++) {
		cout << W[i].first << " (" << W[i].second.first << ", " << W[i].second.second << ")" << endl;
	}cout << "\n";

	makeset();
	int n = 0; //반복문이 몇번 돌아가는지 재기 위해서 
	int f_index = 0;
	int index = 0;
	while (1) {
		n++;
		cout << n << "번째 반복문 입니다." << endl;
		int i, j;
		i = W[index].second.first;
		j = W[index].second.second;
		int e = W[index].first;

		int p = find(U, i);
		int q = find(U, j);
		cout <<"p:"<<p<<" q:"<< q << endl;
		if (p != q) {
			merge(U, p, q);
			F.push_back(pair<int, pair<int, int>>(e, pair<int, int>(p, q)));
			f_index++;
		}
		cout << "U.parent" << endl;
		for (int t = 0; t < 5; t++) {
			cout << U[t].parent << " ";
		}cout << endl;
		cout << "U.depth" << endl;
		for (int t = 0; t < 5; t++) {
			cout << U[t].depth << " ";
		}cout << endl;
		index++;

		int flag = 0;
		for (int k = 0; k < 5; k++) {
			if (U[k].parent == k + 1) {
				flag++;
			}
		}
		if (flag == 1) {
			break;
		}

	}
	cout << "----F 집합----" << endl;
	cout << "weight, (a,b)" << endl;
	int weightsum = 0;
	for (int l = 0; l < f_index; l++) {
		cout << F[l].first << " (" << F[l].second.first << ", " << F[l].second.second << ")" << endl;
		weightsum += F[l].first;
	}cout << "sum of weight=" << weightsum;
}

int main() {
	kruskal();
	return 0;
}
