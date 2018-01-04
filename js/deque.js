//Double Ended Queue

class Node{
    //node class

    constructor(data=null, next_node=null, prev_node=null){
        this.data = data;
        this.next_node = next_node
        this.prev_node = prev_node
    }
}

class Deque{
    //class for double ended queue

    constructor(){
        this.head= null;
        this.tail = null;
        
    }

    size(){
        /*Get Size of dequeue*/
        let count = 0;
        let current_node = this.head;

        while(current_node){
            count += 1;
            current_node = current_node.next_node;
        }

        return count;
    }

    append(val){
        //Add a node to the tail with a specified value.
        let new_node = new Node(val)
        if(!this.head){
            this.head = new_node;
            this.tail = new_node;
        }else{
            this.tail.next_node = new_node;
            new_node.prev_node = this.tail
            this.tail = new_node
        }

    }

    append_left(val){
        /*Add a node to the head with a specified value.*/

        let new_node = new Node(val)

        if(!this.head){
            this.head = new_node
            this.tail = new_node
        }else{
            this.head.prev_node = new_node
            new_node.next_node = this.head
            this.head = new_node
        }
    }

    pop(){
        /*Remove and returns the tail node of the list.*/

        let popped_node = null;

        try{
            if((this.head) && (this.head == this.tail)){
                popped_node = this.head;
                this.head = null;
            }else{
                popped_node = this.tail;
                this.tail.prev_node.next_node = null;
                this.tail = this.tail.prev_node;
            }

            return popped_node.data
            
        }catch(TypeError){
            return "Cannot Pop from Empty List";
           // console.log("Cannot Pop from Empty List")
        }
    }

    pop_left(){
        /*Remove and returns the head node of the list.*/
        let popped_node = null;

        try{
            if((this.head) && (this.head == this.tail)){
                popped_node = this.head;
                this.head = null;
            }else{
                popped_node = this.head;
                this.head.next_node.prev_node = null;
                this.head = this.head.next_node;
            }

            return popped_node.data

        }catch(TypeError){
            return "Cannot Pop from Empty List";
            //console.log("Cannot Pop from Empty List")
        }

    }

    peek(){
        /*Return value from end of list without removing it.*/
        if(this.head == null){
            return null
        }else{
            return this.tail.data
        }        

    }

    peek_left(){
        /*Return value from front of list without removing it.*/
        if(this.head == null){
            return null
        }else{
            return this.head.data
        }       

    }
    
}

dq = new Deque();
dq.append_left(5)
dq.append_left(6)

dq.pop_left()
dq.pop_left()
dq.pop_left()

dq.append(10)
dq.append_left(15)

var x = dq.peek()
var y = dq.peek_left()
console.log(x + " " +y)
console.log(dq.size());


module.exports = Deque;