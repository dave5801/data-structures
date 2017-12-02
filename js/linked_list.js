/*
class Node{
    constructor(data, next){
        this.data = data;
        this.next = next;
    }
    foo(){
        console.log("foo-bar")
    }
}


n = new Node()
n.foo()*/

class Node{
    constructor(data, next){
        this.data = data;
        this.next = next;
    }
}

class SinglyLinkedList{
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
        
        return "Popped head of list: " +current.data;

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

    remove(node){}

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

//main
l = new SinglyLinkedList()
l.push(5);
l.push(3);
l.push(2);
l.push(1);

x = l.search(8);
console.log(x);
