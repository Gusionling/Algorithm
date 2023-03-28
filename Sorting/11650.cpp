#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

bool compare(pair<int, int> a, pair<int, int> b) {
	if (a.first == b.first) { return a.second < b.second; }
	else { return a.first < b.first; }
}

int main() {
	int n; 
	cin >> n;
	vector<pair<int, int>> point;


	for (int i = 0; i < n; i++) {
		int x, y; 
		cin >> x >> y;
		point.push_back(make_pair(x, y));
	}
	sort(point.begin(), point.end(), compare);

	for (int i = 0; i < n; i++) {
		cout << point[i].first << " " << point[i].second << "\n";
	}
}