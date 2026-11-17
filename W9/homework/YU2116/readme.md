**项目选择说明**：
选择项目 A 是因为我想深入理解基于数组的队列结构，并重点掌握如何通过取模运算解决普通队列的“假溢出”问题。

 **反思**：
通过 `(rear + 1) % capacity` 的取模运算，使得队尾指针到达数组末尾后能“绕回”到开头，从而复用已被出队操作释放的头部空间，实现物理空间的循环利用，避免了普通顺序队列的假溢出。

**SSH练习**：
Hi YU2116! You've successfully authenticated, but GitHub does not provide shell access.

git@github.com:YU2116/FIP-212.git