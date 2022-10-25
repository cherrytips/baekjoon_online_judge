#include <iostream>

using namespace std;

#define N (31)

int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int submit[N] = {0};

  for (int i = 0; i < 28; i++) {
    int temp;
    cin >> temp;
    submit[temp] = 1;
  }

  for (int i = 1; i < N; i++) {
    if (submit[i] == 0) cout << i << endl;
  }

  return 0;
}
