import java.util.*;
import java.lang.*;
import java.io.*;

public final class Doras_Set
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        while(t > 0) {
            t--;
            int l = scanner.nextInt(), r = scanner.nextInt();
            if ((r - l + 1) == 3 && l % 2 == 1) {
                System.out.println(1);
            } else if (l%2 == 1 && r%2 == 1) {
                System.out.println((r - l)/4);
            } else if (l%2 == 0 && r%2 == 0) {
                System.out.println((r - l)/4);
            } else {
                System.out.println((r - l + 1)/4);
            }
        }
        scanner.close();
    }
}
