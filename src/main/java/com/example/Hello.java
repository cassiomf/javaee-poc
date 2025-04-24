package com.example;

import java.security.SecureRandom;

public class Hello {
    public String greet(String name) {
        return "Hello, " + name;
    }

    /*
     * This method generates a greeting message, with a random message from a list.
     */
    public String greetWithRambomMessage(String name) {
        String[] messages = {"Hello", "Hi", "Greetings", "Salutations"};
        SecureRandom random = new SecureRandom();
        byte bytes[] = new byte[messages.length];
        random.nextBytes(bytes);
        return messages[random.nextInt(messages.length)] + ", " + name;
    }

    /*
     * This method generates a farewell message for the given name.
     */
    public String farewell(String name) {
        String message = "Goodbye, " + name;
        return message;
    }
}
