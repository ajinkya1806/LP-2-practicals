#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> graph;

// Function to check if a color can be assigned to a node
bool isSafe(int node, int color, const vector<int> &colors) {
    for (int neighbor : graph[node]) {
        if (colors[neighbor] == color)
            return false;
    }
    return true;
}

// Recursive function to color the graph (Backtracking + BnB)
bool colorGraph(int node, int m, int n, vector<int> &colors) {
    if (node == n) return true;

    for (int col = 1; col <= m; col++) {
        if (isSafe(node, col, colors)) {
            colors[node] = col;
            if (colorGraph(node + 1, m, n, colors)) return true;
            colors[node] = 0; // Backtrack
        }
    }
    return false;
}

// Function that checks if coloring is possible and returns result
bool isColorable(int n, int m) {
    vector<int> colors(n, 0);  // 0 = no color
    return colorGraph(0, m, n, colors);
}

int main() {
    int n, e;
    cout << "Enter number of nodes and edges: ";
    cin >> n >> e;

    graph.assign(n, {});  // clear & resize

    cout << "Enter " << e << " edges (0-based indexing):\n";
    for (int i = 0; i < e; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int m;
    cout << "Enter number of colors: ";
    cin >> m;

    if (isColorable(n, m)) {
        cout << "YES: Graph can be colored with " << m << " colors.\n";
    } else {
        cout << "NO: Graph cannot be colored with " << m << " colors.\n";
    }

    return 0;
}
