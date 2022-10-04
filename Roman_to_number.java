class Solution {
    public int romanToInt(String s) {
        
        int ans=0;
        for(int i=0;i<s.length();i++)
        {
            char a=s.charAt(i);
            if (a == 'M'){
                if (i != 0 && s.charAt(i-1) == 'C' ){
                    ans += 800;
                } else {
                    ans += 1000;
                }
            } else if (a == 'D'){
                if (i != 0 && s.charAt(i-1) == 'C' ){
                    ans += 300;
                } else {
                    ans += 500;
                }
            } else if (a == 'C'){
                if (i != 0 && s.charAt(i-1) == 'X' ){
                    ans += 80;
                } else {
                    ans += 100;
                }
            } else if (a == 'L'){
                if (i != 0 && s.charAt(i-1) == 'X' ){
                    ans += 30;
                } else {
                    ans += 50;
                }
            } else if (a == 'X'){
                if (i != 0 && s.charAt(i-1) == 'I' ){
                    ans += 8;
                } else {
                    ans += 10;
                }
            } else if (a == 'V'){
                if (i != 0 && s.charAt(i-1) == 'I' ){
                    ans += 3;
                } else {
                    ans += 5;
                }
            } else if (a == 'I'){
                ans += 1;
            }
        }
        return ans;
    }
}
