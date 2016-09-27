package sub;

import calculator.Calculator;
import org.junit.Test;
import static junit.framework.Assert.assertEquals;


public class SubB {
    @Test
    public void testSubA() throws Exception {

        String res = new Calculator().calculate("9-1");

        assertEquals("= 8.0", res);
    }
}
