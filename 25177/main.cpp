#include <iostream>
using namespace std;

int main()
{
  int N, M, larger, result = 0;
  cin >> N >> M;

  if (N > M)
    larger = N;
  else
    larger = M;

  int current[larger], old[larger];
  for (int i = 0; i < larger; i++)
    if (i >= N)
      current[i] = 0;
    else
      cin >> current[i];
  for (int i = 0; i < larger; i++)
    if (i >= M)
      old[i] = 0;
    else
      cin >> old[i];

  for (int i = 0; i < larger; i++)
  {
    if (current[i] < old[i] && result < old[i] - current[i])
      result = old[i] - current[i];
  }

  cout << result;

  return 0;
}