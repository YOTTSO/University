#include <iostream>
#include <vector>
#include <tuple>
#include <utility>
using namespace std;

int main()
{
    setlocale(LC_ALL, "rus");
    int number_of_arrays, l = 0, i, j, n, m, count, z = 1;
    string p;
    cout << "Введите количество множеств: "; cin >> number_of_arrays;
    vector<int>  size;
    vector<string> temp;
    vector <vector<string>> zxc;
    for (i = 0; i < number_of_arrays; i++)
    {
        cout << "Количество элементов в " << i + 1 << " множестве: "; cin >> n;
        size.push_back(n);
        l++;
    }
    cout << endl << endl << endl;
    l = 0;
    for (i = 0; i < number_of_arrays; i++)
    {
        cout << "\nВведите " << i + 1 << " множество состоящее из " << size[l] << " неповторяющихся элементов!" << endl;
        for (j = 0; j < size[l]; j++)
        {
            cout << j + 1 << "-й элемент множества " << i + 1 << ": "; cin >> p;
            temp.push_back(p);
        }
        zxc.push_back(temp);
        temp.clear();
        l++;
    }
    l = 0;
    cout << endl << endl;
    for (i = 0; i < number_of_arrays; i++)
    {
        cout << i + 1 << " множество: A" << i + 1 << "= {";
        for (j = 0; j < size[l]; j++)
        {
            if (j == size[l] - 1)
            {
                cout << zxc[i][j] << "}" << endl;
                break;
            }
            cout << zxc[i][j] << " , ";
        }
        l++;
        cout << endl << endl;
    }
    cout << endl << "Декартово (прямое) произведение множеств: D={";
    for (i = 0; i < number_of_arrays-1; i++)
    {
        if (i + 1 > number_of_arrays)
        {
            break;
        }
        for (count = z; count < zxc.size(); count++)
        {
            for (m = 0; m < zxc[i].size(); m++)
            {
                for (j = 0; j < zxc[i + count].size(); j++)
                {
                    auto t = make_tuple(zxc[i][m], zxc[i + count][j]);
                    cout << "(" << get<0>(t) << "," << get<1>(t) << ")" << ";";
                }
            }
            z++; 
        }
    }
    cout << "}" << endl << endl;
    cout << endl << "Декартово (обратное) произведение множеств: D={";
    z = 0;
    for (i = number_of_arrays-1; i != 0; i--)
    {
        if (i - 1 < 0)
        {
            break;
        }
        for (count = number_of_arrays-z-1; count != 0; count--)
        {
            for (m = 0; m < zxc[i].size(); m++)
            {
                for (j = 0; j < zxc[i - count].size(); j++)
                {
                    auto t = make_tuple(zxc[i][m], zxc[i - count][j]);
                    cout << "(" << get<0>(t) << "," << get<1>(t) << ")" << ";";
                }
            }
            z++;
        }
    }
    cout << "}" << endl << endl;
    system("pause");
    return 0;
}