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

var user = require('./routes/user')

var database_loader = require('./database/database_loader');

var route_loader = require('./routes/route_loader')

//===== Passport 사용 =====//
var passport = require('passport');
var flash = require('connect-flash');

// 익스프레스 객체 생성
var app = express();

//===== 뷰 엔진 설정 =====//
app.set('views', __dirname + '/views');
// app.set('view engine', 'ejs');
// console.log('뷰 엔진이 ejs로 설정되었습니다.');

app.set('view engine', 'pug');
console.log('뷰 엔진이 pug로 설정되었습니다.');

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

route_loader.init(app, express.Router())

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