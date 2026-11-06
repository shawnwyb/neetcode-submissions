class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        // multi-source bfs, start from every treasure
        int rows = grid.size();
        int cols = grid[0].size();
        queue<pair<int,int>> q;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 0) {
                    q.push({r, c});
                }
            }
        }

        vector<vector<int>> directions = {
            {1, 0}, {-1, 0}, {0, 1}, {0, -1}
        };

        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();
            for (int i = 0; i < 4; i++) {
                int nr = r + directions[i][0];
                int nc = c + directions[i][1];

                // check if in bounds and traversable
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols &&
                    grid[nr][nc] == 2147483647) {
                        // set distance and push to q
                        grid[nr][nc] = grid[r][c] + 1;
                        q.push({nr, nc});
                }
            }
        }
    }
};
