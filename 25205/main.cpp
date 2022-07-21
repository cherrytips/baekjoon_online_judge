#include <iostream>
using namespace std;

int main()
{
  int N, result = 0;
  string s;
  char under[] = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v'};

  cin >> N;
  cin >> s;

  char last = s[N - 1];

  for (auto ch : under)
  {
    if (ch == last)
    {
      result = 1;
      break;
    }
  }

  cout << result;

  return 0;
}