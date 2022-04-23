
#include "string.h"
#include "expression_string.h"

expressionString_s buildExpressionString(const char* str) {
    expressionString_s rt;

    if (strlen(str) > 128) {
        printf("buildExpressionString(): size of expression larger than buffer!\n");
        exit(0);
    };

    rt.pos = 0;
    strcpy(rt.string, str);

    return rt;
}
