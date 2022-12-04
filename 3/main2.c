#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int find_item(char *line[3]);
int get_priority(char item);

int main(void) {

        FILE *fp;
        char *line;
        char *lines[3];
        size_t len = 0;
        ssize_t read;
        fp = fopen("input.txt", "r");

        int sum = 0;

        int i = 0;
        while ((read = getline(&line, &len, fp)) != -1) {
                if (i == 3) {
                        sum += find_item(lines);
                        i = 0;
                        for (int h = 0; h < 3; h++) {
                                free(lines[h]);
                        }
                }
                lines[i] = malloc(strlen(line));
                strcpy(lines[i], line);
                printf("line: %s\n", line);
                i++;
        }

        sum += find_item(lines);

        printf("%i\n", sum);

        fclose(fp);
        if (line)
                free(line);
        return 0;
}

int find_item(char *lines[3]) {

        char item;

        for (size_t i = 0; i < strlen(lines[0]); i++) {
                for (size_t j = 0; j < strlen(lines[1]); j++) {
                        for (size_t h = 0; h < strlen(lines[2]); h++) {
                                if (lines[0][i] == lines[1][j] && lines[1][j] == lines[2][h]) {
                                        printf("char: %c\n", lines[0][i]);
                                        item = lines[0][i];
                                        goto stop;
                                }
                        }


                }
        }
        stop:
        printf("break\n");

        return get_priority(item);
}

int get_priority(char item) {
        int ret;
        if (item >= 'a') {
                ret = item - 'a' +1;
        } else {
                ret = item - 'A' + 27;
        } 

        return ret;
}