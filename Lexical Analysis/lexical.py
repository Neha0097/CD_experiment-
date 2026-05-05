#include <iostream>
#include <fstream>
#include <cctype>
#include <cstring>
using namespace std;

// Function to check if token is a keyword
bool isKeyword(string str) {
    string keywords[] = {
        "int", "float", "double", "char", "if",
        "else", "while", "for", "return", "void", "main"
    };

    for (int i = 0; i < 11; i++) {
        if (str == keywords[i])
            return true;
    }
    return false;
}

// Function to check if token is an operator
bool isOperator(char ch) {
    char operators[] = {'+', '-', '*', '/', '=', '%'};
    for (int i = 0; i < 6; i++) {
        if (ch == operators[i])
            return true;
    }
    return false;
}

int main() {
    ifstream file("input.txt");
    char ch;
    string buffer = "";

    if (!file) {
        cout << "Error opening file!" << endl;
        return 1;
    }

    while (file.get(ch)) {

        // If alphanumeric → build token
        if (isalnum(ch)) {
            buffer += ch;
        }
        else {

            // If buffer not empty, classify token
            if (!buffer.empty()) {

                if (isKeyword(buffer)) {
                    cout << buffer << " --> Keyword" << endl;
                }
                else if (isdigit(buffer[0])) {
                    cout << buffer << " --> Number" << endl;
                }
                else {
                    cout << buffer << " --> Identifier" << endl;
                }

                buffer.clear();
            }

            // Check operators
            if (isOperator(ch)) {
                cout << ch << " --> Operator" << endl;
            }

            // Check special symbols
            else if (!isspace(ch)) {
                cout << ch << " --> Special Symbol" << endl;
            }
        }
    }

    file.close();
    return 0;
}
