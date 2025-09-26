# Patrones de Diseño - Documento Descriptivo

Este documento proporciona una descripción detallada de los patrones de diseño implementados en este repositorio, siguiendo la documentación de [Refactoring Guru](https://refactoring.guru/es/design-patterns).

## Índice

1. [Patrones Creacionales](#patrones-creacionales)
2. [Patrones Estructurales](#patrones-estructurales)  
3. [Patrones de Comportamiento](#patrones-de-comportamiento)

---

## Patrones Creacionales

Los patrones creacionales proporcionan varios mecanismos de creación de objetos que incrementan la flexibilidad y la reutilización del código existente.

### Patrones incluidos:
- **Factory Method**: Proporciona una interfaz para crear objetos en una superclase, permitiendo que las subclases alteren el tipo de objetos que se crearán.
- **Abstract Factory**: Permite producir familias de objetos relacionados sin especificar sus clases concretas.
- **Builder**: Permite construir objetos complejos paso a paso.
- **Prototype**: Permite copiar objetos existentes sin que el código dependa de sus clases.
- **Singleton**: Garantiza que una clase tenga una única instancia y proporciona un punto de acceso global a ella.

---

## Patrones Estructurales

Los patrones estructurales explican cómo ensamblar objetos y clases en estructuras más grandes, manteniendo estas estructuras flexibles y eficientes.

### Patrones incluidos:
- **Adapter**: Permite la colaboración entre objetos de interfaces incompatibles.
- **Bridge**: Divide una clase grande o un grupo de clases estrechamente relacionadas en dos jerarquías separadas.
- **Composite**: Permite componer objetos en estructuras de árbol y trabajar con estas estructuras como si fueran objetos individuales.
- **Decorator**: Permite añadir comportamientos a objetos colocándolos dentro de objetos encapsuladores especiales.
- **Facade**: Proporciona una interfaz simplificada a una biblioteca, un framework o cualquier otro grupo complejo de clases.
- **Flyweight**: Permite mantener más objetos dentro de la cantidad disponible de RAM compartiendo eficientemente las partes comunes del estado entre varios objetos.
- **Proxy**: Permite proporcionar un sustituto o marcador de posición para otro objeto.

---

## Patrones de Comportamiento

Los patrones de comportamiento tratan con algoritmos y la asignación de responsabilidades entre objetos.

### Patrones incluidos:
- **Chain of Responsibility**: Permite pasar solicitudes a lo largo de una cadena de manejadores.
- **Command**: Convierte una solicitud en un objeto independiente que contiene toda la información sobre la solicitud.
- **Interpreter**: Define una representación para una gramática y un intérprete para evaluar sentencias.
- **Iterator**: Permite recorrer elementos de una colección sin exponer su representación subyacente.
- **Mediator**: Permite reducir las dependencias caóticas entre objetos.
- **Memento**: Permite guardar y restaurar el estado previo de un objeto sin revelar los detalles de su implementación.
- **Observer**: Permite definir un mecanismo de suscripción para notificar a varios objetos sobre cualquier evento.
- **State**: Permite a un objeto alterar su comportamiento cuando su estado interno cambia.
- **Strategy**: Permite definir una familia de algoritmos, colocarlos en clases separadas y hacer sus objetos intercambiables.
- **Template Method**: Define el esqueleto de un algoritmo en la superclase pero permite que las subclases sobrescriban pasos específicos.
- **Visitor**: Permite separar algoritmos de los objetos sobre los que operan.

---

## Estructura del Repositorio

```
patrones-de-diseno/
├── patrones-creacionales/
│   ├── factory_method.py
│   ├── abstract_factory.py
│   ├── builder.py
│   ├── prototype.py
│   └── singleton.py
├── patrones-estructurales/
│   ├── adapter.py
│   ├── bridge.py
│   ├── composite.py
│   ├── decorator.py
│   ├── facade.py
│   ├── flyweight.py
│   └── proxy.py
├── patrones-de-comportamiento/
│   ├── chain_of_responsibility.py
│   ├── command.py
│   ├── interpreter.py
│   ├── iterator.py
│   ├── mediator.py
│   ├── memento.py
│   ├── observer.py
│   ├── state.py
│   ├── strategy.py
│   ├── template_method.py
│   └── visitor.py
├── diagramas/
│   ├── patrones-creacionales/
│   ├── patrones-estructurales/
│   └── patrones-de-comportamiento/
└── documentos/
```

Cada patrón incluye:
- Implementación en Python
- Diagrama UML/conceptual
- Ejemplo de uso
- Explicación detallada

---

**Referencia:** [https://refactoring.guru/es/design-patterns](https://refactoring.guru/es/design-patterns)