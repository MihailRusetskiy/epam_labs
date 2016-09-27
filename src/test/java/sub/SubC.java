package sub;

import calculator.Calculator;
import org.junit.Test;
import static junit.framework.Assert.assertEquals;


public class SubC {
    @Test
    public void testSubA() throws Exception {

        String res = new Calculator().calculate("8888888888888888888888888888-111111111111111111111111111111111111111111");

        assertEquals("= -1.1111111111110222E41", res);
    }
}
