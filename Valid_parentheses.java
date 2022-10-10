class Solution {

    public static char[] remove (char[] arr , int a){
        char[] newarr = new char[a];

        for (int i = 0; i < a ; i++){
            newarr[i] = arr[i] ;
        }

        return newarr;
    }

    public static int indexOf (int x ,char[] arr , char a ){
        int ans = 0 ;
        for (int i = 0; i < x; i++){
            if (arr[i] == a ){
                ans = i;
                break;
            }
        }
        return ans;
    }

    public static char[] add ( int x , char[] arr , char a ){
        char[] newarr = new char[x+1] ;

        for (int i = 0; i < x ; i++){
            newarr[i] = arr[i] ;
        }

        newarr[x] = a ;
        return newarr ;
    }

    static boolean contains(char[] list1 , char a){
        for(int i = 0; i< list1.length; i++){
            if (list1[i] == a){
                return true;
            }
        }
        return false;
    }

    public boolean isValid(String s) {
        boolean answer = false ;
        char[] opening = "([{".toCharArray();
        char[] closing = ")]}".toCharArray();
        char[] symbol = new char[0];

        for (int i = 0; i< s.length();i++){
            char a = s.charAt(i);
            int size = symbol.length;
            if (contains(opening , a )){
                symbol = add(size, symbol , a );
            }else if(size == 0 ){
                answer = false;
            } else {
                if (symbol[size - 1] == opening[indexOf(size , closing , a)]){
                    symbol= remove(symbol , size - 1);
                } else {
                    answer = false;
                }
            }
        }
        if (symbol.length == 0){
            answer = true;
        }
        return answer;
    }
}
