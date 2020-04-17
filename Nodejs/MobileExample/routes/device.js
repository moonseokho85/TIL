var adddevice = function (req, res) {
    console.log('Called adddevice function in device module.');

    var database = req.app.get('database');
    var paramMobile = req.param('mobile');
    var paramOsVersion = req.param('osVersion');
    var paramModel = req.param('model');
    var paramDisplay = req.param('display');
    var paramManufacturer = req.param('manufacturer');
    var paramMacAddress = req.param('macAddress');

    // Case of initiated database object
    if (database.db) {

        // Create DeviceModel instance
        var device = new database.DeviceModel({
            "mobile": paramMobile,
            "osVersion": paramOsVersion,
            "model": paramModel,
            "display": paramDisplay,
            "manufacturer": paramManufacturer,
            "macAddress": paramMacAddress,
        });

        // Save data by save()
        device.save(function (err) {
            if (err) {
                console.log('Error occurs on the way to adding the device information: ' + err.stack);

                res.writeHead(200, { 'Content-Type': 'text/html;charset=utf8' });
                res.write('<h2>Error occurs on the way to adding the device information</h2>');
                res.write('<p>' + err.stack + '</p>');
                res.end();

                return;
            }

            console.log('Added device data.');

            console.dir(device);

            res.writeHead(200, { 'Content-Type': 'application/json;charset=utf8' });
            res.write("{code: '200', 'message': 'Success of adding device data.'}")
            res.end();
        });
    }
}

var listdevice = function(req, res){
    console.log('Called listdevice in device module.');

    var database = req.app.get('database');

    // Case of initiated database object
    if(database.db){
        // 1. Search all devices
        database.DeviceModel.findAll(function(err, results){
            if(err){
                console.log('Error occurs on the way to looking up the device list: ' + err.stack);

                res.writeHead(200, { 'Content-Type': 'text/html;charset=utf8' });
                res.write('<h2>Error occurs on the way to looking up the device list</h2>');
                res.write('<p>' + err.stack + '</p>');
                res.end();

                return;
            }

            if(results){
                console.dir(results);

                var context = {
                    title: '단말 목록',
                    devices: results
                };

                req.app.render('listdevice', context, function(err, html){
                    res.end(html);
                })
            }
        })
    }
}

module.exports.adddevice = adddevice;
module.exports.listdevice = listdevice;