package mul;

import calculator.Calculator;
import org.junit.Test;
import static junit.framework.Assert.assertEquals;


public class MulA {
    @Test
    public void testMulA() throws Exception {

        String res = new Calculator().calculate("8/3");

        assertEquals("= 2.6666666666666665", res);
    }
}
