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
        int randomIndex = (int) (Math.random() * messages.length);
        return messages[randomIndex];
    }
}
