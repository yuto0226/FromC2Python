// hello_python.c
#include <stdio.h>
int main(int argc, char* argv[]){
    printf("Hello, %s", argc > 1 ? argv[1] : "World");
    return 0;
}