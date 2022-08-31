#include <cmath>
#include <iostream>
using namespace std;

bool is_decimal(int num) {
  int sq = sqrt(num);

  for (int i = 2; i <= sq; i++) {
    if (num % i == 0) {
      return false;
    }
  }

  return true;
}

int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  int n = 1;
  bool wrong = true;

  while (n != 0) {
    cin >> n;
    

    if (n == 0) break;

    wrong = true;

    for (int i = 3; i <= n; i += 2) {
      if (is_decimal(i) && is_decimal(n - i)) {
        cout << n << " = " << i << " + " << n - i << '\n';
        wrong = false;
        break;
      }
    }

    if (wrong) cout << "Goldbach's conjecture is wrong." << '\n';
  }

  return 0;
}
