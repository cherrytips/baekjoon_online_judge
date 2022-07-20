#include <iostream>
using namespace std;

int main()
{
  int T;

  cin.tie(NULL);
  ios_base::sync_with_stdio(false);

  cin >> T;

  for (int i = 0; i < T; i++)
  {
    int A, B;

    cin >> A >> B;

    cout << "Case #" << i + 1 << ": " << A + B << "\n";
  }

  return 0;
}