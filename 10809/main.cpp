#include <iostream>
#include <array>
using namespace std;

int main()
{
  string S;
  array<char, 26> alph = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
  array<int, 26> result;

  for (int i = 0; i < result.size(); i++)
  {
    result[i] = -1;
  }

  cin >> S;

  for (int i = 0; i < S.length(); i++)
  {
    for (int j = 0; j < alph.size(); j++)
    {
      if (S[i] == alph[j])
      {
        if (result[j] == -1)
          result[j] = i;

        break;
      }
    }
  }

  for (int i = 0; i < result.size(); i++)
  {
    cout << result[i] << ' ';
  }

  return 0;
}