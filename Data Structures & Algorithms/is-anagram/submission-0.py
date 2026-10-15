class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        table = {
            "s": {},
            "t": {}
        }
        # Build the table
        for s_idx, t_idx in zip(s, t):
            if table["s"].get(s_idx):
                table["s"][s_idx] += 1
            else:
                table["s"][s_idx] = 1

            if table["t"].get(t_idx):
                table["t"][t_idx] += 1
            else:
                table["t"][t_idx] = 1

        # Find the matches
        for char in table["s"].keys():
            if char not in table["t"]:
                return False

        for char, val in table["s"].items():
            if table["t"].get(char) != val:
                return False

        return True

        
        