#include <stdlib.h>
#include <stdio.h>

int match_result(char *line);

int main(void) {

        FILE *fp;
        char *line;
        size_t len = 0;
        ssize_t read;

        int my_score = 0;

        fp = fopen("input.txt", "r");
        if (fp == NULL)
                exit(EXIT_FAILURE);

        int score = 0;
        while ((read = getline(&line, &len, fp)) != -1) {
                score = match_result(line);
                my_score += score;
        }


        fclose(fp);
        if (line)
                free(line);

        printf("%i\n", my_score);

        return 0;
}

int match_result(char *line) {

        int my_score = 0;
        int oponent_score = 0;

        char my_char = line[2]; 
        char oponent_char = line[0];

        switch (line[0]) {
        case 'A':
                oponent_score = 1;
                break;
        case 'B':
                oponent_score = 2;
                break;
        case 'C':
                oponent_score = 3;
                break;
        };

        switch (line[2]) {
        case 'X':
                my_score = 0;
                break;
        case 'Y':
                my_score = 3;
                break;
        case 'Z':
                my_score = 6;
                break;
        };

        if (my_char == 'X') {
                if (oponent_char == 'A') {
                        my_score += 3;
                } else if (oponent_char == 'B') {
                        my_score += 1;
                } else if (oponent_char == 'C') {
                        my_score += 2;
                }
        } else if (my_char == 'Y') {
                if (oponent_char == 'A') {
                        my_score += 1;
                } else if (oponent_char == 'B') {
                        my_score += 2;
                } else if (oponent_char == 'C') {
                        my_score += 3;
                }
        } else if (my_char == 'Z') {
                if (oponent_char == 'A') {
                        my_score += 2;
                } else if (oponent_char == 'B') {
                        my_score += 3;
                } else if (oponent_char == 'C') {
                        my_score += 1;
                }
        }
        return my_score;
}