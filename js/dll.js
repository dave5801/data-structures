class Node{
    //node class

    constructor(data, next, prev){
        this.data = data;
        this.next = next;
        this.prev = prev;
    }
}

class DLL{

    constructor(){
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    len(){
        return this.size;
    }

    push(val){
       //add new node to front of list.

       var new_node = new Node(val);

       if(!this.head){
            this.head = new_node;
            this.tail = this.head;
            this.size += 1;
            return;
        }else{
            this.head.prev = new_node;
            new_node.next = this.head;
            this.head = new_node;
            this.size += 1; 
        }
    }
    append(val){
        //add new node to end of list.
        var new_node = new Node(val);

        if(!this.head){
            this.head = new Node(val);
            this.tail = this.head;
            this.size += 1;
            return;
        }else{
            this.tail.next = new_node;
            new_node.prev = this.tail;
            this.tail = new_node;
            this.size += 1;   
        }
    }
    pop(){
        //returns and removes head of list.
        try{
            var popped = this.head;
            this.head = this.head.next;
            this.size -= 1;
            return popped;
        }catch(err){
            console.log("Empty List");
        }
    }

    shift(){
        try{
            var shifted = this.tail;
            this.tail = this.tail.prev;
            this.size -= 1;
            return shifted;
        }catch(err){
            console.log("Empty List");
        }
    }
    remove(val){}
}

dll = new DLL();

dll.push(10)
dll.push(5)
dll.append(3)

var x = dll.shift()
console.log("shifted:" +x.data);
console.log("size: " +dll.len())

