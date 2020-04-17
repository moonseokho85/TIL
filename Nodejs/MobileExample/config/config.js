module.exports = {
    server_port: 3000,
    db_url: 'mongodb://localhost:27017/local',
    db_schemas: [
        { file: './user_schema', collection: 'users6', schemaName: 'UserSchema', modelName: 'UserModel' },
        { file: './device_schema', collection: 'devices', schemaName: 'DeviceSchema', modelName: 'DeviceModel' },
    ],
    route_info: [
        { file: './user', path: '/process/login', method: 'login', type: 'post' },
        { file: './user', path: '/process/adduser', method: 'adduser', type: 'post' },
        { file: './user', path: '/process/listuser', method: 'listuser', type: 'post' },
        
        { file: './test', path: '/process/test1', method: 'test1', type: 'post' },
        
        { file: './device', path: '/process/adddevice', method: 'adddevice', type: 'post' },
        { file: './device', path: '/process/listdevice', method: 'listdevice', type: 'post' },

        { file: './tensorflow', path: '/process/predict', method: 'predict', type: 'post' },
    ],
    facebook: {
        clientID: '620683745179757',
        clientSecret: '19f64f083a354a87da626a7af670511b',
        callbackURL: '/auth/facebook/callback'
    }
}