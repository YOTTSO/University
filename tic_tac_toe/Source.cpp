#include <iostream>
#include "Game.h"

int main() {
	system("chcp 1251");
	bool win = 0;
	int turn_count = 1, game_variation = 1, x_length = 0, y_length = 0;
	krestiki_noliki match;
	match.init(x_length, y_length);
	x_length = match.GetLength(x_length, y_length);
	y_length = match.GetLength(x_length, y_length);
	match.print(x_length, y_length);
	while (win == 0) {
		switch (game_variation)
		{
		case 1:
			if (turn_count == 1)
			{
				turn_count = match.turn_cross(x_length, y_length);
				match.check_win(&win, x_length, y_length);
				if (win == true)
				{
					break;
				}
			}
			if (turn_count == 2) {
				turn_count = match.turn_zero(x_length, y_length);
				match.check_win(&win, x_length, y_length);
			}
			break;
		case 2:
			cout << "������ ����������� ���������� �� ������ ����������";
			main();
		}
	}
	return 0;
}