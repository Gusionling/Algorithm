#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;

deque<int> result;
deque<int> Deque;

int main() {
	int n;
	cin >> n;
	int count = 0;

	for (int i = 0; i < n; i++) { //for문 말고 while(n--)해도 괜찮
		string str;
		cin >> str;
		if (str == "push_front") {
			int k;
			cin >> k;
			Deque.push_front(k);
			count += 1;
		}
		else if (str == "push_back") {
			int k;
			cin >> k;
			Deque.push_back(k);
			count += 1;
		}
		else if (str == "pop_front") {
			if (Deque.empty()) {
				result.push_back(-1);
			}
			else {
				result.push_back(Deque.front());
				Deque.pop_front();
			}
		}
		else if (str == "pop_back") {
			if (Deque.empty()) {
				result.push_back(-1);
			}
			else {
				result.push_back(Deque.back());
				Deque.pop_back();
			}
		}
		else if (str == "size") {
			result.push_back(Deque.size());
		}
		else if (str == "empty") {
			if (Deque.empty()) {
				result.push_back(1);
			}
			else {
				result.push_back(0);
			}
		}
		else if(str == "back"){
			if (Deque.empty()) {
				result.push_back(-1);
			}
			else {
				result.push_back(Deque.back());
			}
		}
		else {
			if (Deque.empty()) {
				result.push_back(-1);
			}
			else {
				result.push_back(Deque.front());
			}
		}
	}

	for (int i = 0; i < n - count; i++) {
		cout << result[i] << "\n";
	}
}