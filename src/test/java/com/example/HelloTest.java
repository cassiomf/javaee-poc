package com.example;

import org.junit.Test;
import static org.junit.Assert.*;

public class HelloTest {
    @Test
    public void testGreet() {
        Hello hello = new Hello();
        assertEquals("Hello, Alice", hello.greet("Alice"));
    }

    @Test
    public void testGreetRandomMessage() {
        Hello hello = new Hello();
        String name = "Bob";
        String result = hello.greetRandomMessage(name);
        assertTrue(result.startsWith("Hello, " + name) || 
                   result.startsWith("Hi, " + name) || 
                   result.startsWith("Greetings, " + name) || 
                   result.startsWith("Welcome, " + name));
    }
}
