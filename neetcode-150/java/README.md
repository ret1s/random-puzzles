# Neetcode 150
Some notes for Neetcode 150 problems.
## 21/08/2024
* Contains Duplicate: use Set, traverse array and put current item if it doesn't exist in the set.
* Valid Anagram: use Array, count total number of character in both input strings, if any character counter value different from zero, return false.
* Two Sum: use HashMap, add items sequentially, check if the diff (target - item) value existed in the HashMap, if yes: return it.
* Group Anagrams: use HashMap, convert each item into key of String and store them in the Map of that key, return values of Map.