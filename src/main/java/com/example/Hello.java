package com.example;

public class Hello {
    public String greet(String name) {
        return "Hello, " + name;
    }

    public String greetMultipleLanguages(String name, String language) {
        if (language.equalsIgnoreCase("spanish")) {
            return "Hola, " + name;
        } else if (language.equalsIgnoreCase("french")) {
            return "Bonjour, " + name;
        } else if (language.equalsIgnoreCase("french")) {
            return "Bonjour, " + name;
        } else if (language.equalsIgnoreCase("german")) {
            return "Hallo, " + name;
        } else {
            return greet(name);
        }
    }
}
