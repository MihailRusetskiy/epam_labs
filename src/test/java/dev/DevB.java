package dev;

import calculator.Calculator;
import org.junit.Test;
import static junit.framework.Assert.assertEquals;


public class DevB {
    @Test
    public void testSumA() throws Exception {

        String res = new Calculator().calculate("1/0");

        assertEquals("= Infinity", res);
    }
}
