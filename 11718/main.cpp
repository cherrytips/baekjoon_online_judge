#include <iostream>
using namespace std;

int main()
{
  string in;

  while (true)
  {
    getline(cin, in);

    if (cin.eof())
      break;

    cout << in << '\n';
  }

  return 0;
}