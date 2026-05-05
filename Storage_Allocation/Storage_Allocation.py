class StackAllocation:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1

    def push(self, variable):
        if self.top == self.size - 1:
            print("Stack Overflow! Cannot allocate:", variable)
            return

        self.stack.append(variable)
        self.top += 1
        print(f"Allocated {variable} at position {self.top}")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow! Nothing to deallocate")
            return

        removed = self.stack.pop()
        print(f"Deallocated {removed} from position {self.top}")
        self.top -= 1

    def display(self):
        print("\nCurrent Stack:")
        if self.top == -1:
            print("Empty")
        else:
            for i in range(self.top, -1, -1):
                print(f"{i} -> {self.stack[i]}")


# -------- MAIN --------
size = int(input("Enter stack size: "))
stack = StackAllocation(size)

while True:
    print("\n1. Allocate (Push)")
    print("2. Deallocate (Pop)")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        var = input("Enter variable name: ")
        stack.push(var)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.display()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
