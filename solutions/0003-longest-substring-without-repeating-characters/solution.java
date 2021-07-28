class Solution {
    public int lengthOfLongestSubstring(String s) {
        String curr = "";
        int count = 0;
        int highestOverall = 0;
        for (int start = 0; start < s.length(); start++){
            curr = s.substring(start, start+1);
            count = 1;
            if (count > highestOverall){
                highestOverall = count;
            }
            for (int corresponding = start+1; corresponding < s.length(); corresponding++){
                String next = s.substring(corresponding, corresponding+1);
                if (curr.indexOf(next) == -1){
                    curr += next;
                    count = curr.length();
                    if (count > highestOverall){
                        highestOverall = count;
                    }
                } else {
                    if (count > highestOverall){
                        highestOverall = count;
                    }
                    break;
                }
            }
        }
        return highestOverall;
    }
}
