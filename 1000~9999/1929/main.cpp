#include <iostream>
#include <cmath>
using namespace std;

bool is_decimal(int num) {
  if (num == 1) return false;
  if (num == 2) return true;

  int sq=sqrt(num);

  for (int i = 2; i <= sq; i++) {
    if (num % i == 0) {
      return false;
    }
  }

  return true;
}

int main(int argc, char const *argv[]) {
  int M, N;

  cin >> M >> N;

  for (int i = M; i <= N; i++) {
    if (is_decimal(i)) cout << i << '\n';
  }

  return 0;
}
