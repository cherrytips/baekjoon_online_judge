#include <iostream>
using namespace std;

int main()
{
  int N;
  int result = -1;

  cin >> N;

  for (int i = 0; i < N; i++)
  {
    int A, B;

    cin >> A >> B;

    if (A <= B)
    {
      if (result == -1 || result > B)
        result = B;
    }
  }

  cout << result;

  return 0;
}