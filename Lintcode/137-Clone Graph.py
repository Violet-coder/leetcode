"""
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors. Nodes are labeled uniquely.
You need to return a deep copied graph, which has the same structure as the original graph, and any changes to the new graph will not have any effect on the original graph.
Example1
Input:
{1,2,4#2,1,4#4,1,2}
Output:
{1,2,4#2,1,4#4,1,2}
Explanation:
1------2
 \     |
  \    |
   \   |
    \  |
      4
"""
"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    """
    首先需要明确图的深拷贝是在做什么，对于一张图而言，它的深拷贝即构建一张与原图结构，值均一样的图，但是其中的节点不再是原来图节点的引用。因此，为了深拷贝出整张图，我们需要知道整张图的结构以及对应节点的值。由于题目只给了我们一个节点的引用，因此为了知道整张图的结构以及对应节点的值，我们需要从给定的节点出发，进行「图的遍历」，并在遍历的过程中完成图的深拷贝。
    为了避免在深拷贝时陷入死循环，我们需要理解图的结构。对于一张无向图，任何给定的无向边都可以表示为两个有向边，即如果节点 A 和节点 B 之间存在无向边，则表示该图具有从节点 A 到节点 B 的有向边和从节点 B 到节点 A 的有向边。
    为了防止多次遍历同一个节点，陷入死循环，我们需要用一种数据结构记录已经被克隆过的节点。
    算法：
    1. 使用一个哈希表 visited 存储所有已被访问和克隆的节点。哈希表中的 key 是原始图中的节点，value 是克隆图中的对应节点。
    2. 将题目给定的节点添加到队列。克隆该节点并存储到哈希表中。
    3. 每次从队列首部取出一个节点，遍历该节点的所有邻接点。如果某个邻接点已被访问，则该邻接点一定在 visited 中，那么从 visited 获得该邻接点，否则创建一个新的节点存储在 visited 中，重复上述操作直到队列为空，则整个图遍历结束。
    """

    def cloneGraph(self, node):
        # write your code here
        if not node:
            return

        root = UndirectedGraphNode(node.label)
        visited = {}
        visited[root.label] = root

        queue = collections.deque([node])

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor.label not in visited:
                    visited[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                visited[cur.label].neighbors.append(visited[neighbor.label])

        return visited[root.label]