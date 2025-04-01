class Solution:
    def isValid(self, s: str) -> bool:
        o, c = "({[", ")}]"
        st = []
        for i in s:
            if i in o:
                st.append(i)
            else:
                if st and st[-1] == o[c.index(i)]:
                    st.pop()
                else:
                    return False
        return len(st) == 0
        