class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        heap = [(0, 0, 0)]
        min_time = [[float('inf')] * cols for _ in range(rows)]
        min_time[0][0] = 0

        while heap:
            curr_time, row, col = heappop(heap)
            for drow, dcol in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                new_row, new_col = row + drow, col + dcol
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if curr_time + 1 >= min_time[new_row][new_col]:
                        continue
                    else:
                        if (curr_time + 1 - grid[new_row][new_col]) % 2 == 0:
                            min_time[new_row][new_col] = max(curr_time + 1, grid[new_row][new_col])
                        else:
                            min_time[new_row][new_col] = max(curr_time + 1, grid[new_row][new_col] + 1)
                        heappush(heap, (min_time[new_row][new_col], new_row, new_col))
        return min_time[-1][-1]
