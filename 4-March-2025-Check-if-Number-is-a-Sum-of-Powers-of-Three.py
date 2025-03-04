class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        4-March-2025-Check-if-Number-is-a-Sum-of-Powers-of-Three.py
        """
        if n%3==2:
            return False
        if n ==1:
            return True
        return self.checkPowersOfThree(n//3)
