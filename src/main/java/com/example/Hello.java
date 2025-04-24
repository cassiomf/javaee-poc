package com.example;

import java.security.SecureRandom;

public class Hello {
    public String greet(String name) {
        return "Hello, " + name;
    }

    public String greetWithRambomMessage(String name) {
        String[] messages = {"Hello", "Hi", "Greetings", "Salutations"};
        SecureRandom random = new SecureRandom();
        byte bytes[] = new byte[20];
        random.nextBytes(bytes);
        return messages[random.nextInt()] + ", " + name;
    }

    public String farewell(String name) {
        String message = "Goodbye, " + name;
        return message;
    }
}
