package dev;

import calculator.Calculator;
import org.junit.Test;
import static junit.framework.Assert.assertEquals;


public class DevA {
    @Test
    public void testDevA() throws Exception {

        String res = new Calculator().calculate("1/1");

        assertEquals("= 1.0", res);
    }
}
