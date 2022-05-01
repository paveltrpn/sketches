let process = require("process")

class exprString_c {
    /**
     * 
     * @param {string} expr 
     */
    constructor(expr) {
        this.expression = expr
        this.pos = 0
    }

    getNextChar() {
        if ((this.pos + 1) > (this.expression.length)) {
            return [-1, ""]
        }

        let rt = this.expression[this.pos]
        this.pos = this.pos + 1
        return [this.pos, rt]
    }

    /**
     * 
     * @param {number} npos 
     * @returns {number}
     */
    setPos(npos) {
        if ((npos > this.expression.length) | (npos < 0)) {
            return -1
        }

        this.pos = npos
        return 0
    }

    /**
     * 
     * @param {string} nexpr 
     */
    loadNewExpression(nexpr) {
        this.expression = nexpr
        this.pos = 0
    }

    getExprLen() {
        return this.expression.length
    }

    /**
     * 
     * @param {string} ch 
     */
    appendChar(ch) {
        this.expression = this.expression + ch
    }
}

let lookahead = ""
let expressionLine = new exprString_c("9+5-2")
let expressionOut = new exprString_c("")

function expr() {
    term()
    while (true) {
        if (lookahead == "+") {
            match("+")
            term()
            expressionOut.appendChar("+")
        } else if (lookahead == "-") {
            match("-")
            term()
            expressionOut.appendChar("-")
        } else {
            return
        }
    }
}

function term() {
    if (!isNaN(lookahead)) {
        let t = lookahead
        match(lookahead)
        expressionOut.appendChar(t)
    } else {
        console.log("syntax error in term()! " + lookahead + "- is not number!")
        process.exit(0)
    }
}

/**
 * @param {string} t
 */
function match(t) {
    if (lookahead == t) {
        lookahead = expressionLine.getNextChar()[1]
    } else {
        console.log("syntax error in match()!")
        process.exit(0)
    }
}

(function main() {
    lookahead = expressionLine.getNextChar()[1]

    expr()

    console.log(expressionOut.expression)
}) ()
