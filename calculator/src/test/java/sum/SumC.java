package sum;

import calculator.Calculator;
import org.junit.Test;
import static junit.framework.Assert.assertEquals;


public class SumC {
    @Test
    public void testSumC() throws Exception {

        String res2 = new Calculator().calculate("5+5555555");

        assertEquals("= 5555560.0", res2);
    }
}
