package mul;

import calculator.Calculator;
import org.junit.Test;
import static junit.framework.Assert.assertEquals;


public class MulC {
    @Test
    public void testMulA() throws Exception {

        String res = new Calculator().calculate("4*1");

        assertEquals("= 4.0", res);
    }
}
