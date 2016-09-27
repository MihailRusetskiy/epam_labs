package sub;

import calculator.Calculator;
import org.junit.Test;
import static junit.framework.Assert.assertEquals;


public class SubA {
    @Test
    public void testSubA() throws Exception {

        String res = new Calculator().calculate("5-7");

        assertEquals("= -2.0", res);
    }
}
