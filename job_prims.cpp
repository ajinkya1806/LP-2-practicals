#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <utility>  // For pair
#include <string>

using namespace std;

// --------------------- Prim's Algorithm ---------------------
const int INF = 1e9;

void prims(int n, vector<pair<int, int>> adj[]) {
    vector<int> key(n + 1, INF);
    vector<bool> vis(n + 1, false);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int,int>>> pq;

    key[1] = 0;
    pq.push(make_pair(0, 1)); // {key, node}

    int cost = 0;

    while (!pq.empty()) {
        int u = pq.top().second;
        int wt = pq.top().first;
        pq.pop();

        if (vis[u])
            continue;

        vis[u] = true;
        cost += wt;

        for (size_t i = 0; i < adj[u].size(); ++i) {
            int v = adj[u][i].first;
            int w = adj[u][i].second;
            if (!vis[v] && w < key[v]) {
                key[v] = w;
                pq.push(make_pair(w, v));
            }
        }
    }

    cout << "\nTotal Minimum Cost (MST): " << cost << endl;
}

// --------------------- Job Scheduling ---------------------
class Job {
public:
    string id;
    int deadline;
    int profit;

    Job(string id = "", int deadline = 0, int profit = 0)
        : id(id), deadline(deadline), profit(profit) {}

    bool operator<(const Job& other) const {
        return profit > other.profit;  // Descending profit
    }
};

class Schedule {
private:
    vector<Job> jobs;

public:
    void input() {
        int numJobs;
        cout << "Enter the number of jobs: ";
        cin >> numJobs;
        jobs.resize(numJobs);

        for (int i = 0; i < numJobs; ++i) {
            cout << "Enter job " << (i + 1) << " details:\n";
            cout << "  ID: ";
            cin >> jobs[i].id;
            cout << "  Deadline: ";
            cin >> jobs[i].deadline;
            cout << "  Profit: ";
            cin >> jobs[i].profit;
        }
    }

    void display() {
        cout << "\nID" << setw(10) << "Deadline" << setw(10) << "Profit\n";
        for (size_t i = 0; i < jobs.size(); ++i) {
            cout << jobs[i].id << "\t" << jobs[i].deadline << "\t\t" << jobs[i].profit << endl;
        }
    }

    void order() {
        sort(jobs.begin(), jobs.end());

        int maxDeadline = 0;
        for (size_t i = 0; i < jobs.size(); ++i)
            maxDeadline = max(maxDeadline, jobs[i].deadline);

        vector<bool> slot(maxDeadline, false);
        vector<string> result(maxDeadline, "");

        for (size_t i = 0; i < jobs.size(); ++i) {
            for (int j = jobs[i].deadline - 1; j >= 0; --j) {
                if (!slot[j]) {
                    slot[j] = true;
                    result[j] = jobs[i].id;
                    break;
                }
            }
        }

        cout << "\nJob Scheduling using Greedy Algorithm:\n";
        for (size_t i = 0; i < result.size(); ++i)
            if (!result[i].empty())
                cout << result[i] << " ";
        cout << endl;
    }
};

// --------------------- Main with Menu ---------------------
int main() {
    int choice;

    do {
        cout << "\n===== MENU =====\n";
        cout << "1. Prim's Algorithm (Minimum Spanning Tree)\n";
        cout << "2. Job Scheduling (Greedy)\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
        case 1: {
            int n, m;
            cout << "Enter number of nodes and edges: ";
            cin >> n >> m;
            vector<pair<int, int>> adj[n + 1];

            cout << "Enter edges in format (u v w):\n";
            for (int i = 0; i < m; ++i) {
                int u, v, w;
                cin >> u >> v >> w;
                adj[u].push_back(make_pair(v, w));
                adj[v].push_back(make_pair(u, w));
            }

            prims(n, adj);
            break;
        }
        case 2: {
            Schedule schedule;
            schedule.input();
            schedule.display();
            schedule.order();
            break;
        }
        case 3:
            cout << "Exiting...\n";
            break;
        default:
            cout << "Invalid choice. Try again.\n";
        }
    } while (choice != 3);

    return 0;
}