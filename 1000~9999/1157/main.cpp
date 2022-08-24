#include <iostream>
#include <cctype>
using namespace std;

int main()
{
  string word;
  int count[26] = {0}; // 알파벳 출현 개수 count
  char result;
  int most = 0; // 가장 많이 사용된 알파벳의 개수

  cin >> word;

  for (int i = 0; i < word.length(); i++)
  {
    word[i] = toupper(word[i]); // 모든 문자 대문자화
    count[(int)word[i] - 65]++; // 출현 개수 증가
  }

  for (int i = 0; i < 26; i++)
  {
    if (count[i] == 0)
      continue;
    else if (most == count[i])
      result = '?';
    else if (most < count[i])
    {
      most = count[i];
      result = (char)(i + 65);
    }
  }

  cout << result << endl;

  return 0;
}