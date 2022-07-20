#include <iostream>
using namespace std;

int main()
{
  int m, n;
  string n_s;

  cin >> m;
  cin >> n;
  n_s = to_string(n);

  for (int i = n_s.length() - 1; i >= 0; i--)
  {
    int convert = n_s.at(i) - '0';
    cout << m * convert << endl;
  }

  cout << m * n;

  return 0;
}