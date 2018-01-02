const SinglyLinkedList = require('./linked_list.js');

class Stack{
    constructor(iterable=[]){
        this.linked_list = new SinglyLinkedList();

        for(var i = 0; i < iterable.length; i++){
            this.push(iterable[i])
        }
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

module.exports = Stack;