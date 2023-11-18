int recursionCount(int& count, Node* root) {
    if (root->pLeft && root->pRight) {
        count++;
        recursionCount(count, root->pLeft);
        recursionCount(count, root->pRight);
        return count;
    }
    if (root->pLeft && !root->pRight) {
        recursionCount(count, root->pLeft);
        return count;
    }
    if (!root->pLeft && root->pRight) {
        recursionCount(count, root->pRight);
        return count;
    }
    return count;
}

int countTwoChildrenNode() {
    if (!root)
        return 0;
    int count = 0;
    recursionCount(count, root);
    return count;
}