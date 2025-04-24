package com.example;

public class Hello {
    public String greet(String name) {
        return "Hello, " + name;
    }

    public String greetWithRambomMessage(String name) {
        String[] messages = {"Hello", "Hi", "Greetings", "Salutations"};
        int randomIndex = (int) (Math.random() * messages.length);
        return messages[randomIndex] + ", " + name;
    }

    public String farewell(String name) {
        String message = "Goodbye, " + name;
        return message;
    }
}
