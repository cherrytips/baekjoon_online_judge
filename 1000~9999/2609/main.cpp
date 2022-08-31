#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  int n1, n2;
  int ans1, ans2;
  // int cnt1 = 1, cnt2 = 1;

  cin >> n1 >> n2;

  int min_n = min(n1, n2);
  int max_n = max(n1, n2);

  n1 = min_n;
  n2 = max_n;

  for (int i = min_n; i > 0; i--) {  // 최대공약수
    if (n1 % i == 0 && n2 % i == 0) {
      ans1 = i;
      break;
    }
  }

  while (min_n != max_n) {
    if (min_n < max_n) {
      min_n += n1;
    } else {
      max_n += n2;
    }
  }

  ans2 = min_n;

  cout << ans1 << '\n';
  cout << ans2 << '\n';

  return 0;
}
