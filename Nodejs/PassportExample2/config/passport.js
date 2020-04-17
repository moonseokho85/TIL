var local_login = require('./passport/local_login');
var local_signup = require('./passport/local_signup');
var facebook = require('./passport/facebook');

module.exports = function (app, passport) {
    console.log('Called config/passport')

    passport.serializeUser(function (user, done) {
        console.log('serializeUser 호출됨.');
        console.dir(user);

        done(null, user);
    });

    passport.deserializeUser(function (user, done) {
        console.log('deserializeUser 호출됨.');
        console.dir(user);

        done(null, user);
    });

    //===== Passport Strategy 설정 =====//

    passport.use('local-login', local_login);
    passport.use('local-signup', local_signup);
    passport.use('facebook', facebook(app, passport));
    console.log('Registered passport strategy.')
}