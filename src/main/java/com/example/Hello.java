package com.example;

public class Hello {
    public String greet(String name) {
        return "Hello, " + name;
    }

    public String greetWithRandomString(String name) {
        String[] array = {
            "Hello, " + name,
            "Hi, " + name,
            "Greetings, " + name,
            "Salutations, " + name,
            "Howdy, " + name
        };
        int randomIndex = (int) (Math.random() * array.length);
        return array[randomIndex];
    }
}
