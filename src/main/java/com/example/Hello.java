package com.example;

public class Hello {
    public enum Language {
        SPANISH, FRENCH, GERMAN, DEFAULT
    }

    public String greet(String name) {
        return "Hello, " + name;
    }

    public String greetMultipleLanguages(String name, Language language) {
        switch (language) {
            case SPANISH:
                return "Hola, " + name;
            case FRENCH:
                return "Bonjour, " + name;
            case GERMAN:
                return "Hallo, " + name;
            default:
                return greet(name);
        }
    }
}
