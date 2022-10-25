#include <iostream>
#include <string>

using namespace std;

#define MAX (10000)

int not_self[MAX + 10];

void get_next() {
  for (int i = 1; i <= MAX; i++) {
    int temp = i;
    string next = to_string(i);

    for (int i = 0; i < next.length(); i++) {
      temp += (next[i] - '0');
    }

    if (temp > MAX) continue;
    not_self[temp] = 1;
  }
}

int main(int argc, char const *argv[]) {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  get_next();

  for (int i = 1; i <= MAX; i++) {
    if (!not_self[i]) cout << i << endl;
  }

  return 0;
}
