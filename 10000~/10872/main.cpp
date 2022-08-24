#include <iostream>
using namespace std;

int main()
{
  int N;
  int result = 1;

  cin >> N;

  if (N != 0 && N != 1)
  {
    for (int i = 2; i <= N; i++)
    {
      result *= i;
    }
  }

  cout << result;

  return 0;
}