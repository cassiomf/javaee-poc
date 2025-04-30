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
    public void testGreetMultipleLanguages() {
        Hello hello = new Hello();
        assertEquals("Hola, Bob", hello.greetMultipleLanguages("Bob", Hello.Language.SPANISH));
        assertEquals("Bonjour, Charlie", hello.greetMultipleLanguages("Charlie", Hello.Language.FRENCH));
        assertEquals("Hallo, David", hello.greetMultipleLanguages("David", Hello.Language.GERMAN));
        assertEquals("Hello, Eve", hello.greetMultipleLanguages("Eve", Hello.Language.DEFAULT));
    }
}
