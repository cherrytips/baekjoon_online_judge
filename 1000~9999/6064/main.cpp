#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  ios::sync_with_stdio(false);  // timeout fix
  cin.tie(NULL);
  cout.tie(NULL);

  int T, M, N, x, y;

  cin >> T;

  for (int i = 0; i < T; i++) {
    cin >> M >> N >> x >> y;

    bool check = false;

    x--;
    y--;

    for (int i = x; i < M * N; i += M) {  // i = count
      if (i % N == y) {
        cout << i + 1 << '\n';
        check = true;
        break;
      }
    }
    if (!check) cout << -1 << '\n';
  }

  return 0;
}
