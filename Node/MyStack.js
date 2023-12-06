import Node from "./Node.js";

export default class MyStack {
    constructor() {
        this.top = null;
    }
        
    push(value) {
        const newTop = new Node(value);
        newTop.next = this.top;
        this.top = newTop;
    }

    pop() {
        if (!this.top) {
            throw new Error("Stack is empty");
        }
        const value = this.top.value;
        this.top = this.top.next;
        return value;
    }

    peek() {
        if (!this.top) {
            throw new Error("Stack is empty");
        }
        return this.top.value;
    }

    isEmpty() {
        return !this.top;
    }
}
