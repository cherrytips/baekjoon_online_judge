#include <iostream>
using namespace std;

int main()
{
  int N, min, max;
  cin >> N;

  int num[N];

  for (int i = 0; i < N; i++) // save numbers to array
  {
    cin >> num[i];
  }

  min = num[0];
  max = num[0];

  for (int i = 0; i < N; i++)
  {
    if (num[i] < min)
    {
      min = num[i];
    }
    if (max < num[i])
    {
      max = num[i];
    }
  }
  cout << min * max << '\n';

  return 0;
}