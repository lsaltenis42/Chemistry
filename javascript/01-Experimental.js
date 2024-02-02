
function Rectangle(length, width) {
    this.length;
    this.width;

    this.draw = function () {
        console.log("|");
        console.log("-".repeat(this.width));
        console.log("|");
        for (let i = 0; i < this.length; i++){
            console.log("|");
            " ".repeat(this.width);
            console.log("|")
        }
        console.log("|");
        console.log("-".repeat(this.width));
        console.log("|");
    }
}

const Rectangle1 = new Rectangle(5, 10);
Rectangle1.draw();
