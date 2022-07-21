#include <iostream>
#include <algorithm>
using namespace std;

bool compare(int a, int b)
{
  return a > b;
}

int main()
{
  int N, k;
  cin >> N >> k;

  int score[N];
  for (int i = 0; i < N; i++)
  {
    cin >> score[i];
  }
  sort(score, score + N, compare);

  cout << score[k - 1];

  return 0;
}