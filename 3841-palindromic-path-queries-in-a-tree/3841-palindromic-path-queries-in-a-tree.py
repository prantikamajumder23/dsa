
class Solution:
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        stack = [(0, -1, False)]

        while stack:
            u, p, exiting = stack.pop()

            if exiting:
                tout[u] = timer
                continue

            parent[u] = u if p == -1 else p
            tin[u] = timer
            timer += 1

            stack.append((u, p, True))

            for v in reversed(graph[u]):
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u, False))

        LOG = n.bit_length()
        up = [parent[:]]

        for j in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        bits = [1 << (ord(c) - 97) for c in s]
        fenwick = [0] * (n + 2)

        def update(i, value):
            i += 1
            while i < len(fenwick):
                fenwick[i] ^= value
                i += i & -i

        def prefix(i):
            result = 0
            while i > 0:
                result ^= fenwick[i]
                i -= i & -i
            return result

        for u in range(n):
            update(tin[u], bits[u])
            update(tout[u], bits[u])

        ans = []

        for q in queries:
            parts = q.split()
            op = parts[0]
            u = int(parts[1])

            if op == "update":
                new_bit = 1 << (ord(parts[2]) - 97)
                delta = bits[u] ^ new_bit

                if delta:
                    update(tin[u], delta)
                    update(tout[u], delta)
                    bits[u] = new_bit
            else:
                v = int(parts[2])
                w = lca(u, v)

                mask = (
                    prefix(tin[u] + 1)
                    ^ prefix(tin[v] + 1)
                    ^ bits[w]
                )

                ans.append((mask & (mask - 1)) == 0)

        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna