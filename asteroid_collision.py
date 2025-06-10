class Solution:
    def asteroidCollision(self, asteroids):
        """Simulate asteroid collisions.

        Parameters
        ----------
        asteroids : List[int]
            Each integer represents an asteroid where the absolute value is
            the size and the sign indicates direction (positive for right,
            negative for left).

        Returns
        -------
        List[int]
            The state of the asteroids after all collisions.
        """
        result = []
        for asteroid in asteroids:
            if asteroid >= 0 or not result:
                result.append(asteroid)
            else:
                while result and result[-1] > 0:
                    if result[-1] < -asteroid:
                        result.pop()
                        continue
                    elif result[-1] == -asteroid:
                        result.pop()
                    break
                else:
                    result.append(asteroid)
        return result

if __name__ == "__main__":
    cases = [
        ([5, 10, -5], [5, 10]),
        ([8, -8], []),
        ([10, 2, -5], [10]),
        ([-2, -1, 1, 2], [-2, -1, 1, 2])
    ]
    sol = Solution()
    for asteroids, expected in cases:
        out = sol.asteroidCollision(asteroids)
        print(asteroids, '->', out)
        assert out == expected, f"For {asteroids} expected {expected} got {out}"
    print("All tests passed.")
