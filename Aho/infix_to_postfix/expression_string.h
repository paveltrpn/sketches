
#ifndef __expression_string_h__
#define __expression_string_h__

typedef struct expressionString_s {
    int pos;
    char string[128];
} expressionString_s;

expressionString_s buildExpressionString(const char* str);

#endif