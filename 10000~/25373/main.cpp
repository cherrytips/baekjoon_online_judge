#include <iostream>
using namespace std;

int main()
{
  int N;

  cin >> N;

  int result = N / 7;

  while (true)
  {
    int watch = 0;

    for (int i = 0; i < 7; i++)
    {
      if (result + i < 0)
        watch += 0;
      else
        watch += result + i;
    }

    if (watch < N)
      break;

    result--;
  }

  cout << result + 7;

  return 0;
}