#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  long long N, count = 0;

  cin >> N;

  for (int i = 1; i <= N; i *= 10) {
    count += N - i + 1;
  }

  cout << count << '\n';

  return 0;
}
