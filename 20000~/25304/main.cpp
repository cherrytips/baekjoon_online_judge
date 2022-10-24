#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int X, N, sum = 0, cost, cnt;

  cin >> X;
  cin >> N;

  for (int i = 0; i < N; i++) {
    cin >> cost >> cnt;
    sum += (cost * cnt);
  }

  if (X == sum)
    cout << "Yes" << endl;
  else
    cout << "No" << endl;

  return 0;
}
