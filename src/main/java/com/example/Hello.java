package com.example;

public class Hello {
    public String greet(String name) {
        String message = "Hello, " + name;
        return message;
    }

    public String greetRandomMessage(String name) {
        String[] messages = {
            "Hello, " + name,
            "Hi, " + name,
            "Greetings, " + name,
            "Welcome, " + name
        };
        java.util.Random random = new java.util.Random();
        int randomIndex = random.nextInt(messages.length);
        return messages[randomIndex];
    }
}
