#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
  int N;
  double M, result = 0;

  cin >> N;

  double score[N];

  for (int i = 0; i < N; i++)
  {
    cin >> score[i];
  }

  M = *max_element(score, score + N);

  for (int i = 0; i < N; i++)
  {
    result += (score[i] / M * 100);
  }

  cout << result / N;

  return 0;
}