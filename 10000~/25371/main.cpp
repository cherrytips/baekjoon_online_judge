#include <iostream>
#include <string>
using namespace std;

int main()
{
  int n, k;
  string a = "", result = "";
  int b = 0, index = 0;

  cin >> n >> k;

  while (n > 0)
  {
    a = to_string(n % k) + a;
    n /= k;
  }

  for (int i = 0; i < a.length(); i++)
  {
    if (a[i] == '0')
    {
      b += stoi(a.substr(index, i - index));

      while (a[i] == '0' && i < a.length())
        i++;
      if (i >= a.length())
        break;

      index = i;
    }
    if (i == a.length() - 1)
      b += stoi(a.substr(index));
  }

  while (b > 0)
  {
    result = to_string(b % k) + result;
    b /= k;
  }

  cout << result;

  return 0;
}
