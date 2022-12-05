#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <string>
#include <vector>

int main(void) 
{
    FILE *fp;
    char *line;
    size_t len = 0;
    ssize_t read;
    fp = fopen("input.txt", "r");

    std::vector<std::vector> boxes;

    bool box_part = true;
    bool move_part = false;
    while ((read = getline(&line, &len, fp)) != -1) {
        if (strncmp(line, " 1", 2)) {
            box_part = false;
        } else if (strlen(line) == 0) {
            move_part = true;
        }

        if (box_part) {
            
        } else if (move_part) {
            
        } 
    }

    fclose(fp);
    free(line);
    return 0;
return 456;
}