#include <iostream>
using namespace std;

int main()
{
  int T, R, C;

  cin >> T;

  for (int i = 0; i < T; i++)
  {
    cin >> R >> C;
    cout << "Case #" << i + 1 << ":\n";

    for (int j = 0; j <= R * 2; j++)
    {
      for (int k = 0; k <= C * 2; k++)
      {
        if ((j == 0 || j == 1) && (k == 0 || k == 1))
          cout << '.';
        else if (k % 2 == 0)
        {
          if (j % 2 == 0)
            cout << '+';
          else
            cout << '|';
        }
        else
        {
          if (j % 2 == 0)
            cout << '-';
          else
            cout << '.';
        }
      }
      cout << '\n';
    }
  }

  return 0;
}