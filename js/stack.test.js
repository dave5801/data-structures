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

/*
test('test size of stack', () => {
    const s = new Stack([1,2,3,4,5]);
    expect(s.size()).toBe(4);
});

test('test len of stack', () => {
    const s = new Stack();
    expect(s);
});

test('test push to stack', () => {
    const s = new Stack();
    expect(s);
});

test('test pop stack', () => {
    const s = new Stack();
    expect(s);
})


test('test pop empty stack', () => {
    const s = new Stack();
    expect(s);
});


*/