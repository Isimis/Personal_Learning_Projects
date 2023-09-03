#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

using namespace std;

const int width = 29;
const int height = 29;

char grid[height][width];

random_device rd;
mt19937 gen(rd());
uniform_int_distribution<int> dist(0, 3);

void initGrid() {
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            grid[i][j] = '#';
        }
    }
}

bool isValid(int x, int y) {
    return x > 0 && x < height && y > 0 && y < width;
}

void recursiveBacktracking(int x, int y) {
    grid[x][y] = ' ';

    int directions[4][2] = {{0, -2}, {0, 2}, {-2, 0}, {2, 0}};
    vector<int> dirs = {0, 1, 2, 3};
    shuffle(dirs.begin(), dirs.end(), gen);

    for (int i = 0; i < 4; i++) {
        int dir = dirs[i];
        int newX = x + directions[dir][0];
        int newY = y + directions[dir][1];

        if (isValid(newX, newY) && grid[newX][newY] == '#') {
            grid[newX][newY] = ' ';
            grid[x + directions[dir][0] / 2][y + directions[dir][1] / 2] = ' ';
            recursiveBacktracking(newX, newY);
        }
    }
}

void printGrid() {
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    initGrid();

    vector<int> handX = {1, 3, 5, 7};
    vector<int> handY = {1, 3, 5, 7};
    shuffle(handX.begin(), handX.end(), gen);
    shuffle(handY.begin(), handY.end(), gen);

    int startX = handX[0];
    int startY = handY[0];

    recursiveBacktracking(startX, startY);
    grid[startX][startY] = 'S';
    grid[height - 2][width - 2] = 'E';

    printGrid();

    return 0;
}
