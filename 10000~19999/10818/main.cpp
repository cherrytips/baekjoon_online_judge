#include <algorithm>
#include <iostream>

using namespace std;

int compare(int a, int b) { return a < b; }

int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int N;
  cin >> N;

  int arr[N];
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
  }

  sort(arr, arr + N, compare);

  cout << arr[0] << " " << arr[N - 1] << endl;

  return 0;
}
