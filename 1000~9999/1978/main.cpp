#include <iostream>
using namespace std;

bool is_decimal(int num) {
  if (num == 1) return false;
  if (num == 2) return true;

  for (int i = 2; i < num; i++) {
    if (num % i == 0) {
      return false;
    } else if (i == num - 1) {
      return true;
    }
  }

  return false;
}

int main(int argc, char const *argv[]) {
  int N, num, result = 0;

  cin >> N;

  for (int i = 0; i < N; i++) {
    cin >> num;
    if (is_decimal(num)) result++;
  }

  cout << result;

  return 0;
}
