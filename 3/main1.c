#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int find_item(char *line);
int get_priority(char item);

int main(void) {

        FILE *fp;
        char *line;
        size_t len = 0;
        ssize_t read;
        fp = fopen("input.txt", "r");

        int sum = 0;

        while ((read = getline(&line, &len, fp)) != -1) {
                sum += find_item(line);
        }

        printf("%i\n", sum);

        fclose(fp);
        if (line)
                free(line);
        return 0;
}

int find_item(char *line) {

        int compartment_size = strlen(line) / 2;
        char item;

        for (size_t i = 0; i < compartment_size; i++) {
                for (size_t j = 0; j < compartment_size; j++) {
                        if (line[i] == line[compartment_size + j]) {
                                item = line[i];
                                break;
                        }
                }
        }

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