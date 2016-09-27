package mul;

import calculator.Calculator;
import org.junit.Test;
import static junit.framework.Assert.assertEquals;


public class MulB {
    @Test
    public void testMulA() throws Exception {

        String res = new Calculator().calculate("5*7");

        assertEquals("= 35.0", res);
    }
}
