#include <iostream>
#include <vector>
#include <string>
using namespace std;

//문자열을 뒤집는 함수
string reverse(string str) {
	string str1;
	int n = str.size();
	for (int i = n; i > 0; i--) {
		//for문의 범위를 정의하는데 i ==0이렇게 하니까
		//그냥 for문을 나와버리더라 그래서 인덱스 범위를 수정했다. 
		str1.push_back(str[i-1]);
	}
	return str1;
}

//문자열을 뒤집어서 원래 문자열과 같으면 true반환
bool isPel(int i) {
	string str = to_string(i);
	string rev = reverse(str);
	if (str.compare(rev) == 0) {
		return true;
	}
	else { return false;}
}

int main() {
	vector<string> sol;

	while (1) {
		int n;
		cin >> n;
		if (n != 0) {
			if (isPel(n)) {
				sol.push_back("yes");
			}
			else { sol.push_back("no"); }
		}
		else { break; }
	}
	for (int i = 0; i < sol.size(); i++) {
		cout << sol[i] << "\n";
	}
}