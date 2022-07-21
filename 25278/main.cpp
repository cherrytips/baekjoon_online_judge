#include <iostream>
#include <string>
using namespace std;

int main()
{
  int ocean = 0;
  int oxygen = 0;
  int temperature = -30;

  int n;
  cin >> n;

  for (int i = 0; i <= n; i++)
  {
    string param;
    getline(cin, param);

    for (int i = 0; i < param.length(); i++)
    {
      if (param[i] == ' ')
      {
        string env_condition = param.substr(0, i);
        param.erase(0, i + 2);
        int value = stoi(param);

        if (env_condition.compare("ocean") == 0)
          ocean += value;
        else if (env_condition.compare("oxygen") == 0)
          oxygen += value;
        else
          temperature += value;
      }
    }
  }

  if (ocean >= 9 && oxygen >= 14 && temperature >= 8)
    cout << "liveable";
  else
    cout << "not liveable";

  return 0;
}