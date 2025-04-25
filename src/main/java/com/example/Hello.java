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
        int randomIndex = (int) (Math.random() * messages.length);
        return messages[randomIndex];
    }
}
