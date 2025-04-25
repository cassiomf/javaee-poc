package com.example;

public class Hello {
    public String greet(String name) {
        return "Hello, " + name;
    }

    public String greetRandomMessage(String name) {
        String[] messages = {
            "Hello, " + name,
            "Hi, " + name,
            "Greetings, " + name,
            "Welcome, " + name
        };
        java.security.SecureRandom secureRandom = new java.security.SecureRandom();
        int randomIndex = secureRandom.nextInt(messages.length);
        return messages[randomIndex];
    }
}
