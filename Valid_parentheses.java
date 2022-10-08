class Solution {
    public boolean isValid(String s) {
        char[] opening = "([{".toCharArray();
        char[] closing = ")]}".toCharArray();
        char[] symbol = new char[0];

        for (int i = 0; i< s.length();i++){
            char a = s.charAt(i);
            int size = symbol.length;
            if (opening.contains(a)){
                symbol.add(a);
            }else if(size == 0 ){
                return false;
            } else {
                if (symbol[size - 1] == opening[closing.indexOf(a)]){
                    symbol.remove(size - 1);
                } else {
                    return false;
                }
            }
        }
        if (symbol.size() == 0){
            return true;
        }
        
    }
}
