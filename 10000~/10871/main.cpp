#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int N, X;
  cin >> N >> X;

  int arr[N];
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
  }

  for (int i = 0; i < N; i++) {
    if (arr[i] < X) cout << arr[i] << " ";
  }
  cout << endl;

  return 0;
}
