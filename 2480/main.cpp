#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
  int a, b, c;
  int count;

  cin >> a >> b >> c;

  if (a == b && a == c)
    cout << 10000 + a * 1000;
  else if (a == b || a == c || b == c)
  {
    if (a == b || a == c)
      cout << 1000 + a * 100;
    else
      cout << 1000 + b * 100;
  }
  else
    cout << max({a, b, c}) * 100;

  return 0;
}