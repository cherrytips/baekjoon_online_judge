#include <iostream>

using namespace std;

#define N (42)

int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int cnt = 0;
  int rest[N] = {0};

  for (int i = 0; i < 10; i++) {
    int temp;
    cin >> temp;
    rest[temp % N] = 1;
  }

  for (int i = 0; i < N; i++) {
    if (rest[i]) cnt++;
  }

  cout << cnt << endl;

  return 0;
}
