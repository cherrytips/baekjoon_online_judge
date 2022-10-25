#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int N, num, cnt = 0;

  cin >> N;
  int arr[N];

  for (int i = 0; i < N; i++) {
    cin >> arr[i];
  }
  cin >> num;

  for (int i = 0; i < N; i++) {
    if (arr[i] == num) cnt++;
  }

  cout << cnt << endl;

  return 0;
}
