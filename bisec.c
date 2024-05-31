// #include<stdio.h>
// #include<stdlib.h>
// #include<math.h>

// double func(double x) {
//     return x*x*x - 3*x + 1;
// }

// void bisection(double a, double b) {
//     if (func(a) * func(b) >= 0) {
//         printf("Incorrect a and b\n");
//         exit(0);
//     }

//     double c = a;
//     while ((b-a) >= 0.00001) {
//         c = (a+b)/2;

//         if (func(c) == 0.0) {
//             break;
//         }
//         else if (func(c)*func(a) < 0) {
//             b = c;
//         }
//         else {
//             a = c;
//         }
//         printf("a = %lf, b = %lf, f(a) = %lf, f(b) = %lf, x = %lf, f(x) = %lf, ", a, b, func(a), func(b), c, func(c));
//         if(func(c) > 0) {
//             printf("+ve\n");
//         } else {
//             printf("-ve\n");
//         }
//     }
//     printf("The value of root is : %lf\n",c);
// }

// int main() {
//     double a1 =-2, b1 = 2;
//     double a2 =0, b2 = 1;
//     double a3 =1, b3 = 2;
//     printf("Root 1:\n");
//     bisection(a1, b1);
//     printf("Root 2:\n");
//     bisection(a2, b2);
//     printf("Root 3:\n");
//     bisection(a3, b3);

//     return 0;
// }   

#include <stdio.h>

#define MAX 100

int top = -1;
char stack[MAX];

void push(char c) {
    if (top == MAX - 1) {
        printf("Stack overflow\n");
        return;
    }
    top++;
    stack[top] = c;
}

char pop() {
    if (top == -1) {
        printf("Stack underflow\n");
        return '\0';
    }
    char data = stack[top];
    top--;
    return data;
}

int isMatchingPair(char character1, char character2) {
   if (character1 == '(' && character2 == ')')
     return 1;
   else if (character1 == '{' && character2 == '}')
     return 1;
   else if (character1 == '[' && character2 == ']')
     return 1;
   else
     return 0;
}

int isBalanced(char *exp) {
    for (int i = 0; exp[i] != '\0'; i++) {
        if (exp[i] == '(' || exp[i] == '{' || exp[i] == '[') {
            push(exp[i]);
        } else if (exp[i] == ')' || exp[i] == '}' || exp[i] == ']') {
            if (!isMatchingPair(pop(), exp[i])) {
                return 0;
            }
        }
    }
    if (top == -1) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    char exp[MAX];
    printf("Enter an expression: ");
    scanf("%s", exp);
    if (isBalanced(exp)) {
        printf("The expression has balanced parentheses.\n");
    } else {
        printf("The expression does not have balanced parentheses.\n");
    }
    return 0;
}
