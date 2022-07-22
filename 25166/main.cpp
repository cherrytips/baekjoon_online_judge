#include <iostream>
using namespace std;

int main()
{
  int S, M;
  string result = "Impossible";

  cin >> S >> M;

  for (int i = 512; i >= 1; i /= 2)
  {
    if (S == i)
    {
      if (i == 1)
      {
        result = "No thanks";
        break;
      }
    }
    S -= i;
  }

  if ((S % 2 == 0 && M % 2 == 0) || (S % 2 == 1 && M % 2 == 1))
    result = "Thanks";

  cout << result;

  return 0;
}