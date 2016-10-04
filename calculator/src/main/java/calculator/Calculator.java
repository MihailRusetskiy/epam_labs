package calculator;

import java.util.Scanner;

public class Calculator {

    public static void main (String[] args){
        boolean cont = true;

            try{
                //System.out.println("Enter numbers");
                Scanner in = new Scanner(System.in);
                String s = in.next();
                System.out.println();
                String res = new Calculator().calculate(s);
                System.out.println(res);

            }
            catch (ArithmeticException e) {
                System.out.println("arphmetic error");
            }
            catch (Exception e) {
                System.out.println("error " + e.getMessage());
            }

    }

    public String calculate(String s){

        ParseInput pi = new ParseInput();
        pi.parse(s);
        double x = pi.GetX();
        double y = pi.GetY();
        String operator = pi.GetOperator();

        String res = new Logic().process(operator, x, y);

        return res;
    }

}
