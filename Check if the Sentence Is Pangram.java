class Solution {
    public static boolean isIn(char[] list1,char a){
        for(int i = 0 ; i < list1.length ; i++){
            if ( list1[i] == a ){
                return true;
            } 
        }
        return false;
    }


    public boolean checkIfPangram(String sentence) {
        char[] list1 = new char[26];
        int index = 0 ;
        for (int i = 0; i < sentence.length(); i++){
            // System.out.println(sentence.charAt(i));
            if (!isIn(list1,sentence.charAt(i))){
                list1[index] = sentence.charAt(i);
                index++;
                if(index == 26){
                    return true;
                }
            }
        }
        return false;
    }
}
