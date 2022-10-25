#include <iostream>

using namespace std;

int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int arr[10];
  int max = 0, max_index;

  for (int i = 1; i <= 9; i++) {
    cin >> arr[i];
    if (arr[i] > max) {
      max = arr[i];
      max_index = i;
    }
  }

  cout << max << endl;
  cout << max_index << endl;

  return 0;
}
