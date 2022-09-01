#include <iostream>
using namespace std;

int max_count = 0;

void countMaxColumn(char arr[51][51], int size) {
  for (int i = 0; i < size; i++) {
    int count = 1;
    for (int j = 0; j < size; j++) {
      if (arr[i][j] == arr[i][j + 1])
        count++;
      else {
        if (count > max_count) max_count = count;
        count = 1;
      }
    }
  }
}

void countMaxRow(char arr[51][51], int size) {
  for (int i = 0; i < size; i++) {
    int count = 1;
    for (int j = 0; j < size; j++) {
      if (arr[j][i] == arr[j + 1][i])
        count++;
      else {
        if (count > max_count) max_count = count;
        count = 1;
      }
    }
  }
}

int main(int argc, char const *argv[]) {
  int N = 0;
  char board[51][51];

  cin >> N;

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cin >> board[i][j];
    }
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      swap(board[i][j], board[i][j + 1]);  // column swap

      countMaxColumn(board, N);
      countMaxRow(board, N);

      swap(board[i][j], board[i][j + 1]);  // original
      swap(board[j][i], board[j + 1][i]);  // row swap

      countMaxColumn(board, N);
      countMaxRow(board, N);

      swap(board[j][i], board[j + 1][i]);  // original
    }
  }

  cout << max_count << '\n';

  return 0;
}
