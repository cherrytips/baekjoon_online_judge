#include <iostream>
using namespace std;

int main()
{
  long long N, result = 0;

  cin >> N;

  for (int i = 1; i <= N; i++)
  {
    result += (N / i) * i;
  }

  cout << result << '\n';

  return 0;
}