#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  int height[9] = {};
  int sum = 0;
  int found = false;

  for (int i = 0; i < 9; i++) {
    cin >> height[i];
    sum += height[i];
  }
  sort(height, height + 9);

  for (int i = 0; i < 8; i++) {
    for (int j = i + 1; j < 9; j++) {
      if ((sum - height[i] - height[j]) == 100) {
        height[i] = -1;
        height[j] = -1;
        found = true;
        break;
      }
    }

    if (found) break;
  }

  for (int i = 0; i < 9; i++) {
    if (height[i] != -1) {
      cout << height[i] << '\n';
    }
  }

  return 0;
}
