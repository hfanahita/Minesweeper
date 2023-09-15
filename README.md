# Minesweeper
A simple implementation of the Minesweeper game.

This is the final project of the Basic Programming course taught in 2020 at the University of Tehran. The goal of this project is to implement the logic of the famous Minesweeper game without any special GUI.

In the [project_guideline.pdf](https://github.com/hfanahita/Minesweeper/blob/main/project_guideline.pdf) you can find the detailed Persian description of the project given by the instructor of the course.

## Playing the Game
This code will generate a random distribution of the mines on a squared table based on the number of rows and mines given at the start of the game.

![image](https://github.com/hfanahita/Minesweeper/assets/42890482/b776c113-3b88-4e2f-8fa8-fe3fd7f8ce36)

For example, this is the outcome for the above input (It has 2 mines hidden in it.):

![image](https://github.com/hfanahita/Minesweeper/assets/42890482/2ca0d1ba-2c47-40ad-bd1c-6f329b1e2711)


Now, there are 4 commands one can use in this game. The general form of the commands is `[r|f|u|x] <row> <column>`.

**r**: reveals a given cell

**f**: puts a flag on a given cell

**u**: removes a flag on a given cell

**x**: exits the game

For example:

![image](https://github.com/hfanahita/Minesweeper/assets/42890482/dbde1a92-0a54-44c7-ba85-901cbf1b4af3)

Keep in mind that you might get an `Invalid Command!` message which means you have not used the above syntax correctly:

![image](https://github.com/hfanahita/Minesweeper/assets/42890482/0e0cd56b-5f4d-4275-959d-419d51047c03)

Don't forget the spaces! Here the correct command is `r 3 4`.
