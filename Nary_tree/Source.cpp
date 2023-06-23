#include <iostream> 
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <conio.h> 

#include "tree.h"

int main(void) {
    system("chcp 1251");
    Tree* tree = NULL;
    string temp,counter, value1, number_of_elements1, k1;
    int key, number_of_elements, count = 0, size, value,k;
    while (count != 3) {
        switch (count)
        {
        case 0:
            std::cout << "Введите количество веток дерева" << std::endl;
            getline(cin, value1);
            value = stoi(value1);
            Tree* treee[645];
            for (int i = 0; i < value; i++)
            {
                std::cout << "Введите элементы дерева" << std::endl;
                getline(cin, temp);
                for (size_t i = 0; i < temp.size(); i++)
                {
                    key = stoi(temp);
                    temp.erase(i, 1);
                    tree = InsertNode(tree, key);
                }
                treee[i] = tree;
                tree = RefreshNode(tree);
                std::cout << std::endl;
            }
            std::cout << "Введите 1 для добавления элементов, 2—для удаления, 3—для выхода" << std::endl;
            getline(cin, counter);
            count = stoi(counter);
            break;
        case 1:
            std::cout << "Введите в какую ветку необходимо добавить элементы" << std::endl;
            getline(cin, k1);
            k = stoi(k1);
            std::cout << "Введите добавляемые элементы" << std::endl;
            getline(cin, temp);
            for (int i = 0; i < temp.size(); i++)
            {
                key = stoi(temp);
                temp.erase(i, 1);
                treee[k] = InsertNode(treee[k], key);
            }
            std::cout << "Введите 1 для добавления элементов, 2—для удаления, 3—для выхода" << std::endl;
            getline(cin, counter);
            count = stoi(counter);
            break;
        case 2:
            if (tree == NULL) {
                std::cout << "Дерево является пустым, удалить элементы невозможно" << endl;
            }
            std::cout << "Введите в какой ветке необходимо удалить элементы" << std::endl;
            getline(cin, k1);
            k = stoi(k1);
            std::cout << "Введите элементы которые необходимо удалить" << std::endl;
            getline(cin, temp);
            for (int i = 0; i < temp.size(); i++)
            {
                key = stoi(temp);
                temp.erase(i, 1);
                treee[k] = DeleteNode(treee[k], key);
            }
            std::cout << "Введите 1 для добавления элементов, 2—для удаления, 3—для выхода" << std::endl;
            getline(cin, counter);
            count = stoi(counter);
            break;
        }
    }
    ClearNode(tree);
    return 0;
}