#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
#include <set>
using namespace std;

// Adjacency list representation
unordered_map<string, vector<string>> adj;

// Function to create graph
void createGraph() {
    adj.clear();
    int edges;
    cout << "Enter number of edges: ";
    cin >> edges;
    for (int i = 0; i < edges; i++) {
        string u, v;
        cout << "Enter edge (u v): ";
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u); // Remove this line for directed graph
    }
}

// Recursive DFS
void dfsRecursive(string node, set<string>& visited) {
    visited.insert(node);
    cout << node << " ";
    for (auto& neighbor : adj[node]) {
        if (visited.find(neighbor) == visited.end()) {
            dfsRecursive(neighbor, visited);
        }
    }
}

// Recursive BFS helper
void bfsRecursive(queue<string>& q, set<string>& visited) {
    if (q.empty()) return;
    string node = q.front(); q.pop();
    cout << node << " ";
    for (auto& neighbor : adj[node]) {
        if (visited.find(neighbor) == visited.end()) {
            visited.insert(neighbor);
            q.push(neighbor);
        }
    }
    bfsRecursive(q, visited);
}

// Print adjacency list
void printAdjList() {
    cout << "\nAdjacency List:\n";
    for (auto& pair : adj) {
        cout << pair.first << " -> ";
        for (auto& neighbor : pair.second)
            cout << neighbor << " ";
        cout << endl;
    }
}

// Main menu
int main() {
    int choice;
    do {
        cout << "\n--- Graph Menu ---\n";
        cout << "1. Create Graph\n";
        cout << "2. Print Adjacency List\n";
        cout << "3. DFS (Recursive)\n";
        cout << "4. BFS (Recursive)\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        string start;
        switch (choice) {
            case 1:
                createGraph();
                break;
            case 2:
                printAdjList();
                break;
            case 3:
                cout << "Enter starting node for DFS: ";
                cin >> start;
                {
                    set<string> visited;
                    cout << "DFS Traversal: ";
                    dfsRecursive(start, visited);
                    cout << endl;
                }
                break;
            case 4:
                cout << "Enter starting node for BFS: ";
                cin >> start;
                {
                    set<string> visited;
                    queue<string> q;
                    q.push(start);
                    visited.insert(start);
                    cout << "BFS Traversal: ";
                    bfsRecursive(q, visited);
                    cout << endl;
                }
                break;
            case 5:
                cout << "Exiting program.\n";
                break;
            default:
                cout << "Invalid choice.\n";
        }
    } while (choice != 5);

    return 0;
}
