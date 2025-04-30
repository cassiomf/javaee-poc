package com.example;

public class Hello {
    public String greet(String name) {
        return "Hello, " + name;
    }

    public String greetMultipleLanguages(String name, String language) {
        if ("Spanish".equals(language)) {
            return "Hola, " + name;
        } else if ("French".equals(language)) {
            return "Bonjour, " + name;
        } else if ("French".equals(language)) {
            return "Bonjour, " + name;
        } else if ("German".equals(language)) {
            return "Hallo, " + name;
        } else {
            return greet(name);
        }
    }
}
