#include <iostream>
#include "ctype.h"
using namespace std;

bool isPalindrome(string s)
{
    int first,last;
    first = 0;
    last = s.size() - 1;
    while (first <= last)
    {
        while (!(isalnum(s[first])) && first < last)
        {
            first++;
        }
        while (!(isalnum(s[last])) && first < last)
        {
            last--;
        }
        if (toupper(s[first]) != toupper(s[last]))
        {
            return false;
        }
        first++;
        last--;
    }
    return true;
}

void main()
{
    string s = "A man, a plan, a canal: Panama";
    bool m = isPalindrome(s);
    cout << m << endl;
    system("pause");
}