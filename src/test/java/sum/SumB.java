package sum;

import calculator.Calculator;
import org.junit.Test;
import static junit.framework.Assert.assertEquals;


public class SumB {
    @Test
    public void testSumB() throws Exception {

        String res1 = new Calculator().calculate("1+0");

        assertEquals("= 1.0", res1);
    }
}
