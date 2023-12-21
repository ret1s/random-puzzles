# Write your MySQL query statement below
SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;
# CHAR_LENGTH() - return number of characters in its argument
# LENGTH() - return the length of string in bytes