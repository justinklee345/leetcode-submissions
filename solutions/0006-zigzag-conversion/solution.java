class Solution {
    public String convert(String s, int numRows) {
        String toReturn = "";
        
        if (numRows == 1 || s.length() == 1) {
            return s;
        }
        
        String[][] zigzag = new String[numRows][s.length() * 2 / 3];
        
        int count = 0;
        int row = 0;
        int col = 0;
        boolean switchVal = false;
        while (count < s.length()) {          
            
            if (count != 0) {
                if (row == numRows - 1 || row == 0) {
                    switchVal = !switchVal;
                }
            }
            
            zigzag[row][col] = s.substring(count, count + 1);
            
            if (!switchVal) {
                row++;
            } else {
                row--;
                col++;
            }
            
            count++;
        }
        
        for (int i = 0; i < zigzag.length; i++) {
            for (int j = 0; j < zigzag[i].length; j++) {
                if (zigzag[i][j] == null) {
                } else {
                    toReturn += zigzag[i][j];
                }
            }
        }
        return toReturn;
    }
}
