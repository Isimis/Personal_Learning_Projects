#include <iostream> //io
#include <random>  // rng
using namespace std;

// Utworzenie mapy gry
char map[4][4] = {
    {'/', '1', '2', '3'},
    {'1', '#', '#', '#'},
    {'2', '#', '#', '#'},
    {'3', '#', '#', '#'}
};

// Przygotowanie potrzebnych wartości
int row = 0, column = 0;
int score[2] = { 0, 0 };

void start_game();

// Wyświetlanie gry
void map_open() {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cout << map[i][j] << " ";
        }
        cout << endl;
    }
}

// Wyświetlanie remisu
void draw() {
    cout << "It's a draw. No one won." << endl;
    map_open();
    cout << endl << endl;
    start_game();
}

// Sprzewdzenie czy gracz wygrał
bool check_player_line(int x1, int y1, int x2, int y2, int x3, int y3) {
    return (map[x1][y1] == 'X' && (map[x1][y1] == map[x2][y2] && map[x2][y2] == map[x3][y3]));
}

bool win_check_player() {
    if (check_player_line(1, 1, 1, 2, 1, 3) ||
        check_player_line(2, 1, 2, 2, 2, 3) ||
        check_player_line(3, 1, 3, 2, 3, 3) ||
        check_player_line(1, 1, 2, 1, 3, 1) ||
        check_player_line(1, 2, 2, 2, 3, 2) ||
        check_player_line(1, 3, 2, 3, 3, 3) ||
        check_player_line(1, 1, 2, 2, 3, 3) ||
        check_player_line(1, 1, 2, 2, 3, 1)) {
        return true;
    }
    else {
        return false;
    }
}

// Sprawdzenie czy przeciwnik wygrał
bool check_enemy_line(int x1, int y1, int x2, int y2, int x3, int y3) {
    return (map[x1][y1] == 'O' && (map[x1][y1] == map[x2][y2] && map[x2][y2] == map[x3][y3]));
}

bool win_check_enemy() {
    if (check_enemy_line(1, 1, 1, 2, 1, 3) ||
        check_enemy_line(2, 1, 2, 2, 2, 3) ||
        check_enemy_line(3, 1, 3, 2, 3, 3) ||
        check_enemy_line(1, 1, 2, 1, 3, 1) ||
        check_enemy_line(1, 2, 2, 2, 3, 2) ||
        check_enemy_line(1, 3, 2, 3, 3, 3) ||
        check_enemy_line(1, 1, 2, 2, 3, 3) ||
        check_enemy_line(1, 1, 2, 2, 3, 1)) {
        return true;
    }
    else {
        return false;
    }
}

// Losowanie ruchu przeciwnika
void roll(int random, int random2) {
    if (map[random][random2] == '#') {
        (map[random][random2] = 'O');
    }
    else
    {
        random = 1 + (rand() % 3);
        random2 = 1 + (rand() % 3);
        roll(random, random2);
    }
}

void player_move();

// Ruch przeciwnika
void enemy_move() {
    srand((unsigned)time(NULL));
    int random = 1 + (rand() % 3);
    int random2 = 1 + (rand() % 3);

    cout << endl << "Enemy's move:" << endl;
    roll(random, random2);
    map_open();
    cout << endl;
    if (win_check_enemy()) {
        cout << "You lost!\n\n";
        score[1]++;
        start_game();
    }
    else if (map[1][1] != '#' && map[1][2] != '#' && map[1][3] != '#' &&
        map[2][1] != '#' && map[2][2] != '#' && map[2][3] != '#' &&
        map[3][1] != '#' && map[3][2] != '#' && map[3][3] != '#') {
        draw();
    }
    player_move();
}

// Ruch gracza
void player_move() {
        cout << endl << "Where do you want to put a mark?\nChoose a column (1/2/3):\n";
        if (!(cin >> column)) {
            cout << "Choose correct value!\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            player_move();
            return;
        }
        else if (column > 3 || column < 1) {
            cout << "Choose correct value!\n";
            player_move();
            return;
        }
        
        cout << "Choose a row (1/2/3):\n";
        if (!(cin >> row)) {
            cout << "Choose correct value!\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), 'n');
            player_move();
            return;
        }
        else if (row > 3 || row < 1) {
            cout << "Choose correct value!\n";
            player_move();
            return;
        }

    if (map[row][column] == 'O') {
        cout << "The enemy has already placed a mark on this square!\nChoose correct squere!\n";
        player_move();
    }
    else if (map[row][column] == 'X') {
        cout << "You have already placed a mark on this square!\nChoose correct squere!\n";
        player_move();
    }
    else if (map[row][column] == '#') {
        (map[row][column] = 'X');
        cout << endl;
        map_open();
        cout << endl;
        if (win_check_player()) {
            cout << "Congratulation! You won!\n\n";
            score[0]++;
            start_game();
        }
        else if (map[1][1] != '#' && map[1][2] != '#' && map[1][3] != '#' &&
            map[2][1] != '#' && map[2][2] != '#' && map[2][3] != '#' &&
            map[3][1] != '#' && map[3][2] != '#' && map[3][3] != '#') {
            draw();
        }
        enemy_move();
    }
    else {
        cout << "Choose correct values!\n";
        player_move();
    }
}

// Sprzątenie po rundzie
void map_cleaner() {
    map[1][1] = '#';
    map[1][2] = '#';
    map[1][3] = '#';
    map[2][1] = '#';
    map[2][2] = '#';
    map[2][3] = '#';
    map[3][1] = '#';
    map[3][2] = '#';
    map[3][3] = '#';
}

// Schemat gry
void start_game() {
    cout << "Welcome in Tic Tac Toe.\n";
    cout << "Actual score: " << score[0] << ":" << score[1] << endl;
    cout << "You start!\n\n";
    map_cleaner();
    map_open();
    player_move();
}

// Program
int main() {
    start_game();
    return 0;
}
