#include <iostream>

using namespace std;

int count(string q) {
  int cnt = 0;
  int score = 0;

  for (int i = 0; i < q.length(); i++) {
    if (q[i] == 'O') {
      score++;
      cnt += score;
    } else {
      score = 0;
    }
  }

  return cnt;
}

int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    string q;
    cin >> q;
    int ans = count(q);
    cout << ans << endl;
  }

  return 0;
}
