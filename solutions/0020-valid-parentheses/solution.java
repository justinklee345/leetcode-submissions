class Solution {
    public boolean isValid(String s) {
        Set<String> set = new HashSet<>();
        set.add("()");
        set.add("{}");
        set.add("[]");
        while (true) {
            if (s.length() == 2 && set.contains(s)) {
                return true;
            }
            if (s.length() <= 2 && !set.contains(s)) {
                return false;
            }
            int idx = s.indexOf("()");
            if (idx == -1) {
                idx = s.indexOf("{}");
                if (idx == -1) {
                    idx = s.indexOf("[]");
                    if (idx == -1) {
                        return false;
                    }
                }
            }
            s = s.substring(0, idx) + s.substring(idx + 2, s.length());
        }
    }
}
