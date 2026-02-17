#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int stateCount = 0;

struct State {
    int id;
    char symbol;
    State* next1;
    State* next2;

    State(char sym) {
        id = stateCount++;
        symbol = sym;
        next1 = next2 = NULL;
    }
};

struct NFA {
    State* start;
    State* accept;
};

// Create basic NFA for single character
NFA basicNFA(char symbol) {
    State* s1 = new State(symbol);
    State* s2 = new State('e');   // epsilon

    s1->next1 = s2;

    return {s1, s2};
}

// Concatenation
NFA concatenate(NFA nfa1, NFA nfa2) {
    nfa1.accept->symbol = 'e';
    nfa1.accept->next1 = nfa2.start;
    return {nfa1.start, nfa2.accept};
}

// Union
NFA unionNFA(NFA nfa1, NFA nfa2) {
    State* start = new State('e');
    State* accept = new State('e');

    start->next1 = nfa1.start;
    start->next2 = nfa2.start;

    nfa1.accept->next1 = accept;
    nfa2.accept->next1 = accept;

    return {start, accept};
}

// Kleene Star
NFA kleeneStar(NFA nfa) {
    State* start = new State('e');
    State* accept = new State('e');

    start->next1 = nfa.start;
    start->next2 = accept;

    nfa.accept->next1 = nfa.start;
    nfa.accept->next2 = accept;

    return {start, accept};
}

int precedence(char op) {
    if (op == '*') return 3;
    if (op == '.') return 2;
    if (op == '|') return 1;
    return 0;
}

// Convert Infix to Postfix
string infixToPostfix(string regex) {
    stack<char> s;
    string postfix = "";

    for (char ch : regex) {
        if (isalnum(ch))
            postfix += ch;
        else if (ch == '(')
            s.push(ch);
        else if (ch == ')') {
            while (!s.empty() && s.top() != '(') {
                postfix += s.top();
                s.pop();
            }
            s.pop();
        }
        else {
            while (!s.empty() && precedence(s.top()) >= precedence(ch)) {
                postfix += s.top();
                s.pop();
            }
            s.push(ch);
        }
    }

    while (!s.empty()) {
        postfix += s.top();
        s.pop();
    }

    return postfix;
}

// Build NFA from postfix
NFA buildNFA(string postfix) {
    stack<NFA> s;

    for (char ch : postfix) {
        if (isalnum(ch)) {
            s.push(basicNFA(ch));
        }
        else if (ch == '.') {
            NFA nfa2 = s.top(); s.pop();
            NFA nfa1 = s.top(); s.pop();
            s.push(concatenate(nfa1, nfa2));
        }
        else if (ch == '|') {
            NFA nfa2 = s.top(); s.pop();
            NFA nfa1 = s.top(); s.pop();
            s.push(unionNFA(nfa1, nfa2));
        }
        else if (ch == '*') {
            NFA nfa = s.top(); s.pop();
            s.push(kleeneStar(nfa));
        }
    }

    return s.top();
}

// Display transitions
void display(State* state, vector<int>& visited) {
    if (!state || find(visited.begin(), visited.end(), state->id) != visited.end())
        return;

    visited.push_back(state->id);

    if (state->next1)
        cout << "q" << state->id << " --" << state->symbol
             << "--> q" << state->next1->id << endl;

    if (state->next2)
        cout << "q" << state->id << " --" << state->symbol
             << "--> q" << state->next2->id << endl;

    display(state->next1, visited);
    display(state->next2, visited);
}

int main() {
    string regex;

    cout << "Enter Regular Expression (use . for concatenation): ";
    cin >> regex;

    string postfix = infixToPostfix(regex);
    cout << "Postfix Expression: " << postfix << endl;

    NFA finalNFA = buildNFA(postfix);

    cout << "\nNFA Transitions:\n";
    vector<int> visited;
    display(finalNFA.start, visited);

    cout << "\nStart State: q" << finalNFA.start->id << endl;
    cout << "Accept State: q" << finalNFA.accept->id << endl;

    return 0;
}
