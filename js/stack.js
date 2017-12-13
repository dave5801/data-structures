class Node{
    //node class

    constructor(data, next){
        this.data = data;
        this.next = next;
    }
}

class SinglyLinkedList{
    //linked list class

    constructor(head){
        this.head = null;
        this.size = 0;
    }

    push(val){
        //insert new value into linked list

        if(!this.head){
            this.head = new Node(val);
            this.size += 1;
            return;
        }

        var current = this.head;

        while(current.next){
            current = current.next
        }

        current.next = new Node(val);
        this.size +=1;

    }

    pop(){
        //remove head of list

        if(!this.head){
            return;
        }

        var current = this.head;
        this.head = current.next;
        this.size -= 1;
        
        //return "Popped head of list: " + current.data;
        return current.data;

    }

    get_size(){
        //return size of list
        return this.size;
    }

    search(val){
        //return node of with data of val

        var current = this.head;

        while(current.next){

            if(current.data == val){
                return current;
            }

            current = current.next
        }

        return "not found";

    }

    remove(node){
        //remove a node from the list

        node.data = node.next.data;
        node.next = node.next.next;
        this.size -= 1;
    }

    display(){
        //display contents of linked list

        if(!this.head){
            console.log("Empty List");
            return;
        }

        var current = this.head;

        while(current.next){
            console.log("Node: " +current.data);
            current = current.next;

        }
        console.log("Node: " +current.data);
    
    }
}

class Stack{
    constructor(){
        this.linked_list = new SinglyLinkedList();
    }
    size(){
        return this.linked_list.get_size();
    }
    push(val){
        this.linked_list.push(val);
    }
    pop(){
        this.linked_list.pop();
    }
    len(){
        return this.size();
    }
}

stack = new Stack();
stack.push(5);
stack.push(6);
stack.push(7);
console.log(stack.size());