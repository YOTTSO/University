#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
int n, x, k = 0, y = 0, p;
vector<int> v1;
vector<int> v2;
vector<int> v3;
vector<int> v4;
vector<int> v5;
int t(int u) {
    int j, m, l, b;
    for (j = 0; j < n; j++) {
        if (v2[u] == v1[j]) {
            v3.push_back(v2[u]);
            l = v3.size();
            for (m = 0; m < l; m++) {
                if (v3[m] == x) {
                    for (b = 0; b < l; b++) {
                        v4.push_back(v3[b]);
                        v5.push_back(v3[b]);
                        v3.clear();
                        return u;
                    }
                }
            }
        }
    }
    return u;
}

int main()
{
    setlocale(LC_ALL, "Russian");
    int o;
    cout << " ¬вод: 0 - из файла, 1 - вручную ";
    cin >> o;
    ifstream in("in.txt");
    if (o == 0) {
        in >> n;
    }
    else {
        cin >> n;
    }

    int i, j;

    int** a = new int* [n];
    for (i = 0; i < n; i++) {
        a[i] = new int[n];
    }

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (o == 0) {
                in >> a[i][j];
            }
            else {
                cin >> a[i][j];
            }
        }
    }

    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (a[i][j] == 1) {
                v1.push_back(i);
                v2.push_back(j);
            }
        }
    }

    int  u;
    for (i = 0; i < n; i++) {
        x = v1[i];
        for (u = 0; u < n; u++) {
            if (v1[i] == v2[u]) {
                p = i;
                t(u);
            }
        }
    }
    int l;
    l = v4.size();

    for (i = 0; i < l; i++) {
        if (v4[0] == v5[i]) {
            v5.erase(v5.begin() + i);
            l = v5.size();
            i--;
        }
    }

    ofstream out("out.txt");
    int gg = 0;
    for (i = 0; i < n; i++) {
        for (j = 0; j < l; j++) {
            if (i != v5[j]) {
                gg++;
            }
        }
        if (gg == l) {
            cout << i << " ";
            out << i << " ";
        }
        gg = 0;
    }

    return 0;
}