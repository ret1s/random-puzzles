import java.util.*;

class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
        int x = 0, y = 0, d = 0;
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int maxDistance = 0;
        Set<String> obstacleSet = new HashSet<>();
        for (int[] obstacle : obstacles) {
            obstacleSet.add(obstacle[0] + "," + obstacle[1]);
        }       
        for (int c : commands) {
            if (c == -1) {
                d = (d + 1)%4;
            } else if (c == -2) {
                d = (d + 3)%4;
            } else {
                for (int i = 0; i < c; i++) {
                    int nx = x + directions[d][0];
                    int ny = y + directions[d][1];
                    if (obstacleSet.contains(nx + "," + ny)) {
                        break;
                    }
                    x = nx;
                    y = ny;
                    maxDistance = Math.max(maxDistance, x*x + y*y);
                }
            }
        }
        return maxDistance;
    }
}