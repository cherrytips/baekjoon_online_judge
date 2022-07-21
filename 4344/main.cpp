#include <iostream>
using namespace std;

int main()
{
  int C;

  cin >> C;

  for (int i = 0; i < C; i++)
  {
    int N;
    cin >> N;

    int score[N], over = 0;
    double avg = 0;
    for (int j = 0; j < N; j++)
    {
      cin >> score[j];
      avg += score[j];
    }
    avg /= N;

    for (int j = 0; j < N; j++)
    {
      if (score[j] > avg)
        over++;
    }

    cout << fixed;
    cout.precision(3);
    cout << (double)over / N * 100 << '%' << endl;
  }

  return 0;
}