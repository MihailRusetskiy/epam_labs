package dev;

import calculator.Calculator;
import org.junit.Test;
import static junit.framework.Assert.assertEquals;


public class DevC {
    @Test
    public void testSumA() throws Exception {

        String res = new Calculator().calculate("5*7");

        assertEquals("= 35.0", res);
    }
}
