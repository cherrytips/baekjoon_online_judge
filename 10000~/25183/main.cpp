#include <iostream>
using namespace std;

int main()
{
  int N;
  string S, result = "NO";

  cin >> N;
  cin >> S;

  for (int i = 0; i <= N - 5; i++)
  {
    int limit = i + 4;

    for (int j = i; j < limit; j++) // 앞 4개가 다음것과 이웃하는지 확인
    {
      if ((int)S[j + 1] != (int)S[j] - 1 && (int)S[j + 1] != (int)S[j] + 1)
        break;
      if (j == limit - 1)
        result = "YES";
    }

    if (result.compare("YES") == 0) // 당첨이면 loop 탈출
      break;
  }

  cout << result;

  return 0;
}