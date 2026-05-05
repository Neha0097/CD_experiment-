#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;

int main() {

    int n, t;
    cout << "Enter number of NFA states: ";
    cin >> n;

    cout << "Enter number of transitions: ";
    cin >> t;

    map<pair<int, char>, set<int>> nfa;
    set<char> symbols;

    cout << "Enter transitions (from to symbol, use e for epsilon):\n";
    for (int i = 0; i < t; i++) {
        int from, to;
        char sym;
        cin >> from >> to >> sym;
        nfa[{from, sym}].insert(to);
        if (sym != 'e')
            symbols.insert(sym);
    }

    int startState;
    cout << "Enter start state: ";
    cin >> startState;

    set<int> finalStates;
    int f;
    cout << "Enter number of final states: ";
    cin >> f;

    cout << "Enter final states: ";
    for (int i = 0; i < f; i++) {
        int x;
        cin >> x;
        finalStates.insert(x);
    }

    // Function for epsilon closure
    auto epsilonClosure = [&](set<int> states) {
        stack<int> st;
        for (int s : states)
            st.push(s);

        set<int> closure = states;

        while (!st.empty()) {
            int state = st.top();
            st.pop();

            for (int next : nfa[{state, 'e'}]) {
                if (closure.find(next) == closure.end()) {
                    closure.insert(next);
                    st.push(next);
                }
            }
        }
        return closure;
    };

    map<set<int>, int> dfaStates;
    vector<map<char, set<int>>> dfa;
    queue<set<int>> q;

    set<int> startClosure = epsilonClosure({startState});
    dfaStates[startClosure] = 0;
    q.push(startClosure);

    int dfaStateCount = 0;

    while (!q.empty()) {
        set<int> current = q.front();
        q.pop();

        map<char, set<int>> transitions;

        for (char sym : symbols) {
            set<int> moveSet;

            for (int state : current) {
                for (int next : nfa[{state, sym}])
                    moveSet.insert(next);
            }

            set<int> closure = epsilonClosure(moveSet);

            if (!closure.empty()) {
                if (dfaStates.find(closure) == dfaStates.end()) {
                    dfaStates[closure] = ++dfaStateCount;
                    q.push(closure);
                }
                transitions[sym] = closure;
            }
        }

        dfa.push_back(transitions);
    }

    cout << "\nDFA Transition Table:\n";
    for (auto &state : dfaStates) {
        cout << "D" << state.second << " = { ";
        for (int s : state.first)
            cout << s << " ";
        cout << "}\n";
    }

    cout << "\nTransitions:\n";
    for (auto &state : dfaStates) {
        int from = state.second;
        for (char sym : symbols) {
            if (dfa[state.second].count(sym)) {
                set<int> toSet = dfa[state.second][sym];
                cout << "D" << from << " --" << sym << "--> D"
                     << dfaStates[toSet] << endl;
            }
        }
    }

    cout << "\nDFA Final States:\n";
    for (auto &state : dfaStates) {
        for (int s : state.first) {
            if (finalStates.count(s)) {
                cout << "D" << state.second << " ";
                break;
            }
        }
    }

    return 0;
}
