// Express 기본 모듈 불러오기
var express = require("express");
var http = require("http");
var path = require("path");

// Express의 미들웨어 불러오기
var bodyParser = require("body-parser");

// 쿠키 모듈 사용
var cookieParser = require("cookie-parser");
var static = require("serve-static");
var errorHandler = require('errorHandler');

// 오류 핸들러 모듈 사용
var expressErrorHandler = require("express-error-handler");

// 세션 모듈 사용
var expressSession = require("express-session");

var user = require('../PassportExample2/routes/user')

var database_loader = require('../PassportExample2/database/database_loader');

var route_loader = require('../PassportExample2/routes/route_loader')

//===== Passport 사용 =====//
var passport = require('passport');
var flash = require('connect-flash');

// 익스프레스 객체 생성
var app = express();

//===== 뷰 엔진 설정 =====//
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
console.log('뷰 엔진이 ejs로 설정되었습니다.');

// app.set('view engine', 'pug');
// console.log('뷰 엔진이 pug로 설정되었습니다.');

var config = require('./config');

//===== 서버 변수 설정 및 static으로 [public] 폴더 설정 =====//
console.log('config.server_port: %d', config.server_port);
app.set('port', process.env.PORT || config.server_port || 3000);

// public 폴더를 static으로 오픈
app.use('/public', static(path.join(__dirname, 'public')));

// body-parser를 사용해 application/x-www-form-urlencoded 파싱
app.use(bodyParser.urlencoded({ extended: false }));

// body-parser를 사용해 application/json 파싱
app.use(bodyParser.json());

// cookie-parser 설정
app.use(cookieParser());

// 세션 설정
app.use(expressSession({
    secret: 'my key',
    resave: true,
    saveUninitialized: true
}));

//===== Passport 초기화 =====//
app.use(passport.initialize());
app.use(passport.session());
app.use(flash());

//===== Passport Strategy 설정 =====//
var LocalStrategy = require('passport-local').Strategy;

passport.use('local-login', new LocalStrategy({
    usernameField: 'email', passwordField: 'password', passReqToCallback: true
}, function (req, email, password, done) {
    console.log('passport의 local-login 호출됨: ' + email + ', ' + password);

    var database = app.get('database');
    console.log(database)
    database.UserModel.findOne({
        'email': email, function(err, user) {
            if (err) {
                console.log('에러 발생함.')
                return done(err);
            }

            if (!user) {
                console.log('사용자 아이디가 일치하지 않습니다.');
                return done(null, false, req.flash('loginMessage', '등록한 계정이 없습니다.'));
            }

            var authenticated = user.authenticate(password, user._doc.salt, user._doc.hashed_password);
            if (!authenticated) {
                console.log('비밀번호가 일치하지 않습니다.');
                return done(null, false, req.flash('loginmessage', '일치하는 비밀번호가 없습니다.'));
            }

            console.log('아이디와 비밀번호가 일치합니다.');
            return done(null, user)
        }
    });
}));

passport.use('local-signup', new LocalStrategy({
    usernameField: 'email',
    passwordField: 'password',
    passReqToCallback: true
}, function (req, email, password, done) {
    var paramName = req.body.name || req.query.name;
    console.log('passport의 local-signup 호출됨: ' + email + ', ' + password + ', ' + paramName);

    var database = app.get('database');
    database.UserModel.findOne({ 'email': email }, function (err, user) {
        if (err) {
            console.log('에러 발생.');
            return done(err);
        }

        if (user) {
            console.log('기존에 계정이 있습니다.');
            return done(null, false, req.flash('signupMessage', '계정이 이미 있습니다.'));
        } else {
            var user = new database.UserModel({ 'email': email, 'password': password, 'name': paramName });
            user.save(function (err) {
                if (err) {
                    console.log('데이터베이스 저장 시 에러')
                    return done(null, false, req.flash('signupMessage', '사용자 정보 저장 시 에러가 발생했습니다.'));
                }

                console.log('사용자 데이터 저장함.');
                return done(null, user);
            })
        }
    })
}));

passport.serializeUser(function (user, done) {
    console.log('serializeUser 호출됨.');
    console.dir(user);

    done(null, user);
});

passport.deserializeUser(function (user, done) {
    console.log('deserializeUser 호출됨.');
    console.dir(user);

    done(null, user);
})

var router = express.Router();
route_loader.init(app, router);

// ===== 회원가입과 로그인 라우팅 함수 =====//
router.route('/').get(function (req, res) {
    console.log('/ 패스로 요청됨.');

    res.render('index.ejs');
})

router.route('/login').get(function (req, res) {
    console.log('/login 패스로  GET 요청됨.');

    res.render('login.ejs', { message: req.flash('loginMessage') });
})

router.route('/login').post(passport.authenticate('local-login', {
    successRedirect: '/profile',
    failureRedirect: '/login',
    failureFlash: true
}));

router.route('/signup').get(function (req, res) {
    console.log('/signup 패스로 GET 요청됨.');

    res.render('signup.ejs', { message: req.flash('signupMessage') });
})

router.route('/signup').post(passport.authenticate('local-signup', {
    successRedirect: '/profile',
    failureRedirect: '/signup',
    failureFlash: true
}))

router.route('/profile').get(function (req, res) {
    console.log('requested GET method to /profile path');

    console.log('Object information of req.user');
    console.dir(req.user);

    if (!req.user) {
        console.log('Unauthenticated State.')
        res.redirect('/');
    } else {
        console.log('Authenticated state.');

        if (Array.isArray(req.user)) {
            res.render('profile.ejs', { user: req.user[0]._doc });
        } else {
            res.render('profile.ejs', { user: req.user });
        }
    }
});

router.route('/logout').get(function(req, res){
    console.log('requested GET method to /logout path.');

    req.logout();
    res.redirect('/');
})


// 모든 router 처리 끝난 후 404 오류 페이지 처리
var errorHandler = expressErrorHandler({
    static: {
        "404": "./public/404.html",
    },
});

app.use(expressErrorHandler.httpError(404));
app.use(errorHandler);

//===== 서버 시작 =====//
http.createServer(app).listen(app.get('port'), function () {
    console.log("서버가 시작되었습니다. 포트 : " + app.get('port'));

    // 데이터베이스 연결
    database_loader.init(app, config);
});