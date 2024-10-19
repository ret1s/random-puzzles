#include <bits/stdc++.h>
using namespace std;

int customAtoi(string s) {
    __int64 res = 0;
    __int64 count = 1;
    bool sign = true;

    for (char c : s) {
        // '-' or '+'
        if (count == 1 && c == '-') {
            sign = false;
            continue;
        }
        if (count == 1 && c == '+')
            continue;
        int val = (int) c - '0';
        // end when reach non-digit character
        if ((val > 9 || val < 0) && c != ' ')
            break;
        // ignore whitespace
        if (c == ' ')
            continue;
        else {
            res += count * val;
            count *= 10;
        }
    }
    // 356 -> 653
    // if (size > 10 && sign)
    //     return INT32_MAX;
    // if (size > 11 && !sign) 
    //     return INT32_MIN;

    // -> result in reversed order
    count /= 10;
    __int64 num = 0;
    while (count > 0) {
        num += count * (res % 10);
        res /= 10;
        count /= 10;
    }

    // out-of-range case
    if (sign == false)
        num = -num;
    
    if (num < INT32_MIN)
        num = INT32_MIN;
    else if (num > INT32_MAX)
        num = INT32_MAX;

    return num;
}

int main() {
    int a = customAtoi("   -0042+42");
    cout << a << endl;
    // 2147483647 -2147483648
    return 0;
} 

// Implement the customAtoi(string s) function, which converts a string to a 32-bit signed integer(similar to C/C++'s atoi function).
// The algorithm for customAtoi(string s) is as follows:

// 1. Read in and ignore any leading whitespace.

// 2. Check if the next character (if not already at the end of the string) is '-' or '+'.Read this character in if it is either.
// This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
// 3. Read in next the characters until the next non-digit character or the end of the input is reached.
// The rest of the string is ignored.

// 4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
// If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).

// 5. If the integer is out of the 32-bit signed integer range, then clamp the integer so that it remains in the range.
// Specifically, integers less than -2^31 should be clamped to -2^31, and integer greater than 2^31 - 1 should be clamped to 2^31 - 1.