/*Test class for Stack.*/

/*requirements*/
const Stack = require('./stack.js');

/*Tests*/

test('test create new stack', () => {
    const s = new Stack();
    expect(s);
});


test('test size of stack empty', () => {
    const s = new Stack([]);
    expect(s.size()).toBe(0);
});


test('test size of stack', () => {
    const s = new Stack([1,2,3,4,5]);
    expect(s.size()).toBe(5);
});

test('test len of stack empty', () => {
    const s = new Stack([]);
    expect(s.len()).toBe(0);
});

test('test len of stack', () => {
    const s = new Stack([1,2,3,4,5]);
    expect(s.len()).toBe(5);
});

test('test push to stack', () => {
    const s = new Stack([1,2,3,4,5]);
    s.push(10)
    s.push(12)
    s.push(15)
    expect(s.len()).toBe(8);
});

test('test push to empty stack', () => {
    const s = new Stack([]);
    s.push(10)
    s.push(12)
    s.push(15)
    expect(s.len()).toBe(3);
});

test('test pop from stack', () => {
    const s = new Stack([1,2,3,4,5]);
    s.pop()
    s.pop()
    expect(s.len()).toBe(3);
});

test('test pop empty stack', () => {
    const s = new Stack();
    s.pop()
    expect(s.len()).toBe(0);
});
