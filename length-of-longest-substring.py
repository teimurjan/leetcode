class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        
        left, right = 0, 0
        
        visited = set()
        
        while right < len(s):                                    
            if s[right] in visited:
                result = max(result, len(visited))
                
                while s[right] in visited:
                    visited.remove(s[left])
                    left += 1
            else:
                visited.add(s[right])
                right += 1

        result = max(result, len(visited))
                
        
        return result
            
s = Solution()

s.lengthOfLongestSubstring('abcabcbb')