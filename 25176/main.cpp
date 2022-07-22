#include <iostream>
using namespace std;

int clean_count(int n);

int main()
{
  int N;
  cin >> N;

  cout << clean_count(N);

  return 0;
}

int clean_count(int n)
{
  if (n == 1)
    return 1;
  else
    return n * clean_count(n - 1);
}