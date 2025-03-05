class Solution:
    def coloredCells(self, n: int) -> int:
        """
        5-March-2025-Count-Total-Number-of-Colored-Cells.py
        """
        if n == 1:
            return 1
        return 4*(n-1) + self.coloredCells(n-1)
