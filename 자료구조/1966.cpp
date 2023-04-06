#include <iostream>
#include <queue>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	// 우선순위 큐를 <자료형, 구현체, 비교연산자>를 이용하여 선언한다. 
	int n;
	cin >> n; 

	while (n--) {
		int k; 
		int location;
		queue<pair<int, int>> q;
		priority_queue<int> pq;


		int flag = 0;

		cin >> k >> location;

		int pri;
		for (int j = 0; j < k; j++) {
			cin >> pri;
			q.push({ j, pri });
			pq.push(pri);
		}

		while (!q.empty()) {
			int idx = q.front().first;
			int val = q.front().second;
			q.pop();

			if (pq.top() == val) {
				pq.pop();
				flag++;
				if (idx == location) {
					cout << flag << "\n";
					break;
				}
			}
			else
			{
				q.push({ idx, val });
			}
		}

	}
	return 0;
}
