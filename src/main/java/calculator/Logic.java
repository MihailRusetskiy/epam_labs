package calculator;

public class Logic {

    public static String process(String operator, double x, double y){
        String res = new String();

        if (operator.equals("*")){
            res = "= " + (x * y);
        }
        if (operator.equals("/")){
            res = "= " + (x / y);
        }
        if (operator.equals("+")){
            res = "= " + (x + y);
        }
        if (operator.equals("-")){
            res = "= " + (x - y);
        }

        return res;
    }
}