var util = require('util');
var EventEmitter = require('events').EventEmitter;

var Calc = () => {
    var self = this;

    this.on('stop', () => {
        console.log('Calc에 stop event 전달됨.');
    });
};

util.inherits(Calc, EventEmitter);

Calc.prototype.add = (a, b) => {
    return a + b;
}

module.exports = Calc;
module.exports.title = 'calculator';