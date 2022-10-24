#include <iostream>

using namespace std;

int Solution(int N) {
  int cnt = 0;
  int num = N;

  do {
    num = (num % 10) * 10 + ((num / 10) + (num % 10)) % 10;
    cnt++;
  } while (num != N);

  return cnt;
}

int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int N, result;

  cin >> N;
  result = Solution(N);
  cout << result << endl;

  return 0;
}
