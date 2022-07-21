#include <iostream>
using namespace std;

int main()
{
  int size = 5;
  int num[size] = {
      0,
  };
  int result = 0;

  for (int i = 0; i < size; i++)
  {
    cin >> num[i];
    result += (num[i] * num[i]);
  }

  cout << result % 10;

  return 0;
}