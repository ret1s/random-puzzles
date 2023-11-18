int numOfChild(BSTNode* node) {
    int count = 0;
    if (!node)
        return 0;
    if (node->left) count++;
    if (node->right) count++;
    return count;
}

int singleChild(BSTNode* root) {
    if (!root || numOfChild(root) == 0)
        return 0;
    if (numOfChild(root) == 1) {
        return 1 + singleChild(root->left) + singleChild(root->right);
    }
    if (numOfChild(root) == 2) {
        return singleChild(root->left) + singleChild(root->right);
    }
    return 0;
}