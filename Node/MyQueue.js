import Node from "./Node.js";

export default class MyQueue {
    constructor() {
        this.front = null;
        this.rear = null;
    }

    add(value) {
        const newNode = new Node(value);

        if (!this.front) {
            this.front = newNode;
            this.rear = newNode;
        } else {
            this.rear.next = newNode;
            this.rear = newNode;
        }
    }

    remove() {
        if (!this.front) {
            throw new Error("Queue is empty");
        }

        const value = this.front.value;
        this.front = this.front.next;

        if (!this.front) {
            this.rear = null;
        }

        return value;
    }

    peek() {
        if (!this.front) {
            throw new Error("Queue is empty");
        }

        return this.front.value;
    }

    isEmpty() {
        return !this.front;
    }
}
