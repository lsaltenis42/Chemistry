function Rectangle(width, height) {
    this.width;
    this.height;

    this.draw = function () {
        if (width < 1 || height < 1){
            console.log("Invalid dimensions!")
            return
        } else {
            console.log("|" + "\u203E".repeat(width) + "|")
            for (let _ = 0; _ < height - 2; _++){
                console.log("|" + " ".repeat(width) + "|");
            }
            if (height == 1){
                console.log(" " + "\u203E".repeat(width) + " ")
            } else {
                console.log("|" + "\u005F".repeat(width) + "|")
            }
            
        }
    }
}

const Rectangle1 = new Rectangle(1, 1);
const Rectangle2 = new Rectangle(2, 2);

Rectangle1.draw();
Rectangle2.draw();
