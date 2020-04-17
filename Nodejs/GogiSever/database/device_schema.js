var crypto = require('crypto');

var Schema = {};

Schema.createSchema = function (mongoose) {

    // 스키마 정의
    var DeviceSchema = mongoose.Schema({
        mobile: { type: String, index: 'hashed', 'default': '' },
        osVersion: { type: String, 'default': '' },
        model: { type: String, 'default': '' },
        display: { type: String, 'default': '' },
        manufacturer: {type: String, 'default': ''},
        macAddress: {type: String, 'default': ''},
        registrationId: { type: String, 'default': '' },
        created_at: { type: Date, index: { unique: false }, 'default': Date.now },
        updated_at: { type: Date, index: { unique: false }, 'default': Date.now },
    });

    // 필수 속성에 대한 유효성 확인(길이 값 체크)
    DeviceSchema.path('mobile').validate(function (mobile) {
        return mobile.length;
    }, 'Value of mobile column is NULL');

    // 스키마에 static 메소드 추가
    DeviceSchema.static('findByMobile', function (mobile, callback) {
        return this.find({ mobile: mobile }, callback)
    });

    DeviceSchema.static('findAll', function (callback) {
        return this.find({}, callback);
    });

    DeviceSchema.static('load', function(options, callback){
        options.select = options.select || 'mobile';
        this.findOne(options.criteria).select(options.select).exec(callback);
    })

    // Register schema to model
    mongoose.model('Device', DeviceSchema);
    console.log('Define the DeviceSchema.');

    return DeviceSchema;
}

// module.exports에 UserSchema 객체 직접 할당
module.exports = Schema;