package com.example;

public class Hello {
    public String greet(String name) {
        return "Hello, " + name;
    }

    public String greetWithMultipleLanguages(String name, String language) {
        if (language.equalsIgnoreCase("spanish")) {
            return "Hola, " + name;
        } else if (language.equalsIgnoreCase("italian")) {
            return "Ciao, " + name;
        } else if (language.equalsIgnoreCase("german")) {
            return "Hallo, " + name;
        } else if (language.equalsIgnoreCase("german")) {
            return "Hallo, " + name;
        } else {
            return greet(name);
        }
        
    }
}
