void BFS() {
    if (!root)
        return;
    Node* tmp = root;
    cout << tmp->value;

    queue<Node*> q;
    q->push(tmp->pLeft);
    q->push(tmp->pRight);

    while (!q.empty()) {
        Node* cur = q.front();
        q.pop();
        if (!cur) {
            cout << " " << cur->value;
            q.push(cur->pLeft);
            q.push(cur->pRight);
        }
    }    
}