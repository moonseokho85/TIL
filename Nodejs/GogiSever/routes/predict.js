
var predict = async function (req, res) {
    console.log('Called predict function in predict module.');

    const tf = require('@tensorflow/tfjs-node');

    const model = await tf.loadLayersModel('file://C:/Users/mseok/TIL/Nodejs/GogiServer/model/model.json');
    console.log("model: " + model);

};

module.exports.predict = predict;