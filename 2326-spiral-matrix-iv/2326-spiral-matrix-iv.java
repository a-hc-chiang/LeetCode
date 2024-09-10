/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        int [][] res = new int[m][n];
        if (m==1 && n==1) {
            res[0][0] = head.val; 
            return res; 
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res[i][j] = -1; 
            }
        }

        int currPath = 0; //0 = rightwards, 1 = downwards, 2 = leftwards, 3 = upwards
        int upRows = 0, rightCols = 0, downRows = 0, leftCols = 0; 
        while (head != null) {

            switch (currPath) {
                case 0: //moving right to left 
                    for (int i = 0; i < n - (rightCols + leftCols); i++) {
                        if (head == null) break; 
                        res[upRows][i + leftCols] = head.val; 
                        head = head.next;
                    }
                    upRows++; 
                    break;
                case 1: //moving up to down
                    for (int i = 0; i < m - (downRows + upRows); i++) {
                        if (head == null) break; 

                        res[i + upRows][n - 1 - leftCols] = head.val;
                        head = head.next;
                    }
                    rightCols++;  
                    break; 
                case 2: 
                    for (int i = 0; i < n - (rightCols + leftCols); i++) {
                        if (head == null) break; 

    
                        res[m - downRows - 1][n - 1 - rightCols - i] = head.val;
                        head = head.next; 
                        
                    }
                    downRows++; 
                    break; 
                case 3: 
                    for (int i = 0; i < m - (downRows + upRows); i++) {
                        if (head == null) break; 

                        res[m - i - upRows - 1][leftCols] = head.val;
                        head = head.next;
                    }
                    leftCols++; 
                    break; 
            }
        

            currPath++; 
            if (currPath == 4) {
                currPath = 0; 
            }
        }
        return res; 
    }
}