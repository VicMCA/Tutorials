/*
Quick reference guide on how to use classes and objects in JavaScript.
We take a look at the structure of objects, classes, inheritance, getters
and setters, methods and how to use them in a basic way.
*/

const objSquare = {                             // Creating an object. Using "const" instead of "var" or "let" is encouraged
    length: 5,
    vertices: 4,                                // Normal properties
    color: "green",
    location: { x: 0, y: 0 },                   // Using an object as property

    draw() {                                    // Method for this object
        return (`I'm a ${this.vertices}-sided polygon, and my sides have ${this.length}mm in length.`
        + `\nMy color is ${this.color} and I'm located at ${this.location.x} ${this.location.y}.`)
    }
}

class Polygon {                                 // Class creation
    #ImSecret = "I'm a private property";       // This is a private property
    constructor(length, vertices) {             // Class' constructor with parameters
        this._length = length;                  // Normal properties from parameters
        this._vertices = vertices;              // Use of "this" keyword is needed to reference the objects
        this._location = { x: 0, y: 0 };        // An object used as property
    }
    get location() {                            // Getter function, called without brackets when used
        return this._location;                  // The "_" is to generate another variable, so as to not create a stack overflow
    }
    set location(newLocation) {                 // Setter function, also called without brackets when used
        this._location = newLocation;           // Again, we use "_" to avoid a stack overflow
    }
    draw() {                                    // Normal method for the object created from this class
        return `I am a ${this._vertices}-sided polygon, and my sides have ${this._length}mm in length.`;
    }
    changeMe() {
        return `I'm a method from the original (or parent) class`;
    }
    revealSecret() {                            // This method can return a private property
        return this.#ImSecret + " but you have discovered me!";
    }
    changeSecret(newSecret) {                   // This method can change the private property's value
        this.#ImSecret = newSecret
    }
}

class ColorPolygon extends Polygon {          // Class extended from previous class
    constructor(length, vertices, color) {      // The constructor needs the basic parameters + any new ones
        super(length, vertices);                // We call the parent class' parameters using "super()"
        this._color = color;                    // New parameters are attributed after that
    }
    get color() {                               // New getter for child class' property
        return this._color;
    }
    set color(newColor) {                       // New setter for child class' property
        this._color = newColor;
    }                                           // Parent class' getters, setters and methods are inherited
    changeMe() {                                // Inherited methods and properties can be overwritten.
        return (`I'm a method from the extended (or child) class.\n`
        + `I'm clearly better since I remembered to finish my sentence with a period.`);
    }

}

function main() {
    /* OBJECT HANDLING */
    console.log("<< A nice square object >>\n")
    
    console.log(objSquare.draw());              // Calling an object's normal method
    console.table(objSquare);                   // Printing an object's properties in a table
    objSquare.color = "ultramarine";            // Changing an object's property directly
    objSquare.location = { x: 3, y: 7 };        // Changing an object's object property (confusing, I know) directly
    console.log(objSquare.draw());              // Calling the method again to see the differences
    console.table(objSquare);                   // Printing the table again to check the object's changed properties


    /* CREATING AN OBJECT USING A CLASS AND HANDLING IT */
    console.log("\n\n<< A nice square object created with class >>\n")

    let square = new Polygon(12, 4);            // Creating an object from a class
    console.log(square.draw());                 // Calling an object's normal method
    console.log(square.changeMe());             // <- Original method from parent class
    console.log(square.revealSecret());
    console.table(square);                      // Printing an object's properties in a table

    
    /* CREATING AN OBJECT USING THE SUBCLASS AND HANDLING IT */
    console.log("\n\n<< A nice COLORED square object created with a subclass >>\n")

    let colorSquare = new ColorPolygon(9, 4, "turquoise");      // Creating an object from the child class
    console.log(colorSquare.draw());            // Using the parent class' inherited method
    console.log(colorSquare.changeMe());        // Using the changed inherited method
    console.log(colorSquare.revealSecret());
    console.table(colorSquare);                 // Printing an object's properties in a table
    
    colorSquare._length = 20;                   // Altering a property with no getter/setter by referencing it directly
    colorSquare.color = "sea green";            // Altering a property using the setter
    colorSquare.location = { x: 5, y: 8 };      // Altering an object property using the setter
    colorSquare.changeSecret("The secret has changed");    // Changing a private property's value through a method

    console.log("\n\n<< The same nice COLORED square object but with CHANGES >>\n")
    
    console.log(colorSquare.draw());            // Calling the method again to see differences
    console.log(colorSquare.revealSecret());    // Calling the method again to see change in the private property
    console.table(colorSquare);                 // Printing to a table to see every difference
}


if (require.main === module) {
    main();
}


