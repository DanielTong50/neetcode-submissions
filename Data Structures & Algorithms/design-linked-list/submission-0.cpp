class MyLinkedList {
public:

    struct Node{
        int val;
        Node* next;
        Node(int nval, Node* nx=nullptr):val(nval), next(nx){};
        Node(): val(0), next(nullptr){};
    };

    Node* head;
    int size;

    MyLinkedList() {
        head = nullptr;
        size = 0;
    }

    
    int get(int index) {
        if (index < 0 || index >= size) return -1;
        Node* curr = head;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
        }
        return curr->val;
    }
    
    void addAtHead(int val) {
        Node* temp = new Node(val);
        temp->next = head;
        head = temp;
        size++;
    }
    
    void addAtTail(int val) {
        if (size == 0) {
            addAtHead(val);
            return;
        }
        Node* curr = head;
        while (curr->next != nullptr){
            curr = curr->next;
        }
        curr->next = new Node(val);
        size++;
    }
    
    void addAtIndex(int index, int val) {
        if (index > size) return;
        if (index <= 0) {
            addAtHead(val);
            return;
        }
        Node* curr = head;
        for (int i = 0; i < index - 1; i++) {
            curr = curr->next;
        }
        Node* temp = new Node(val);
        temp->next = curr->next;
        curr->next = temp;
        size++;
    }
    
    void deleteAtIndex(int index) {
        if (index < 0 || index >= size) return;
        if (index == 0) {
            Node* temp = head;
            head = head->next;
            delete temp;
        } else {
            Node* curr = head;
            for (int i = 0; i < index - 1; i++) {
                curr = curr->next;
            }
            Node* toDelete = curr->next;
            curr->next = curr->next->next;
            delete toDelete;
        }
        size--;
    }
};