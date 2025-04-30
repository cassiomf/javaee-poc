package com.example;

public class Hello {
    public String greet(String name) {
        return "Hello, " + name;
    }

    public String greetMultipleLanguages(String name, String language) {
        switch (language.toLowerCase()) {
            case "spanish":
                return "Hola, " + name;
            case "french":
                return "Bonjour, " + name;
            case "german":
                return "Hallo, " + name;
            default:
                return greet(name);
        }
    }
}
