#include <iostream>
using namespace std;

long long dp[1000001];
long long s[1000001];
int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int T;

  for (int i = 1; i <= 1000000; i++) {
    for (int j = 1; i * j <= 1000000; j++) {
      dp[i * j] += i;
    }
  }

  for (int i = 1; i <= 1000000; i++) {
    s[i] = s[i - 1] + dp[i];
  }

  cin >> T;

  while (T--) {
    int N;
    cin >> N;
    cout << s[N] << "\n";
  }

  return 0;
}