#pragma once
#include <cstdlib>
using namespace std;
struct Tree {
    int   child;
    int parent;
    Tree* left;
    Tree* right;
};

Tree* InsertNode(Tree* node, int val);
Tree* DeleteNode(Tree* node, int val);
void  PrintNode(std::ostream& _out, const Tree* node);
Tree*  RefreshNode(Tree* node);
void  ClearNode(Tree* node);