#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  int E, S, M, year = 1;
  int esm[3] = {1, 1, 1};
  int exceed[3] = {16, 29, 20};

  cin >> E >> S >> M;

  while (!(esm[0] == E && esm[1] == S && esm[2] == M)) {
    for (int i = 0; i < 3; i++) {
      esm[i]++;
      if (esm[i] == exceed[i]) esm[i] = 1;
    }
    year++;
  }

  cout << year;

  return 0;
}
