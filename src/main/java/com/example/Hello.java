package com.example;

public class Hello {

    public enum Language {
        ENGLISH("en"),
        SPANISH("es"),
        ITALIAN("it"),
        GERMAN("de");

        private String code;

        Language(String code) {
            this.code = code;
        }

        public static Language fromString(String code) {
            for (Language lang : Language.values()) {
                if (lang.code.equalsIgnoreCase(code)) {
                    return lang;
                }
            }
            return ENGLISH; // default to English
        }
    }

    public String greet(String name) {
        return "Hello, " + name;
    }

    public String greetWithMultipleLanguages(String name, String language) {
        switch (Language.fromString(language)) {
            case SPANISH:
            return "Hola, " + name;
            case ITALIAN:
            return "Ciao, " + name;
            case GERMAN:
            return "Hallo, " + name;
            default:
            return greet(name);
        }
        
    }
}
