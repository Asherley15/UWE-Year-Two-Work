#include <stdio.h>
#include <string.h>

int main()
{
    char str[] = "echo These words should be arguements, not part of the file name";
    char *argv[255];
    char *pointer;

    char *token = strtok_r(str, " ", &pointer);
    printf("File Name: %s\n", token);
    char *filename = token;
    memcpy(filename, token, sizeof(token));
    printf("File Name!!!: %s\n", filename);
    int counter = 0;
    while (token != NULL)
    {
        token = strtok_r(NULL, " ", &pointer);
        argv[counter] = token;
        counter += 1;
    }
    printf("\nThis is how the array looks:\n");
    for (int i = 0; i < counter; i++)
    {
        printf("%d: %s\n", i, argv[i]);
    }
    return 0;
}