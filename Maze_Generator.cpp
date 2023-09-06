#include <iostream> // output
#include <vector> // vector
#include <random> // rng
#include <algorithm> // shuffle

using namespace std;

// Wielkość labiryntu - będzie działać poprawnie przy wszystkich liczbach nieparzystych
const int width = 29;
const int height = 29;

// Tworzenie labiryntu
char grid[height][width];

// Tworzenie rng
random_device rd; // Źródło losowości
mt19937 gen(rd()); // Wdrożenie algorytmu mt19937
uniform_int_distribution<int> dist(0, 3); // Losuje liczby od 0 do 3 co posłuży do losowania kierunków

// Zapełnienie labiryntu ścianami
void InitGrid() {
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            grid[i][j] = '#';
        }
    }
}

// Sprawdzanie czy pole, które ma zostać zburzona ściana znajduje się w labiryncie
bool IsValid(int x, int y) {
    return x > 0 && x < height && y > 0 && y < width;
}

// Zastosowanie metody Recursive Backtracking do generowanie ścieżek labiryntu
void RecursiveBacktracking(int x, int y) {
    grid[x][y] = ' ';

    int directions[4][2] = {{0, -2}, {0, 2}, {-2, 0}, {2, 0}}; // Wyznaczenie kierunków ruchu generatora
    vector<int> dirs = {0, 1, 2, 3};
    shuffle(dirs.begin(), dirs.end(), gen); // Losowanie kierunków

    // Wyznaczanie ścieżki dla każdego kierunku
    for (int i = 0; i < 4; i++) {
        int dir = dirs[i];
        int newX = x + directions[dir][0];
        int newY = y + directions[dir][1];

        // Generowanie ścieżki
        if (IsValid(newX, newY) && grid[newX][newY] == '#') {
            grid[newX][newY] = ' '; 
            grid[x + directions[dir][0] / 2][y + directions[dir][1] / 2] = ' ';
            RecursiveBacktracking(newX, newY); // Wdrożenie rekursywności w celu generowania dalszej drogi
        }
    }
}

// Rysowanie labiryntu
void PrintGrid() {
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
}

// Program
int main() {
    // Zapełnianie labiryntu
    InitGrid();

    // Losowanie i wyznaczanie początku ścieżki labiryntu
    vector<int> handX = {1, 3, 5, 7};
    vector<int> handY = {1, 3, 5, 7};
    shuffle(handX.begin(), handX.end(), gen);
    shuffle(handY.begin(), handY.end(), gen);
    int startX = handX[0];
    int startY = handY[0];

    // Generowanie ścieżki
    RecursiveBacktracking(startX, startY); 
    grid[startX][startY] = 'S';
    grid[height - 2][width - 2] = 'E';

    // Rysowanie labiryntu
    PrintGrid();

    return 0;
}
