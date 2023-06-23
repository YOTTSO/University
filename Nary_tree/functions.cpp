#include <iostream> 
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <conio.h>
#include "tree.h"
using namespace std;
Tree* DeleteNode(Tree* node, int val) {

    if (node == NULL)
        return node;

    if (val == node->child) {

        Tree* tmp;
        if (node->right == NULL)
            tmp = node->left;
        else {

            Tree* ptr = node->right;
            if (ptr->left == NULL) {
                ptr->left = node->left;
                tmp = ptr;
            }
            else {

                Tree* pmin = ptr->left;
                while (pmin->left != NULL) {
                    ptr = pmin;
                    pmin = ptr->left;
                }
                ptr->left = pmin->right;
                pmin->left = node->left;
                pmin->right = node->right;
                tmp = pmin;
            }
        }

        delete node;
        return tmp;
    }
    else if (val < node->child)
        node->left = DeleteNode(node->left, val);
    else
        node->right = DeleteNode(node->right, val);
    return node;
}

Tree* InsertNode(Tree* node, int val) {

    if (node == NULL) {
        node = new (std::nothrow) Tree();
        if (node != NULL) {
            node->child = val;
            node->left = node->right = NULL;
        }
        return node;
    }

    if (val < node->child)
        node->left = InsertNode(node->left, val);
    else
        node->right = InsertNode(node->right, val);
    return node;
}
void PrintNode(std::ostream& _out, const Tree* node) {
    if (node != NULL) {
        if (node->left != NULL)
            PrintNode(_out, node->left);

        _out << node->child << ' ';

        if (node->right != NULL)
            PrintNode(_out, node->right);
    }
}
Tree* RefreshNode(Tree* node) {
    if (node != NULL) {
        if (node->left != NULL)
            RefreshNode(node->left);
        if (node->right != NULL)
            RefreshNode(node->right);
        node = NULL;
    }
    return node;
}
void ClearNode(Tree* node) {
    if (node != NULL) {
        if (node->left != NULL)
            ClearNode(node->left);
        if (node->right != NULL)
            ClearNode(node->right);
        delete node;
    }
}