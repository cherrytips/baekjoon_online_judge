#include <iostream>
using namespace std;

int main()
{
  int a[6];
  int base[] = {1, 1, 2, 2, 2, 8};

  for (int i = 0; i < 6; i++)
  {
    cin >> a[i];
    cout << base[i] - a[i] << ' ';
  }
  cout << endl;

  return 0;
}