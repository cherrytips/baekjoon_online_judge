#include <iostream>
using namespace std;

int main()
{
  int A, B;

  cin.tie(NULL);
  ios_base::sync_with_stdio(false);

  while (true)
  {
    cin >> A >> B;

    if (cin.eof() == true)
      break;

    cout << A + B << '\n';
  }

  return 0;
}