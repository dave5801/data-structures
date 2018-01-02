class Node{
    //node class

    constructor(data, next, prev){
        this.data = data;
        this.next = next;
        this.prev = prev;
    }
}

class DLL{

    constructor(iterable=[]){
        this.head = null;
        this.tail = null;
        this.size = 0;

        for(var i = 0; i < iterable.length; i++){
            this.push(iterable[i])
        }
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

        if(this.head){
            var shifted = this.tail;
            this.tail = this.tail.prev;
            this.size -= 1;
            return shifted;
        }else{
            return("Empty List")
        }
    }
    remove(val){
        var current = this.head;
        if(current){
             while(current.next){
                if(current.data == val){

                    if(current == this.head){
                        this.head = current.next;
                        this.head.prev = null;
                        this.size -= 1;
                        return;
                    }else if(current == this.tail){
                        this.tail = current.prev;
                        self.tail.next = null;
                        this.size -= 1;
                        return;
                    }else{
                        current.prev.next = current.next;
                        current.next.prev = current.prev;
                        this.size -= 1;
                        return;
                    }

                }else{
                    current = current.next;
                }
            }     
            console.log("Value not in List");
        }else{
            console.log("Empty List");
        }           
    }
}

/*
dll = new DLL();

dll.push(10)
dll.push(5)
dll.append(3)

dll.remove(8);
;*/

module.exports = DLL;

