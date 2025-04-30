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
    public void testGreetWithMultipleLanguages() {
        Hello hello = new Hello();
        assertEquals("Hola, Bob", hello.greetWithMultipleLanguages("Bob", "es"));
        assertEquals("Ciao, Charlie", hello.greetWithMultipleLanguages("Charlie", "it"));
        assertEquals("Hallo, David", hello.greetWithMultipleLanguages("David", "de"));
        assertEquals("Hello, Eve", hello.greetWithMultipleLanguages("Eve", "fr")); // default to English
    }
}
